import pygame

from Core import Constants
from Core.Entities.Entity import Entity
from Core.Functions import Clamp_Vector

# Speler class, handlet input en is centraal voor het spel. Is er maar 1 van in het spel.
class Player(Entity):
    def __init__(self, _Game, Position: pygame.Vector2 = pygame.Vector2(0,0)):
        super().__init__(Constants.Images.Player_Image, _Game, Position)

        # Hoe snel beweegt de speler?
        self.MaxSpeed = pygame.Vector2(250, 250)
        self.Speed = pygame.Vector2(0, 0)
        # Hoe snel versnelt de speler?
        self.Acceleration = pygame.Vector2(5000, 5000)

        self.CollidingList = []

        # Alle collider logica.
        self.Hit_Interval = 1.5 # 3 Seconden immuun na hit
        self.Hit_Timer = 0
        self.Hit = False
        self.Lives = 3 # 3 Levens als standaard
        self.Blink_Timer = 0
        self.Blink_Interval = 0.2
        self.Death_Time = 3
        self.Death_Timer = 0

    # Input die de speler verplaatst aan de hand van een paar variabelen zoals acceleratie etc.
    def Update_Movement(self):
        Keys = pygame.key.get_pressed()
        # Coole compactere versie van de inputregelaar die ik eerst had. Maakt van Direction een richtingvector die gebruikt
        # wordt bij het berekenen van de snelheid
        Direction = pygame.Vector2(
            Keys[pygame.K_RIGHT] - Keys[pygame.K_LEFT],
            Keys[pygame.K_DOWN] - Keys[pygame.K_UP] )

        # Nu ben je diagonaal niet meer sneller
        if Direction.length_squared() > 0:
            Direction = Direction.normalize()

        # Elementwise omdat hij anders het inproduct berekent en de snelheid omzet naar een scalar. Kostte mij veel debugtijd
        self.Speed += (Direction * self.Acceleration.elementwise() * self._Game.Deltatime)
        # Frictie
        self.Speed *= max(0, 1 - self._Game.Get_GameInfo().Friction * self._Game.Deltatime)
        self.Speed = Clamp_Vector(self.Speed, -self.MaxSpeed, self.MaxSpeed) # Houdt de snelheid van de spelers binnen de kaders van het spel.

        # Trekkracht, "Remt" de auto af als hij niet actief versnelt.
        self.Speed += pygame.Vector2(0, 750) * self._Game.Deltatime

        # Hier oefent de snelheid de verplaatsing uit als functie van de acceleratie.
        self.Position += (self.Speed * self._Game.Deltatime)
        # Houdt de speler binnen de kaders van het spel.
        self.Position = Clamp_Vector(self.Position, pygame.Vector2(0, 0), pygame.Vector2(self._Game.Get_Screen().get_size()) - (1, 1) * self.Size.elementwise())

    # Player side collision handling
    def Update_Collision(self):
        self.CollidingList = []
        for Entity in self._Game.Get_GameInfo().EntityList:
                if Entity.Rect.colliderect(self.Rect):
                    # Alle entities hebben expliciet uitgeschreven gedrag voor wat een collision zou moeten doen
                    Entity.Handle_Collision(self)
                    self.CollidingList.append(Entity)
                    return

    # Hit update handling
    def Update_Hit(self):
        if self.Hit:
            # Update timers
            self.Hit_Timer += self._Game.Deltatime
            self.Blink_Timer += self._Game.Deltatime

            # Knipperen
            if self.Blink_Timer >= self.Blink_Interval:
                self.Visible = not self.Visible
                self.Blink_Timer = 0
            if self.Hit_Timer > self.Hit_Interval:
                # Kan weer geraakt worden
                self.Hit = False
                self.Hit_Timer = 0
                self.Visible = True
                self.Blink_Timer = 0

    def Update(self, Eventstack):
        if self.Lives > 0:
            super().Update(Eventstack)
            self.Update_Movement()
            self.Update_Collision()
            self.Update_Hit()
        else:
            # DOOD FUNCTIONALITEIT
            self.Death_Timer += self._Game.Deltatime
            if self.Death_Timer > self.Death_Time:
                self._Game.Get_GameInfo().End_Game()

    def Draw(self):
        super().Draw()

