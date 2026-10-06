# Een wrapper voor entity, met wat toegevoegde functionaliteit
import pygame
from Core import Constants
from Core.Entities.Entity import Entity


class EnemyBase(Entity):
    def __init__(self, Sprite, Game, Position, Visible: bool = True):
        super().__init__(Sprite, Game, Position, Visible)

        # Lijkt veel op de Player Class, Movement die je KAN gebruiken voor de Enemy Gedrag verder aan te vullen

        # Hoe snel beweegt de Enemy?
        self.MaxSpeed = None # Moet altijd een pygame vector zijn
        self.Speed = pygame.Vector2(0, 0)
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

        # Kijkt of de entity buiten het scherm valt. Zo ja, verwijder deze uit de entitylijst.
        if ((self.Position.x > pygame.Vector2(self._Game.Get_Screen().get_size()).x or self.Position.x < 0-self.Size.x) or
            (self.Position.y > pygame.Vector2(self._Game.Get_Screen().get_size()).y or self.Position.y < 0-self.Size.y)):
            self.Kill()

# Even kijken of mijn functionaliteiten werken
class TestEnemy(EnemyBase):
    def __init__(self, Sprite, Game, Position, Visible: bool = True):
        super().__init__(Sprite, Game, Position, Visible)
        self.Speed.y = 250
        self.Type = Constants.EnemyTypes.Enemy

# POWERUPS
class ClearingBomb(EnemyBase):
    def __init__(self, Sprite, Game, Position, Visible: bool = True):
        super().__init__(Sprite, Game, Position, Visible)
        self.Type = Constants.EnemyTypes.PowerUp

    def Handle_Collision(self, Other_Entity):
        for Entity in self._Game.Get_GameInfo().EntityList:
            # Cleart elke entity behalve de powerups
            if Entity.type is not Constants.EnemyTypes.PowerUp:
                Entity.Kill()
# 1 extra leven :)
class Heart(EnemyBase):
    def __init__(self, Sprite, Game, Position, Visible: bool = True):
        super().__init__(Sprite, Game, Position, Visible)
        self.Type = Constants.EnemyTypes.PowerUp

    def Handle_Collision(self, Other_Entity):
        Other_Entity.Lives += 1
# 1 minder leven :( Lijkt op een powerup, maar is dit niet.
class HurtingBomb(EnemyBase):
    def __init__(self, Sprite, Game, Position, Visible: bool = True):
        super().__init__(Sprite, Game, Position, Visible)
        self.Type = Constants.EnemyTypes.PowerUp
# ENEMIES