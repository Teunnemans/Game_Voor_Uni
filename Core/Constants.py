import pygame
from enum import Enum
# Bestand met voorgeladen constante waardes. Die iedere deel van het programma kan gebruiken


class Images:
    Player = pygame.transform.scale(pygame.image.load("Art/Player.png"), (50, 50))
    Background =  pygame.transform.scale(pygame.image.load("Art/Background.jpg"), (500, 500))
    MainMenu = pygame.transform.scale(pygame.image.load("Art/MainMenu.jpg"), (500, 500))

class Game_State(Enum):
    Main_Menu = 0
    In_Game = 1

class EnemyTypes(Enum):
    Standard = 0
    PowerUp = 1
    Enemy = 2