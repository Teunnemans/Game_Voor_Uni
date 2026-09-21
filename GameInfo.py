import time

class GameInfo:
    def __init__(self):
        # Een grote lijst met allemaal Entity-Class objecten. Kan hier iteratief alle Draw() en Update() functies uitvoeren
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
    # Alle logica voor het tekenen op het scherm.
    def Draw(self):
        # Teken alle entities in het spel.
        for Entity in self.EntityList:
            Entity.Draw()
