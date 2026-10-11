# Een class met veel informatie over de gang van het spel.
from Core import Constants
import pygame

from Core.Entities.Spawner import Spawner
from Core.Functions import Find_Center, WriteHighScoreFile
from Core.Entities.Player import Player
from Core.Entities.Entity import Entity
from Core.Functions import Generate_Background


class GameInfo:
    def __init__(self, Game):
        self._Game = Game # Verwijzing naar boven.

        # Staat de game op pauze? Kan om veel redenen. Ui past zich hierop aan, en en de updates worden ook op pauze gezet
        self.Paused = False
        self.ShouldToggle = True

        # Dynamische background logica, functioneel geproduceerd
        self.Backgrounds = []
        for x in range(2):
            Background = Generate_Background()
            Background[1] = pygame.Vector2(0, -500 + (x * 500))
            self.Backgrounds.append(Background)

        self.Background_Speed = pygame.Vector2(0, 150)
        # Core properties
        self.Friction = 7

        # Een grote lijst met allemaal Entity-Class objecten. Kan hier iteratief alle Draw() en Update() functies uitvoeren
        # Speler staat hier NIET in, die staat een laag hoger, in Game, omdat er maar 1 speler is. Onderlinge collision is hier door niet mogelijk, maar het is wel efficient
        self.EntityList = []
        self.Spawner = Spawner(self)
         # Basis voor score hier.
        self.Score = 0 # na 180 seconden 5000 punten. Dus 180/5000 punten/seconden erbij

        # Speler van het spel, aparte class die boven alle andere logica staat
        self.Player = Player(self._Game, Find_Center(pygame.Vector2(50, 50), pygame.Vector2(500, 500)))

        # Tijd sinds Game_Start
        self.Time_Since_Game_Start = 0
    def Get_Game(self):
        return self._Game
    # Alle logica voor het updaten van het spel
    def Update(self, Eventstack):
        self.HandlePause(Eventstack)
        # Spel speelt normaal, anders spel op pauze
        if not self.Paused:
            # Enemy spawning update
            self.Spawner.Update()

            self.Player.Update(Eventstack) # Player Update
            # Update alle entities in het spel
            for Entity in self.EntityList:
                Entity.Update(Eventstack)
            if self.Player.Lives > 0:
                self.Score += (5000/180) * self._Game.Deltatime # zie score init voor definitie
            self.Time_Since_Game_Start += self._Game.Deltatime
            self.Update_Background()
    # Alle logica voor het tekenen op het scherm.
    def Draw(self):
        self.Player.Draw() # Player Draw Update
        # Teken alle entities in het spel.
        for Entity in self.EntityList:
            Entity.Draw()

    def Update_Background(self):
        # Update de positie van de achtergronden, is de achtergrond van het scherm af? Genereer een nieuwe
        Index = 0 # Indexeren yeahh
        for Background in self.Backgrounds:
            Background[1] += self.Background_Speed * self._Game.Deltatime
            if Background[1].y >= 500:
                # Reset de achtergrond
                self.Backgrounds[Index] = Generate_Background()
                self.Backgrounds[Index][1] = pygame.Vector2(0, -500)
            Index += 1
        # Snelheid van de backgrounds schaalt met de score
        self.Background_Speed = pygame.Vector2(0, 150 + (self.Score / 10) + self.Time_Since_Game_Start)
    def Get_Background(self):
        # Genereert de hele achtergrond, die de renderer dan weer blit.
        FullBackGround = pygame.Surface((500, 1000))
        for Background in self.Backgrounds:
            # Rendert de 2 achtergronden
            FullBackGround.blit(Background[0], Background[1])
        return [FullBackGround, pygame.Vector2(0, 0)]

    # Afschuiven van pauze-logica naar een aparte functie om het duidelijker te maken
    def HandlePause(self, Eventstack):
        # Pauze logica
        for Event in Eventstack:
            if Event.type == pygame.KEYDOWN and ((Event.key == pygame.K_ESCAPE) or (Event.key == pygame.K_p)):
                if self.ShouldToggle:
                    self.Paused = not self.Paused  # Toggle
                    if self.Paused: self._Game.Get_Audio_Manager().Pause_Music()
                    else: self._Game.Get_Audio_Manager().Resume_Music()
                self.ShouldToggle = False
                self._Game.Get_Audio_Manager().Play_Sound("Button_Click")
            elif Event.type == pygame.KEYUP and ((Event.key == pygame.K_ESCAPE) or (Event.key == pygame.K_p)):
                self.ShouldToggle = True
    # Kan én 1 entity toevoegen, of een groep van entities
    def Add_Entity(self, Entity: Entity|list):
        if type(Entity) is list:
            self.EntityList.extend(Entity)
            return
        self.EntityList.append(Entity)

    # Verwijdert de entity uit de entitylist, waardoor ze niet meer geupdate worden
    def Remove_Entity(self, Entity):
        self.EntityList.remove(Entity)

    # Terug naar het menu.
    def End_Game(self):
        # Highscore voor de ranking
        self._Game.Attempts.append({"Score" : self.Score, "Time_Survived" : self.Time_Since_Game_Start})
        self._Game.Set_State(Constants.Game_State.Main_Menu)
        self._Game.Get_Ui_Manager().Update_ScoreBoard()
        WriteHighScoreFile(self._Game.Attempts)