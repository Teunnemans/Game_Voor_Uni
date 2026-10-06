# Een class met veel informatie over de gang van het spel.
from Core import Constants
import pygame

from Core.Entities.Spawner import Spawner
from Core.Entities.Test_Entity import TestEntity
from Core.Functions import Find_Center
from Core.Entities.Player import Player


class GameInfo:
    def __init__(self, Game):
        self._Game = Game # Verwijzing naar boven.

        # Staat de game op pauze? Kan om veel redenen. Ui past zich hierop aan, en en de updates worden ook op pauze gezet
        self.Paused = False
        self.ShouldToggle = True

        # Core properties
        self.Friction = 7

        # Een grote lijst met allemaal Entity-Class objecten. Kan hier iteratief alle Draw() en Update() functies uitvoeren
        # Speler staat hier NIET in, die staat een laag hoger, in Game, omdat er maar 1 speler is. Onderlinge collision is hier door niet mogelijk, maar het is wel efficient
        self.EntityList = []
        self.Spawner = Spawner(self)
         # Basis voor score hier.
        self.Score = 0 # na 180 seconden 5000 punten. Dus 180/5000 punten/seconden erbij

        # Speler van het spel, aparte class die boven alle andere logica staat
        self.Player = Player(Constants.Images.Player, self._Game, Find_Center(pygame.Vector2(50, 50), pygame.Vector2(500, 500)))

        #self.EntityList.append(TestEntity(Constants.Images.Player, self._Game, Find_Center(pygame.Vector2(50, 50), pygame.Vector2(500, 500))))

        # Tijd sinds Game_Start
        self.Time_Since_Game_Start = 0

        # Achtergrond van het spel. TODO maak deze dynamisch
        self.Background = Constants.Images.Background

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

            self.Score += (5000/180) * self._Game.Deltatime # zie score init voor definitie
            self.Time_Since_Game_Start += self._Game.Deltatime

        # TODO HIER MOET NOG SPEL LOGICA
    # Alle logica voor het tekenen op het scherm.
    def Draw(self):

        #TODO Dynamische ACHTERGROND
        self.Player.Draw() # Player Draw Update
        # Teken alle entities in het spel.
        for Entity in self.EntityList:
            Entity.Draw()

    # Afschuiven van pauze-logica naar een aparte functie om het duidelijker te maken
    def HandlePause(self, Eventstack):
        # Pauze logica
        for Event in Eventstack:
            if Event.type == pygame.KEYDOWN and ((Event.key == pygame.K_ESCAPE) or (Event.key == pygame.K_p)):
                if self.ShouldToggle: self.Paused = not self.Paused  # Toggle
                self.ShouldToggle = False
            elif Event.type == pygame.KEYUP and ((Event.key == pygame.K_ESCAPE) or (Event.key == pygame.K_p)):
                self.ShouldToggle = True

    def Add_Entity(self, Entity):
        self.EntityList.append(Entity)

    def Remove_Entity(self, Entity):
        self.EntityList.remove(Entity)