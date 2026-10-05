import pygame

# Bestand met voorgeladen constante waardes. Die iedere deel van het programma kan gebruiken


class Images:
    Player = pygame.image.load("Art/Player.png")
    Background =  pygame.transform.scale(pygame.image.load("Art/Background.jpg"), (500, 500))
    MainMenu = pygame.transform.scale(pygame.image.load("Art/MainMenu.jpg"), (500, 500))

class Game_State(enumerate):
    Main_Menu = 0
    In_Game = 1

# Vind het centrum van een surface TOV je eigen grootte. Hierna kan een offset toegepast worden in de x en de y richting
def Find_Center(Size_Self, Surface):
    return (Surface[0] / 2) - (Size_Self[0] / 2), (Surface[1] / 2) - (Size_Self[1] / 2)