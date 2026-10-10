# Een wrapper voor entity, met wat toegevoegde functionaliteit
import random

from pygame.sprite import Sprite

from Core.Functions import Clamp_Vector, Scale_Rect_From_Center
import pygame
from Core import Constants
from Core.Entities.Entity import Entity
import math

class EnemyBase(Entity):
    def __init__(self, Sprite, Game, Position, Speed=pygame.Vector2(0, 0)):
        super().__init__(Sprite, Game, Position, True)

        # Lijkt veel op de Player Class, Movement die je KAN gebruiken voor de Enemy Gedrag verder aan te vullen

        # Hoe snel beweegt de Enemy?
        self.Speed = Speed
        self.MaxSpeed = self.Speed # Moet altijd een pygame vector zijn
        # Hoe snel versnelt de Enemy?
        self.Acceleration = None

        self.Type = Constants.EnemyTypes.Standard

    def Update(self, Eventstack):
        # Update de rect, en schaal de hitbox naar 95% van de normale grootte voor de eerlijkheid van het spel, 10px marge zo
        self.Rect = Scale_Rect_From_Center(pygame.Rect(self.Position, self.Size), 0.95)
        self.Handle_Behaviour(Eventstack)


    def Draw(self):
        super().Draw()

    # Verwijdert zichzelf uit de gameinfo
    def Kill(self):
        self._Game.Get_GameInfo().Remove_Entity(self)

    # Default behaviour
    def Handle_Collision(self, Other_Entity):
        if not Other_Entity.Hit:
            Other_Entity.Hit = True
            Other_Entity.Hit_Timer = 0
            Other_Entity.Lives -= 1
    # Ook default update behaviour
    def Handle_Behaviour(self, Eventstack):
        # Hier oefent de snelheid de verplaatsing uit als functie van de acceleratie.
        self.Position += (self.Speed * self._Game.Deltatime)

        # Kijkt of de entity buiten het scherm valt. Zo ja, verwijder deze uit de entitylijst. 1000 zodat er lange ketens gemaakt
        # Kunnen worden
        if (
            self.Position.x > self._Game.Get_Screen().get_width() + 1000
            or self.Position.x < -2 * self.Size.x - 1000
            or self.Position.y > self._Game.Get_Screen().get_height() + 1000
            or self.Position.y < -2 * self.Size.y - 1000):
            self.Kill()

# POWERUPS
class ClearingBomb(EnemyBase):
    def __init__(self, Game, Position, Speed = 0):
        super().__init__(Constants.Images.Clearing_Bomb_Sprite, Game, Position, Speed)
        self.Type = Constants.EnemyTypes.PowerUp


    def Handle_Collision(self, Other_Entity):
        self._Game.Get_GameInfo().Score += 50 * len(self._Game.Get_GameInfo().EntityList)
        self._Game.Get_GameInfo().EntityList = [] # Verwijdert elke entity van de lijst, scherm wordt leeg.
# 1 extra leven :)
class Heart(EnemyBase):
    def __init__(self, Game, Position, Speed=0, Direction=pygame.Vector2(0, 0)):
        super().__init__(Constants.Images.Heart_PowerUp, Game, Position, Speed)
        self.Type = Constants.EnemyTypes.PowerUp

    def Handle_Collision(self, Other_Entity):
        # Update score als winst :)
        self._Game.Get_GameInfo().Score += 500
        if Other_Entity.Lives < 5:
            Other_Entity.Lives += 1
        self.Kill()

# Super basic enemy die gewoon beweegt
class SimpleEnemy(EnemyBase):
    def __init__(self, Sprite, Game, Position, Speed= pygame.Vector2(0, 0)):
        super().__init__(Sprite, Game, Position, Speed)# Sprite van deze is in principe onbepaald tot zijn richting bepaald is
        self.Type = Constants.EnemyTypes.Enemy

# Beweegt naar je toe terwijl hij valt
class TailGater(EnemyBase):
    def __init__(self, Game, Position, Speed=pygame.Vector2(0, 0)):
        super().__init__(Constants.Images.Tailgater_Enemy, Game, Position, Speed)
        # Slome accleratie
        self.Acceleration = pygame.Vector2(1000, 0)
        #self.MaxSpeed = pygame.Vector2(Speed, self.Speed.y)
        self.Type = Constants.EnemyTypes.Enemy

    def Handle_Behaviour(self, Eventstack): # TODO FIX
        DeltaX = self.Position.x - self._Game.Get_GameInfo().Player.Position.x
        # Kiest richting om in te bewegen
        if DeltaX > 0: Direction = pygame.Vector2(-1, 0)
        elif DeltaX < 0: Direction = pygame.Vector2(1, 0)
        else: Direction = pygame.Vector2(0, 0)
        self.Speed = self.Speed
        # Elementwise omdat hij anders het inproduct berekent en de snelheid omzet naar een scalar. Kostte mij veel debugtijd
        self.Speed += (Direction * self.Acceleration.elementwise() * self._Game.Deltatime)
        # Frictie
        self.Speed.x *= max(0, 1 - self._Game.Get_GameInfo().Friction * self._Game.Deltatime)
        self.Speed = Clamp_Vector(self.Speed, -self.MaxSpeed, self.MaxSpeed) # Houdt de snelheid van de spelers binnen de kaders van het spel.

        super().Handle_Behaviour(Eventstack)

# Beweegt heen en weer als vijandig patroon
class OscilatingEnemy(EnemyBase): #TODO FIX
    def __init__(self, Game, Position, Speed=pygame.Vector2(0, 0)):
        super().__init__(Constants.Images.Oscillating_Enemy, Game, Position, Speed)
        self.Speed = Speed
        self.Type = Constants.EnemyTypes.Enemy
        self.Start_Position = Position.copy()

        # Waardes van oscilatie, nooit gedacht dat ik gonio zou gebruiken bij dit project:)
        self.Amplitude = random.randint(50, 100)
        self.Frequency = random.uniform(1, 3)
        self.Phase = random.uniform(0, 2 * math.pi)
    def Handle_Behaviour(self, Eventstack):
        # Random periode, amplitude en random startpositie
        self.Position.x = (
                self.Start_Position.x +
                math.sin(self.Frequency * self._Game.Get_GameInfo().Time_Since_Game_Start + self.Phase ) * self.Amplitude)
        super().Handle_Behaviour(Eventstack)
