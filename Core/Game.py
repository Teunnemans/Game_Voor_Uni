import time
from Core import Constants
from Core.AudioManager import Audio_Manager
from Core.Constants import *
from Core.Functions import ReadHighScoreFile
from Core.GameInfo import GameInfo
from Core.UI.UI_Manager import UI_Manager


# Een abstractielaag om de code in Main.py simpel te houden,
# centraliseert alle logica in 2 functies die steeds geroepen worden. Behoud ook de beschermde belangrijke variabelen
class Game:
    def __init__(self, Screen: pygame.Surface):

        # Deltatime setup
        self.Deltatime = self.Old_Time = time.perf_counter()

        # ScoreKeeping, slaat deze ook op in een Json bestand
        self.Attempts = ReadHighScoreFile()

        self._Screen = Screen #Scherm variabele

        # Alles met een _ ervoor beschouw ik een beetje als "sacred", wees voorzichtig met wat je daar aanpast
        self._State = Game_State.Main_Menu # DEZE VARIABLE BEPAALT IN WELKE STAAT HET SPEL ZICH BEVIND. ALLES PAST ZICH HIER OP AAN
        self._GameInfo = GameInfo(self) # Gameinfo object die zich elke ronde reset.
        self._UI_Manager = UI_Manager(self) # UI manager
        self._Audio_Manager = Audio_Manager()

        # Update ook meteen de state, zodat de ui manager de juiste ui kan tonen
        self.Set_State(self._State)


    # Deltatime update, update ook de pygame clock
    def Update_Deltatime(self):
        New_Time = time.perf_counter()
        # Verschil in tijd sinds laatste frame
        self.Deltatime = New_Time - self.Old_Time
        self.Old_Time = New_Time

    # Get-functies van de "beschermde" variabelen
    def Get_Screen(self): return self._Screen
    def Get_GameInfo(self): return self._GameInfo
    def Get_Ui_Manager(self): return self._UI_Manager
    def Get_State(self): return self._State
    def Get_Audio_Manager(self): return self._Audio_Manager

    # returned de juist achtergrond
    def Get_Background(self):
        # Op basis van de state, return een andere achtergrond
        match self._State:
            case Game_State.Main_Menu:
                return [Constants.Images.MainMenuBackGround, pygame.Vector2(0, 0)]
            case Game_State.In_Game:
                return self._GameInfo.Get_Background()

    # Set functie van de State variable
    def Set_State(self, New_State):
        # State updates
        self._State = New_State
        self._UI_Manager.Switch_State(New_State)
        # Music state Update
        if New_State == Constants.Game_State.In_Game:
            self._Audio_Manager.Play_Music("GameMusic.ogg", 0.6)
        elif New_State == Constants.Game_State.Main_Menu:
            self._Audio_Manager.Play_Music("MainMenuMusic.ogg", 0.6)
    def Start_Game(self):
        self.Set_State(Game_State.In_Game)
        self._GameInfo = GameInfo(self)
    # Reset functie, zorgt ervoor dat de gameinfo en ui_manager opnieuw gestart worden
    def Reset(self): self.Start_Game()

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
        Background = self.Get_Background()
        self._Screen.blit(Background[0],Background[1]) # Draw achtergrond, altijd size(500, 500) Haalt hij op uit een functie

        # State logica, ook te vinden in draw, zodat je selectief kan kiezen wat er zichtbaar is tijdens verschillende delen van het spel
        match self._State:
            case Game_State.Main_Menu: pass
            case Game_State.In_Game: self._GameInfo.Draw() # Alles wat de gameinfo moet tekenen tekent hij hier. Eigenlijk alle entities

        # Onafhankelijk van game_state aangezien de ui_manager dat zelf regelt.
        self._UI_Manager.Draw(self._Screen)  # UI Draw