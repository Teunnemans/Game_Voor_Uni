# Een wrapper voor entity, met wat toegevoegde functionaliteit
import random
from Core.Functions import Scale_Rect_From_Center
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
        # Type van de "enemy", kan ook een powerup zijn
        self.Type = Constants.EnemyTypes.Standard

    def Update(self, Eventstack):
        # Update de rect, en schaal de hitbox naar 90% van de normale grootte voor de eerlijkheid van het spel, 10px marge zo
        self.Rect = Scale_Rect_From_Center(pygame.Rect(self.Position, self.Size), 0.90)
        self.Handle_Behaviour(Eventstack)

    # Verwijdert zichzelf uit de gameinfo
    def Kill(self):
        self._Game.Get_GameInfo().Remove_Entity(self)

    # Default behaviour
    def Handle_Collision(self, Other_Entity):
        if not Other_Entity.Hit:
            Other_Entity.Hit = True
            Other_Entity.Hit_Timer = 0
            Other_Entity.Lives -= 1
            self._Game.Get_Audio_Manager().Play_Sound("Hit")

    # Ook default update behaviour
    def Handle_Behaviour(self, Eventstack):
        # Hier oefent de snelheid de verplaatsing uit als functie van de acceleratie.
        self.Position += (self.Speed * self._Game.Deltatime)

        # Kijkt of de entity buiten het scherm valt. Zo ja, verwijder deze uit de entitylijst. 1000 zodat er lange ketens gemaakt
        # Kunnen worden
        if (self.Position.x > self._Game.Get_Screen().get_width() + 1000
            or self.Position.x < -2 * self.Size.x - 1000
            or self.Position.y > self._Game.Get_Screen().get_height() + 1000
            or self.Position.y < -2 * self.Size.y - 1000):
            self.Kill()

# POWERUPS
# Verwijdert alle entitys uit de gameinfo, en geeft score obv hoeveel entitys er zijn
class ClearingBomb(EnemyBase):
    def __init__(self, Game, Position, Speed = 0):
        super().__init__(Constants.Images.Clearing_Bomb_Sprite, Game, Position, Speed)
        self.Type = Constants.EnemyTypes.PowerUp

    def Handle_Collision(self, Other_Entity):
        self._Game.Get_GameInfo().Score += 10 * len(self._Game.Get_GameInfo().EntityList)
        self._Game.Get_GameInfo().EntityList = [] # Verwijdert elke entity van de lijst, scherm wordt leeg.
        self._Game.Get_Audio_Manager().Play_Sound("Clearing_Bomb")
# 1 extra leven :)
class Heart(EnemyBase):
    def __init__(self, Game, Position, Speed=0):
        super().__init__(Constants.Images.Heart_PowerUp, Game, Position, Speed)
        self.Type = Constants.EnemyTypes.PowerUp

    def Handle_Collision(self, Other_Entity):
        # Update score als winst :)
        self._Game.Get_GameInfo().Score += 500
        if Other_Entity.Lives < 5:
            Other_Entity.Lives += 1
        self.Kill()
        self._Game.Get_Audio_Manager().Play_Sound("Health")

# Super basic enemy die gewoon beweegt, heeft een richting en beweegt bijna altijd in een groep
class SimpleEnemy(EnemyBase):
    def __init__(self, Sprite, Game, Position, Speed= pygame.Vector2(0, 0)):
        super().__init__(Sprite, Game, Position, Speed)# Sprite van deze is in principe onbepaald tot zijn richting bepaald is
        self.Type = Constants.EnemyTypes.Enemy

# Beweegt naar je toe terwijl hij valt, goed voor opassen
class TailGater(EnemyBase):
    def __init__(self, Sprite, Game, Position, Speed=pygame.Vector2(0, 0)):
        super().__init__(Sprite, Game, Position, Speed)
        self.Type = Constants.EnemyTypes.Enemy
        # Hoe sterk de enemy naar de speler stuurt
        self.Acceleration = 200

    def Handle_Behaviour(self, Eventstack):
        # Kiest richting om in te bewegen
        # Richting naar de speler
        Direction = self._Game.Get_GameInfo().Player.Position - self.Position
        if Direction.length_squared() > 0:
            Direction = Direction.normalize()

        # Geleidelijk snelheid toevoegen richting de speler
        self.Speed += Direction * self.Acceleration * self._Game.Deltatime

        # Hier oefent de snelheid de verplaatsing uit als functie van de acceleratie.
        self.Position += (self.Speed * self._Game.Deltatime)

        # Kijkt of de entity buiten het scherm valt. Zo ja, kill zichzelf, doet dit eerder dan andere entitys want anders blijf hij je volgen
        # Kunnen worden
        if (self.Position.x > self._Game.Get_Screen().get_width() + 100
                or self.Position.x < -2 * self.Size.x - 100
                or self.Position.y > self._Game.Get_Screen().get_height() + 100
                or self.Position.y < -2 * self.Size.y - 100):
            self.Kill()



# Beweegt heen en weer als vijandig patroon, gebruikt gonio voor de verplaatsing
class OscilatingEnemy(EnemyBase):
    def __init__(self, Sprite, Game, Position, Speed=pygame.Vector2(0, 0)):
        super().__init__(Sprite, Game, Position, Speed)
        self.Speed = Speed
        self.Type = Constants.EnemyTypes.Enemy
        self.Start_Position = Position.copy()
        self.Elapsed_Time = 0

        # Waardes van oscilatie, nooit gedacht dat ik gonio zou gebruiken bij dit project:)
        self.Amplitude = random.randint(50, 100)
        self.Frequency = random.uniform(1, 3)
        self.Phase = random.uniform(0, 2 * math.pi)

        # Eenheidsvector van de bewegingsrichting
        Direction = Speed.normalize() if Speed.length_squared() > 0 else pygame.Vector2(0, 1)
        # Loodrechte vector op de bewegingsrichting, hierlangs beweegt de enemy
        self.Perpendicular = pygame.Vector2(-Direction.y, Direction.x)
    def Handle_Behaviour(self, Eventstack):
        self.Elapsed_Time += self._Game.Deltatime
        # Random periode, amplitude en random startpositie
        self.Start_Position += (self.Speed * self._Game.Deltatime)
        # Oscillatie loodrecht op de bewegingsrichting
        Offset = self.Perpendicular * ( math.sin(self.Frequency * self.Elapsed_Time + self.Phase) * self.Amplitude)

        self.Position = self.Start_Position + Offset

        # Kijkt of de entity buiten het scherm valt.
        if (self.Position.x > self._Game.Get_Screen().get_width() + 1000
            or self.Position.x < -2 * self.Size.x - 1000
            or self.Position.y > self._Game.Get_Screen().get_height() + 1000
            or self.Position.y < -2 * self.Size.y - 1000):
            self.Kill()
