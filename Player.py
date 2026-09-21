import pygame

from Entity import Entity
# Speler class, handlet input en is centraal voor het spel. Is er maar 1 van in het spel.
class Player(Entity):
    def __init__(self, Game_Sprite: pygame.Surface, _Game, X: int = 0 , Y: int = 0, Z: int = 0, Rotation: int = 0):
        super().__init__(Game_Sprite, _Game, X, Y, Z, Rotation)

        # Hoe snel beweegt de speler?
        self.Speed = 100
        # Nu nog ongebruikt
        self.Acceleration = 100

    def Update(self):
        super().Update()

        # Super Simpele Input die speler verplaatst.
        Keys = pygame.key.get_pressed()
        if Keys[pygame.K_UP]:
            self.Y -= self.Speed * self._Game._GameInfo.Deltatime
        if Keys[pygame.K_DOWN]:
            self.Y += self.Speed * self._Game._GameInfo.Deltatime
        if Keys[pygame.K_LEFT]:
            self.X -= self.Speed * self._Game._GameInfo.Deltatime
        if Keys[pygame.K_RIGHT]:
            self.X += self.Speed * self._Game._GameInfo.Deltatime

    def Draw(self):
        super().Draw()
        pass

