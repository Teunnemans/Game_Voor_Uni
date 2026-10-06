# Een wrapper voor entity, met wat toegevoegde functionaliteit
import random
from Core.Functions import Clamp_Vector
import pygame
from Core import Constants
from Core.Entities.Entity import Entity
import math

class EnemyBase(Entity):
    def __init__(self, Sprite, Game, Position):
        super().__init__(Sprite, Game, Position, True)

        # Lijkt veel op de Player Class, Movement die je KAN gebruiken voor de Enemy Gedrag verder aan te vullen

        # Hoe snel beweegt de Enemy?
        self.Speed = pygame.Vector2(0, 0)
        self.MaxSpeed = self.Speed # Moet altijd een pygame vector zijn
        # Hoe snel versnelt de Enemy?
        self.Acceleration = None


        self.Type = Constants.EnemyTypes.Standard

    def Update(self, Eventstack):
        super().Update(Eventstack)
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

#TODO enemies groeperen, enemeies een richting kunnen geven

# POWERUPS
class ClearingBomb(EnemyBase):
    def __init__(self, Sprite, Game, Position):
        super().__init__(Sprite, Game, Position)
        self.Type = Constants.EnemyTypes.PowerUp

    def Handle_Collision(self, Other_Entity):
        for Entity in self._Game.Get_GameInfo().EntityList:
            # Cleart elke entity behalve de powerups
            if Entity.Type is not Constants.EnemyTypes.PowerUp:
                Entity.Kill()
        self.Kill()
# 1 extra leven :)
class Heart(EnemyBase):
    def __init__(self, Sprite, Game, Position):
        super().__init__(Sprite, Game, Position)
        self.Type = Constants.EnemyTypes.PowerUp

    def Handle_Collision(self, Other_Entity):
        Other_Entity.Lives += 1
        self.Kill()
# 1 minder leven :( Lijkt op een powerup, maar is dit niet.
class HurtingBomb(EnemyBase):
    def __init__(self, Sprite, Game, Position, Visible: bool = True):
        super().__init__(Sprite, Game, Position)
        self.Type = Constants.EnemyTypes.PowerUp
    def Handle_Collision(self, Other_Entity):
        super().Handle_Collision(Other_Entity)
        self.Kill()
# ENEMIES

# Even kijken of mijn functionaliteiten werken
class SimpleEnemy(EnemyBase):
    def __init__(self, Sprite, Game, Position, Speed):
        super().__init__(Sprite, Game, Position)# anders scalair
        self.Speed = Speed
        self.Type = Constants.EnemyTypes.Enemy
# Beweegt naar je toe terwijl hij valt
class TailGater(EnemyBase):
    def __init__(self, Sprite, Game, Position, Speed):
        super().__init__(Sprite, Game, Position)
        # Slome accleratie
        self.Acceleration = pygame.Vector2(1000, 0)
        self.MaxSpeed = pygame.Vector2(Speed, self.Speed.y)
        self.Type = Constants.EnemyTypes.Enemy

    def Handle_Behaviour(self, Eventstack):
        DeltaX = self.Position.x - self._Game.Get_GameInfo().Player.Position.x
        # Kiest richting om in te bewegen
        if DeltaX > 0: Direction = pygame.Vector2(-1, 0)
        elif DeltaX < 0: Direction = pygame.Vector2(1, 0)
        else: Direction = pygame.Vector2(0, 0)
        # Elementwise omdat hij anders het inproduct berekent en de snelheid omzet naar een scalar. Kostte mij veel debugtijd
        self.Speed += (Direction * self.Acceleration.elementwise() * self._Game.Deltatime)
        # Frictie
        self.Speed.x *= max(0, 1 - self._Game.Get_GameInfo().Friction * self._Game.Deltatime)
        self.Speed = Clamp_Vector(self.Speed, -self.MaxSpeed, self.MaxSpeed) # Houdt de snelheid van de spelers binnen de kaders van het spel.

        super().Handle_Behaviour(Eventstack)

class OscilatingEnemy(EnemyBase):
    def __init__(self, Sprite, Game, Position):
        super().__init__(Sprite, Game, Position)
        self.Speed.y = 110
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
