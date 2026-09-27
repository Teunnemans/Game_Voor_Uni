# Dit is een python bestand met een eigengeschreven UI_Manager die allemaal ui elements onderhoud en verzamelt.
import pygame
import time
from Core.Functions import Round_Vector
from Core.UI.UI_Types import Image, Text_Element

class UI_Manager:
    def __init__(self, Game):
        self.Elements = []
        self._Game = Game
        self.Standard_Font = pygame.font.SysFont("Arial", 20)
        # Paar debug statements, Laat statistieken van de speler zien
        if self._Game.Debug:
            self.Add_Element(Text_Element("FPS", f"FPS ", (0, 10), self.Standard_Font, (255, 0, 0)))
            self.Add_Element(Text_Element("Time", f"Time: ", (0, 30), self.Standard_Font, (255, 0, 0)))
            self.Add_Element(Text_Element("Position", f"Position:", (0, 50), self.Standard_Font, (255, 0, 0)))
            self.Add_Element(Text_Element("Speed", f"Speed:", (0, 70), self.Standard_Font, (255, 0, 0)))
            self.Add_Element(Text_Element("Paused", f"Paused:", (0, 90), self.Standard_Font, (255, 0, 0)))

        # Oneliner voor het maken van de Pause overlay, laatste parameter is opacity
        PausedOverlay = pygame.Surface((500, 500), pygame.SRCALPHA); PausedOverlay.fill((0, 0, 0, 70))
        self.Add_Element(Image("Paused-Overlay", PausedOverlay, (0, 0), Visible=False))
        self.Add_Element(Text_Element("Pause-Text", "Gepauzeerd", (200, 230), self.Standard_Font, (255, 255, 255), Visible=False))

    def Add_Element(self, Element):
        self.Elements.append(Element)

    def Remove_Element(self, ID):
        for Element in self.Elements:
            if Element.Name == ID:
                self.Elements.remove(Element)

    def Get_Element(self, ID):
        for Element in self.Elements:
            if Element.Name == ID:
                return Element
        return None

    # Teken functie
    def Draw(self):
        # Tekent alleen als de Element zichtbaar is.
        for Element in self.Elements:
            if Element.Visible:
                Element.Draw(self._Game.Get_Screen())

    # Update functie
    def Update(self):
        # Debug statements updaten(Dit zou ook buiten de manager kunnen gebeuren dat is prima)
        if self._Game.Debug:
            self.Get_Element("FPS").Text = f"FPS: {round(1 / self._Game.Deltatime)}"
            self.Get_Element("Time").Text = f"Time: {round(time.perf_counter() - self._Game.Time_Since_Game_Start, 2)}"
            self.Get_Element("Position").Text = f"Position: {Round_Vector(self._Game.Player.Position, 0)}"
            self.Get_Element("Speed").Text = f"Speed: {Round_Vector(self._Game.Player.Speed, 0)}"
            self.Get_Element("Paused").Text = f"Paused: {self._Game.Paused}"

        # Pauze overlays
        if self._Game.Paused:
            self.Get_Element("Paused-Overlay").Visible = True
            self.Get_Element("Pause-Text").Visible = True
        else:
            self.Get_Element("Paused-Overlay").Visible = False
            self.Get_Element("Pause-Text").Visible = False

        # Daadwerkelijke update functie
        for Element in self.Elements:
            if Element.Visible:
                Element.Update()