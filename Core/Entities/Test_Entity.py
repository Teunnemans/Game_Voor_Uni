from Core.Entities.Entity import Entity
import pygame

from Core.Entities.Player import Player

# ENTITY OM TE KIJKEN HOE COLLISIONS ZOUDEN WERKEN
class TestEntity(Entity):
    def __init__(self, Game_Sprite: pygame.Surface, _Game, Position: pygame.Vector2 = pygame.Vector2(0, 0), Rotation: int = 0, Visible: bool = True):
        super().__init__(Game_Sprite, _Game, Position, Visible)
        self.Blink_Timer = 0

    def Handle_Collision(self, Other_Entity: Player):
        # Overlap berekenen
        Overlap = self.Rect.clip(Other_Entity.Rect)
        # Bepaal vanaf welke kant de collision het kleinst is
        if Overlap.width < Overlap.height:
            # Horizontale collision
            if Other_Entity.Rect.centerx < self.Rect.centerx:
                # Speler komt van links
                Other_Entity.Position.x -= Overlap.width
            else:
                # Speler komt van rechts
                Other_Entity.Position.x += Overlap.width

            # Horizontale snelheid stoppen
            Other_Entity.Speed.x = 0

        else:
            # Verticale collision
            if Other_Entity.Rect.centery < self.Rect.centery:
                # Speler komt van boven
                Other_Entity.Position.y -= Overlap.height
            else:
                # Speler komt van onder
                Other_Entity.Position.y += Overlap.height

            # Verticale snelheid stoppen
            Other_Entity.Speed.y = 0

    def Handle_Blinking(self, Eventstack):
        self.Visible = not self.Visible
        if self.Visible:
            self.Blink_Timer = 0
        else:
            self.Blink_Timer += self._Game.Deltatime
            if self.Blink_Timer > 0.5:
                self.Visible = True

    def Update(self, Eventstack):
        super().Update(Eventstack)
        self.Handle_Blinking(Eventstack)