# Dit is een python bestand met een eigengeschreven UI_Manager die allemaal ui elements onderhoud en verzamelt.
import pygame
from Core.Functions import Round_Vector
from Core.UI.UI_Element import UI_Group
from Core.UI.UI_Types import Image, Text_Element, Button
from Core.Constants import Game_State
from Core.Functions import Find_Center

class UI_Manager(UI_Group):
    def __init__(self, Game):
        super().__init__("", "UI_Manager", (0, 0))

        self.Elements = []
        self.Game = Game
        self.Standard_Font = pygame.font.SysFont("Arial", 20)

        self.Add_Element(Generate_Pause_Overlay(self)) # Genereert de pausedUIoverlay
        self.Add_Element(Generate_MainMenu(self)) # Genereert de mainmenu
        # Paar debug statements, Laat statistieken van de speler zien
        if self.Game.Debug: self.Add_Element(Generate_Debug_Overlay(self))

    # Update functie
    def Update(self, Eventstack):
        # De ui heeft toegang tot de pygame event queue. Hierdoor reageert de game op events.
        for Event in Eventstack:
            if Event.type == pygame.USEREVENT:
                if Event.dict["Type"] == "Button_Pressed":
                    if Event.dict["Name"] == "MainMenuButton": self.Game.Set_State(Game_State.Main_Menu)
                    if Event.dict["Name"] == "RestartButton": self.Game.Reset()
                    if Event.dict["Name"] == "PlayButton": self.Game.Start_Game()

        # Pauze menu alleen te zien in game
        if self.Game.Get_GameInfo().Paused and self.Game.Get_State() == Game_State.In_Game: self.Get_Element("Paused_Ui").Visible = True
        else: self.Get_Element("Paused_Ui").Visible = False
        # Debug statements updaten(Dit zou ook buiten de manager kunnen gebeuren dat is prima)
        if self.Game.Debug: Update_Debug_Overlay(self)

        # Daadwerkelijke update functie, update hoe dan ook heel de UI. Niet mega efficient, maar met weinig ui prima
        for Element in self.Elements: Element.Update(Eventstack)

    # Stateless UI, reageert dus alleen op de UI Updates
    def Switch_State(self, New_State):
        # State logica
        match New_State:
            case Game_State.Main_Menu:
                self.Get_Element("MainMenu_Ui").Visible = True
                # self.Get_Element("Game_UI").Visible = False
            case Game_State.In_Game:
                # self.Get_Element("Game_UI").Visible = True TODO MAAK DEZE
                self.Get_Element("MainMenu_Ui").Visible = False

# Functie voor het genereren van de UI van de pause_overlay
def Generate_Pause_Overlay(UIManager):
    PausedUi = UI_Group(UIManager, "Paused_Ui", (0, 0))
    # Oneliner voor het maken van de Pause overlay, laatste parameter is opacity
    PausedOverlay = pygame.Surface((500, 500), pygame.SRCALPHA)
    PausedOverlay.fill((0, 0, 0, 70))
    PausedUi.Add_Element(Image(PausedUi, "PausedBackground", PausedOverlay, (0, 0)))
    PausedUi.Add_Element(
        Text_Element(PausedUi, "PauseText", "Gepauzeerd", (200, 230), UIManager.Standard_Font, (255, 255, 255)))
    PausedUi.Add_Element(
        Button(UIManager, "MainMenuButton", pygame.Vector2(20, 102), pygame.transform.scale(pygame.image.load("Art/Player.png"), (130, 50)),
               "Terug naar menu", UIManager.Standard_Font, (255, 0, 0)))

    PausedUi.Add_Element(
        Button(UIManager, "RestartButton", pygame.Vector2(20, 50), pygame.transform.scale(pygame.image.load("Art/Player.png"), (130, 50)),
               "Herstart het spel", UIManager.Standard_Font, (255, 0, 0)))

    return PausedUi
# Main menu generatie
def Generate_MainMenu(UIManager):
    MainMenuUi = UI_Group(UIManager, "MainMenu_Ui", (0, 0))
    MainMenuUi.Add_Element(
        Button(UIManager, "PlayButton", Find_Center((130, 50), UIManager.Game.Get_Screen().get_size()) + pygame.Vector2(0, 50), pygame.transform.scale(pygame.image.load("Art/Player.png"), (130, 50)),
               "Spel starten", UIManager.Standard_Font, (255, 0, 0)))
    MainMenuUi.Add_Element(
        Button(UIManager, "QuitButton", Find_Center((130, 50), UIManager.Game.Get_Screen().get_size()) + pygame.Vector2(0, 102), pygame.transform.scale(pygame.image.load("Art/Player.png"), (130, 50)),
               "Spel stoppen", UIManager.Standard_Font, (255, 0, 0)))
    return MainMenuUi
# Functie voor het genereren van de UI van de Debug_Overlay
def Generate_Debug_Overlay(UIManager):
    DebugUi = UI_Group(UIManager, "Debug_Ui", (0, 0))

    DebugUi.Add_Element(Text_Element(DebugUi, "FPS", f"FPS ", (0, 10), UIManager.Standard_Font, (255, 0, 0)))
    DebugUi.Add_Element(Text_Element(DebugUi, "Time", f"Time: ", (0, 30), UIManager.Standard_Font, (255, 0, 0)))
    DebugUi.Add_Element(Text_Element(DebugUi, "Position", f"Position:", (0, 50), UIManager.Standard_Font, (255, 0, 0)))
    DebugUi.Add_Element(Text_Element(DebugUi, "Speed", f"Speed:", (0, 70), UIManager.Standard_Font, (255, 0, 0)))
    DebugUi.Add_Element(Text_Element(DebugUi, "Colliding", f"Colliding:", (0, 90), UIManager.Standard_Font, (255, 0, 0)))
    DebugUi.Add_Element(Text_Element(DebugUi, "Lives", f"Lives:", (0, 110), UIManager.Standard_Font, (255, 0, 0)))
    DebugUi.Add_Element(Text_Element(DebugUi, "Score", f"Score:", (0, 130), UIManager.Standard_Font, (255, 0, 0)))
    DebugUi.Add_Element(Text_Element(DebugUi, "Entitylist", f"Entitylist:", (0, 150), UIManager.Standard_Font, (255, 0, 0)))


    return DebugUi

def Update_Debug_Overlay(UiManager):
    DebugUi = UiManager.Get_Element("Debug_Ui")
    DebugUi.Get_Element("FPS").Text = f"FPS: {round(1 / UiManager.Game.Deltatime)}"
    DebugUi.Get_Element("Time").Text = f"Time: {round(UiManager.Game.Get_GameInfo().Time_Since_Game_Start, 2)}"
    DebugUi.Get_Element("Position").Text = f"Position: {Round_Vector(UiManager.Game.Get_GameInfo().Player.Position, 0)}"
    DebugUi.Get_Element("Speed").Text = f"Speed: {Round_Vector(UiManager.Game.Get_GameInfo().Player.Speed, 0)}"
    if len(UiManager.Game.Get_GameInfo().Player.CollidingList) > 0:
        DebugUi.Get_Element("Colliding").Text = f"Colliding: {UiManager.Game.Get_GameInfo().Player.CollidingList}"
    else:
        DebugUi.Get_Element("Colliding").Text = f"Colliding:"
    DebugUi.Get_Element("Lives").Text = f"Lives: {UiManager.Game.Get_GameInfo().Player.Lives}"
    DebugUi.Get_Element("Score").Text = f"Score: {round(UiManager.Game.Get_GameInfo().Score)}"
    DebugUi.Get_Element("Entitylist").Text = f"Entitylist: {len(UiManager.Game.Get_GameInfo().EntityList)}"
