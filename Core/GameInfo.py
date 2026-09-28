# Een class met veel informatie over de gang van het spel.

class GameInfo:
    def __init__(self, Game):
        self._Game = Game # Verwijzing naar boven.

        # Core properties
        self.Friction = 7

        # Een grote lijst met allemaal Entity-Class objecten. Kan hier iteratief alle Draw() en Update() functies uitvoeren
        # Speler staat hier NIET in, die staat een laag hoger, in Game, omdat er maar 1 speler is.
        self.EntityList = []
        # Basis voor score hier.
        self.Score = 0

    # Alle logica voor het updaten van het spel
    def Update(self, Eventstack):
        # Update alle entities in het spel
        for Entity in self.EntityList:
            Entity.Update(Eventstack)
    # Alle logica voor het tekenen op het scherm.
    def Draw(self):
        # Teken alle entities in het spel.
        for Entity in self.EntityList:
            Entity.Draw()