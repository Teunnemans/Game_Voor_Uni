import pygame
from GameInfo import GameInfo
from Player import Player


# Een abstractielaag om de code in Main.py simpel te houden,
# centraliseert alle logica in 2 functies die steeds geroepen worden. Behoud ook de beschermde belangrijke variabelen
class Game:
    def __init__(self, Screen: pygame.Surface):
        # Alles met een _ ervoor beschouw ik een beetje als "sacred", wees voorzichtig met wat je daar aanpast
        self._GameInfo = GameInfo(self)
        #Scherm variabele
        self._Screen = Screen
        # Achtergrond van het spel. TODO maak deze dynamisch
        self.Background = pygame.transform.scale(pygame.image.load("Art/Background.jpg"), (self._Screen.get_width(), self._Screen.get_height()))
        # Lettertype voorgeladen om het spel soepeler te maken.
        self.Font = pygame.font.SysFont("Arial", 20)
        # Speler van het spel, aparte class die boven alle andere logica staat
        self.Player = Player(self, 250, 250)

    # Get-functies van de "beschermde" variabelen
    def Get_Screen(self):
        return self._Screen
    def Get_GameInfo(self):
        return self._GameInfo


    # Alle logica voor het updaten van het spel
    def Update(self):
        self._GameInfo.Update()
        # Player Update
        self.Player.Update()
    # Alle logica voor het tekenen op het scherm.
    def Draw(self):
        # Screen reset.
        self._Screen.blit(self.Background, (0, 0))

        #Player Draw Update
        self.Player.Draw()
        #Alles wat de gameinfo moet tekenen tekent hij hier.
        self._GameInfo.Draw()
