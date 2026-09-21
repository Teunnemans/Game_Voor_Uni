import time

# Een class met veel informatie over de gang van het spel.
class GameInfo:
    def __init__(self, Game):
        self._Game = Game # Verwijzing naar boven.

        # Een grote lijst met allemaal Entity-Class objecten. Kan hier iteratief alle Draw() en Update() functies uitvoeren
        # Speler staat hier NIET in, die staat een laag hoger, in Game, omdat er maar 1 speler is.
        self.EntityList = []

        # Deltatime setup
        self.Deltatime = self.Old_Time = time.perf_counter()

    # Deltatime update
    def Update_Deltatime(self):
        New_Time = time.perf_counter()
        # Verschil in tijd sinds laatste frame
        self.Deltatime = New_Time - self.Old_Time
        self.Old_Time = New_Time

    # Alle logica voor het updaten van het spel
    def Update(self):
        self.Update_Deltatime()
        # Update alle entities in het spel
        for Entity in self.EntityList:
            Entity.Update()
            Entity.Draw()
    # Alle logica voor het tekenen op het scherm.
    def Draw(self):
        # Teken alle entities in het spel.
        for Entity in self.EntityList:
            Entity.Draw()

        # Laat de fps van het spel zien.
        self._Game._Screen.blit(self._Game.Game_Font.render(f"FPS: {round(1/self.Deltatime)}", True, (255, 255, 255)), (0,0))
