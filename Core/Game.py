import pygame
import time
from Core.GameInfo import GameInfo
from Core.Entities.Player import Player
from Core.UI.UI_Manager import UI_Manager

# Een abstractielaag om de code in Main.py simpel te houden,
# centraliseert alle logica in 2 functies die steeds geroepen worden. Behoud ook de beschermde belangrijke variabelen
class Game:
    def __init__(self, Screen: pygame.Surface):
        self.Debug = True

        # DEZE VARIABLE BEPAALT IN WELKE STAAT HET SPEL ZICH BEVIND. ALLES PAST ZICH HIER OP AAN
        self._State = "In_Game"

        # Alles met een _ ervoor beschouw ik een beetje als "sacred", wees voorzichtig met wat je daar aanpast
        self._GameInfo = GameInfo(self)
        # UI manager
        self._UI_Manager = UI_Manager(self)

        #Scherm variabele
        self._Screen = Screen
        # Staat de game op pauze? Kan om veel redenen. Ui past zich hierop aan, en en de updates worden ook op pauze gezet
        self.Paused = False
        self.ShouldToggle = True

        # Deltatime setup
        self.Deltatime = self.Old_Time = time.perf_counter()
        # Tijd sinds Game_Start
        self.Time_Since_Game_Start = time.perf_counter()

        # Achtergrond van het spel. TODO maak deze dynamisch
        self.Background = pygame.transform.scale(pygame.image.load("Art/Background.jpg"), self._Screen.get_size())
        # Speler van het spel, aparte class die boven alle andere logica staat
        self.Player = Player(self, pygame.Vector2(50, 50))

    # Deltatime update
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

    # Set functie van de State variable
    def Set_State(self, New_State): self._State = New_State

    # Alle logica voor het updaten van het spel
    def Update(self, Eventstack):
        # Update de deltatime
        self.Update_Deltatime()

        # Pauze logica, gaat op pauze zodra je esc of p indrukt. Is een toggle
        Keys = pygame.key.get_pressed()
        if Keys[pygame.K_ESCAPE] or Keys[pygame.K_p]:
            if self.ShouldToggle:
                self.ShouldToggle = False
                self.Paused = not self.Paused # Toggle
        else: self.ShouldToggle = True

        # Spel speelt normaal, anders spel op pauze
        if not self.Paused:
            self._GameInfo.Update(Eventstack) # GameInfo Update
            self.Player.Update(Eventstack) # Player Update

        self._UI_Manager.Update(Eventstack) # UI Update, altijd apart van Paused
    # Alle logica voor het tekenen op het scherm.
    def Draw(self):
        self._Screen.blit(self.Background, (0, 0)) # Screen reset.

        self.Player.Draw() #Player Draw Update

        self._GameInfo.Draw() #Alles wat de gameinfo moet tekenen tekent hij hier.

        self._UI_Manager.Draw(self._Screen) # UI Draw
