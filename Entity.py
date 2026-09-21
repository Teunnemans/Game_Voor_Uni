import pygame, uuid
# Coole entity class die een basis vormt voor objecten in het spel. Bevat veel informatie
# Die gebruikt kan worden bij andere classes waar hij op doorbouwt.
class Entity:
    def __init__(self, Game_Sprite: pygame.Surface, _Game, X: int = 0 , Y: int = 0, Z: int = 0, Rotation: int = 0):
        # Een reference naar de Globale _Game variable. Niets in aanpassen,
        # maar kan wel informatie opvragen en functies uitvoeren
        self._Game = _Game

        # Een unieke code Specifiek tot DIE entity, gebruikt voor identificatie.
        self.ID = uuid.uuid4()

        # "Plaatje" van de entity
        self.Sprite = Game_Sprite
        # "Positie" van de entity
        self.X = X
        self.Y = Y
        # Optioneel mocht ik ooit diepte toevoegen
        self.Z = Z
        # Functie voor de collision van de Entity, een rect is een vierkant.
        self.Width, self.Height = Game_Sprite.get_rect().size
        self.Rect = pygame.Rect(self.X, self.Y, self.Width, self.Height)
        # Draaiing in graden
        self.Rotation = Rotation

    # Zelf in te vullen, wil je dat een entity iets anders doet/ander gedrag heeft? Dan kan dat.
    # Dit is in ieder geval standaard gedrag.
    def Update(self):
        # Nieuwe Rect
        self.Rect = pygame.Rect(self.X, self.Y, self.Width, self.Height)
    # Ook zelf in te vullen, misschien wil je wel helemaal niet dat de entity getekend wordt, kan ook.
    # Dit is standaard gedrag.
    def Draw(self):
        self._Game._Screen.blit(self.Sprite, (self.X, self.Y))
