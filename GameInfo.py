import time
from Functions import Round_Vector


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
        self._Game.Get_Screen().blit(self._Game.Font.render(f"FPS: {round(1/self.Deltatime)}", True, (255, 0, 0)), (0,0))
        # Laat wat statistieken van de speler zien. Lang lijntje code maar is toch debug
        self._Game.Get_Screen().blit(self._Game.Font.render(f"Position: {Round_Vector(self._Game.Player.Position, 0)}", True, (255, 0, 0)), (0,50))
        self._Game.Get_Screen().blit(self._Game.Font.render(f"Speed: {Round_Vector(self._Game.Player.Speed, 0)}", True, (255, 0, 0)), (0,100))