import time

from Core import Constants
from Core.GameInfo import GameInfo
from Core.UI.UI_Manager import UI_Manager
from Core.Constants import *
# Een abstractielaag om de code in Main.py simpel te houden,
# centraliseert alle logica in 2 functies die steeds geroepen worden. Behoud ook de beschermde belangrijke variabelen
class Game:
    def __init__(self, Screen: pygame.Surface):
        self.Debug = True

        #Scherm variabele
        self._Screen = Screen

        # DEZE VARIABLE BEPAALT IN WELKE STAAT HET SPEL ZICH BEVIND. ALLES PAST ZICH HIER OP AAN
        self._State = Game_State.Main_Menu

        # Alles met een _ ervoor beschouw ik een beetje als "sacred", wees voorzichtig met wat je daar aanpast
        self._GameInfo = GameInfo(self)
        # UI manager
        self._UI_Manager = UI_Manager(self)

        # Deltatime setup
        self.Deltatime = self.Old_Time = time.perf_counter()
        self.Clock = pygame.time.Clock()

    # Deltatime update, update ook de pygame clock
    def Update_Deltatime(self):
        New_Time = time.perf_counter()
        # Verschil in tijd sinds laatste frame
        self.Deltatime = New_Time - self.Old_Time
        self.Old_Time = New_Time

        self.Clock.tick()

    # Get-functies van de "beschermde" variabelen
    def Get_Screen(self): return self._Screen
    def Get_GameInfo(self): return self._GameInfo
    def Get_Ui_Manager(self): return self._UI_Manager
    def Get_State(self): return self._State

    # returned de juist achtergrond
    def Get_Background(self):
        # Op basis van de state, return een andere achtergrond
        match self._State:
            case Game_State.Main_Menu:
                return Constants.Images.MainMenu
            case Game_State.In_Game:
                return self._GameInfo.Background
        # Default achtergrond
        return Constants.Images.MainMenu

    # Set functie van de State variable
    def Set_State(self, New_State):
        self._State = New_State
        self._UI_Manager.Switch_State(New_State)

    def Start_Game(self):
        self.Set_State(Game_State.In_Game)
        self._GameInfo = GameInfo(self)
    # Reset functie, zorgt ervoor dat de gameinfo en ui_manager opnieuw gestart worden
    def Reset(self):
        self.Set_State(Game_State.In_Game)
        self._GameInfo = GameInfo(self)

    # Alle logica voor het updaten van het spel
    def Update(self, Eventstack):
        # Update de deltatime
        self.Update_Deltatime()

        # State logica, ook te vinden in draw, zodat je selectief kan kiezen wat er zichtbaar is tijdens verschillende delen van het spel
        match self._State:
            case Game_State.Main_Menu: pass
            case Game_State.In_Game: self._GameInfo.Update(Eventstack) # GameInfo Update

        self._UI_Manager.Update(Eventstack) # UI Update, altijd apart van Paused
    # Alle logica voor het tekenen op het scherm.
    def Draw(self):

        self._Screen.fill((0, 0, 0)) # Screen reset.
        self._Screen.blit(self.Get_Background(), (0, 0)) # Draw achtergrond, altijd size(500, 500) Haalt hij op uit een functie

        # State logica, ook te vinden in draw, zodat je selectief kan kiezen wat er zichtbaar is tijdens verschillende delen van het spel
        match self._State:
            case Game_State.Main_Menu: pass
            case Game_State.In_Game: self._GameInfo.Draw() # Alles wat de gameinfo moet tekenen tekent hij hier. Eigenlijk alle entities

        # Onafhankelijk van game_state aangezien de ui_manager dat zelf regelt.
        self._UI_Manager.Draw(self._Screen)  # UI Draw