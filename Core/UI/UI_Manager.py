# Dit is een python bestand met een eigengeschreven UI_Manager die allemaal ui elements onderhoud en verzamelt.
import pygame
import time
from Core.Functions import Round_Vector
from Core.UI.UI_Element import UI_Group
from Core.UI.UI_Types import Image, Text_Element, Button


class UI_Manager(UI_Group):
    def __init__(self, Game):
        super().__init__("", "UI_Manager", (0, 0))

        self.Elements = []
        self._Game = Game
        self.Standard_Font = pygame.font.SysFont("Arial", 20)

        # Debug ui elements
        DebugUi = UI_Group(self, "Debug_Ui", (0, 0))
        self.Add_Element(DebugUi)
        # Paar debug statements, Laat statistieken van de speler zien
        if self._Game.Debug:
            DebugUi.Add_Element(Text_Element(DebugUi, "FPS", f"FPS ", (0, 10), self.Standard_Font, (255, 0, 0)))
            DebugUi.Add_Element(Text_Element(DebugUi, "Time", f"Time: ", (0, 30), self.Standard_Font, (255, 0, 0)))
            DebugUi.Add_Element(Text_Element(DebugUi, "Position", f"Position:", (0, 50), self.Standard_Font, (255, 0, 0)))
            DebugUi.Add_Element(Text_Element(DebugUi, "Speed", f"Speed:", (0, 70), self.Standard_Font, (255, 0, 0)))
            DebugUi.Add_Element(Text_Element(DebugUi, "Colliding", f"Colliding:", (0, 90), self.Standard_Font, (255, 0, 0)))
            DebugUi.Add_Element(Text_Element(DebugUi, "State", f"State:", (0, 110), self.Standard_Font, (255, 0, 0)))

        PausedUi = UI_Group(self, "Paused_Ui", (0, 0))
        self.Add_Element(PausedUi)
        # Oneliner voor het maken van de Pause overlay, laatste parameter is opacity
        PausedOverlay = pygame.Surface((500, 500), pygame.SRCALPHA); PausedOverlay.fill((0, 0, 0, 70))
        PausedUi.Add_Element(Image(PausedUi, "PausedBackground", PausedOverlay, (0, 0)))
        PausedUi.Add_Element(Text_Element(PausedUi, "PauseText", "Gepauzeerd", (200, 230), self.Standard_Font, (255, 255, 255)))
        PausedUi.Add_Element(Button(self, "Quit", (0,0), pygame.transform.scale(pygame.image.load("Art/Player.png"), (130, 50)), "Stop met spelen", self.Standard_Font, (255, 0, 0)))

    # Update functie
    def Update(self, Eventstack):
        # De ui heeft toegang tot de pygame event queue. Hierdoor reageert de game op events.
        for Event in Eventstack:
            if Event.type == pygame.USEREVENT:
                if Event.dict["Type"] == "Button_Pressed":
                    if Event.dict["Name"] == "Play":
                        self.Get_Element("Play").Visible = False

        # Debug statements updaten(Dit zou ook buiten de manager kunnen gebeuren dat is prima)
        if self._Game.Debug:
            DebugUi = self.Get_Element("Debug_Ui")
            DebugUi.Get_Element("FPS").Text = f"FPS: {round(1 / self._Game.Deltatime)}"
            DebugUi.Get_Element("Time").Text = f"Time: {round(time.perf_counter() - self._Game.Time_Since_Game_Start, 2)}"
            DebugUi.Get_Element("Position").Text = f"Position: {Round_Vector(self._Game.Player.Position, 0)}"
            DebugUi.Get_Element("Speed").Text = f"Speed: {Round_Vector(self._Game.Player.Speed, 0)}"
            if len(self._Game.Player.CollidingList) > 0:
                DebugUi.Get_Element("Colliding").Text = f"Colliding: {self._Game.Player.CollidingList}"
            else: DebugUi.Get_Element("Colliding").Text = f"Colliding:"
            DebugUi.Get_Element("State").Text = f"State: {self._Game.Get_State()}"

        # Pauze overlays
        if self._Game.Paused: self.Get_Element("Paused_Ui").Visible = True
        else: self.Get_Element("Paused_Ui").Visible = False

        # Daadwerkelijke update functie
        for Element in self.Elements: Element.Update(Eventstack)