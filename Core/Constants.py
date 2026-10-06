import pygame

# Bestand met voorgeladen constante waardes. Die iedere deel van het programma kan gebruiken


class Images:
    Player = pygame.transform.scale(pygame.image.load("Art/Player.png"), (50, 50))
    Background =  pygame.transform.scale(pygame.image.load("Art/Background.jpg"), (500, 500))
    MainMenu = pygame.transform.scale(pygame.image.load("Art/MainMenu.jpg"), (500, 500))

class Game_State(enumerate):
    Main_Menu = 0
    In_Game = 1
