import pygame, uuid
from Game import Game


class Entity:
    def __init__(self, Game_Sprite: pygame.Surface, _Game: Game, X: int = 0 , Y: int = 0, Z: int = 0) -> None:
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

    # Zelf in te vullen, wil je dat een entity iets anders doet/ander gedrag heeft? Dan kan dat.
    def Update(self):
        pass
    # Ook zelf in te vullen, misschien wil je wel helemaal niet dat de entity getekend wordt, kan ook.
    def Draw(self):
        pass