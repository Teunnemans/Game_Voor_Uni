import pygame
from GameInfo import GameInfo

class Game:
    def __init__(self, Screen: pygame.Surface):
        # Alles met een _ ervoor beschouw ik een beetje als "sacred", wees voorzichtig met wat je daar aanpast
        self._GameInfo = GameInfo()
        self._Screen = Screen

    # Alle logica voor het updaten van het spel
    def Update(self):
        self._GameInfo.Update()
    # Alle logica voor het tekenen op het scherm.
    def Draw(self):
        # Reset het scherm
        self._Screen.fill((0, 0, 255))