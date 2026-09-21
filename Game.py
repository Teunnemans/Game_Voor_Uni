import pygame
from GameInfo import GameInfo
from Player import Player


# Een abstractielaag om de code in Main.py simpel te houden,
# centraliseert alle logica in 2 functies die steeds geroepen worden.
class Game:
    def __init__(self, Screen: pygame.Surface):
        # Alles met een _ ervoor beschouw ik een beetje als "sacred", wees voorzichtig met wat je daar aanpast
        self._GameInfo = GameInfo(self)
        self._Screen = Screen
        self.Player = Player(pygame.image.load("Art/Player.png"), self, 250, 250)
        self.Game_Font = pygame.font.SysFont("Arial", 20)

    # Alle logica voor het updaten van het spel
    def Update(self):
        self._GameInfo.Update()
        # Player Update
        self.Player.Update()
    # Alle logica voor het tekenen op het scherm.
    def Draw(self):
        #Player Draw Update
        self.Player.Draw()
        #Alles wat de gameinfo moet tekenen tekent hij hier.
        self._GameInfo.Draw()
