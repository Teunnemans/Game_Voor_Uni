import pygame, uuid
# Coole entity class die een basis vormt voor objecten in het spel. Bevat veel informatie
# Die gebruikt kan worden bij andere classes waar hij op doorbouwt.
class Entity:
    def __init__(self, Game_Sprite: pygame.Surface, _Game, Position: pygame.Vector2 = pygame.Vector2(0, 0), Rotation: int = 0, Visible: bool = True):
        # Een reference naar de Globale _Game variable. Niets in aanpassen,
        # maar kan wel informatie opvragen en functies uitvoeren
        self._Game = _Game

        # Een unieke code Specifiek tot DIE entity, gebruikt voor identificatie.
        self.ID = uuid.uuid4()

        # "Plaatje" van de entity, TODO Vervangen voor een animatiesysteem (OBV states die de speler aan kan nemen)
        self.Sprite = Game_Sprite
        # "Positie" van de entity
        self.Position = Position
        # Functie voor de collision van de Entity, een rect is een vierkant.
        self.Size = pygame.Vector2(Game_Sprite.get_size())
        self.Rect = pygame.Rect(self.Position, self.Size)
        # Draaiing in graden TODO Draaing inplementeren
        self.Rotation = Rotation

        self.Visible = Visible

    # Lege collision functie die aangeroepen wordt als de speler tegen de collider aanloopt. Als deze niet aangevult wordt
    # door een andere class dan is hij niet collidable
    def Handle_Collision(self, Other_Entity):
        pass

    # Zelf in te vullen, wil je dat een entity iets anders doet/ander gedrag heeft? Dan kan dat. roep wel eerst super.update() aan
    # Dit is in ieder geval standaard gedrag.
    def Update(self, Eventstack):
        # Nieuwe Rect
        self.Rect = pygame.Rect(self.Position, self.Size)
    # Ook zelf in te vullen, misschien wil je wel helemaal niet dat de entity getekend wordt, kan ook.
    # Dit is standaard gedrag.
    def Draw(self):
        if self.Visible:
            self._Game.Get_Screen().blit(self.Sprite, self.Position)
