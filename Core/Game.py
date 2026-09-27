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

        # Alles met een _ ervoor beschouw ik een beetje als "sacred", wees voorzichtig met wat je daar aanpast
        self._GameInfo = GameInfo(self)
        # UI manager
        self._UI_Manager = UI_Manager(self)

        #Scherm variabele
        self._Screen = Screen
        # Staat de game op pauze? Kan om veel redenen. Ui past zich hierop aan, en en de updates worden ook op pauze gezet
        self.Paused = False

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
    def Get_Screen(self):
        return self._Screen
    def Get_GameInfo(self):
        return self._GameInfo

    # Alle logica voor het updaten van het spel
    def Update(self):
        # Update de deltatime
        self.Update_Deltatime()
        # Pauze logica, gaat op pauze zolang je esc of p ingedrukt houdt
        Keys = pygame.key.get_pressed()
        if Keys[pygame.K_ESCAPE] or Keys[pygame.K_p]: self.Paused = True
        else: self.Paused = False

        # Spel speelt normaal, anders spel op pauze
        if not self.Paused:
            self._GameInfo.Update()
            # Player Update
            self.Player.Update()

        # UI Update, altijd apart van Paused
        self._UI_Manager.Update()
    # Alle logica voor het tekenen op het scherm.
    def Draw(self):
        # Screen reset.
        self._Screen.blit(self.Background, (0, 0))
        #Player Draw Update
        self.Player.Draw()
        #Alles wat de gameinfo moet tekenen tekent hij hier.
        self._GameInfo.Draw()
        # UI Draw
        self._UI_Manager.Draw()
