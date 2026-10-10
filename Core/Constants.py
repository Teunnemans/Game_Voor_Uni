import pygame
from enum import Enum


# Game init
pygame.init()
pygame.font.init()
pygame.display.set_caption("Space Racer! :)")


class Images:

    # Clearing Bomb sprite
    Clearing_Bomb_Sprite = pygame.transform.scale(pygame.image.load("Art/Enemy_Sprites/Clearing-Bomb.png"), (50, 50))
    Heart_PowerUp = pygame.transform.scale(pygame.image.load("Art/Enemy_Sprites/Heart-Powerup.png"), (50, 50))
    # Moving enemy sprite
    Moving_Enemy = pygame.transform.scale(pygame.image.load("Art/Enemy_Sprites/player.png"),(50, 50))
    # Oscilating enemy sprite
    Oscillating_Enemy = pygame.transform.scale(pygame.image.load("Art/Enemy_Sprites/Oscilating-Enemy.png"), (50, 50))
    Tailgater_Enemy = pygame.transform.scale(pygame.image.load("Art/Enemy_Sprites/Tailgater-Enemy.png"), (50, 50))
    Parallel_Enemy = {
        "UP": pygame.transform.rotate(Moving_Enemy, -90),
        "DOWN": pygame.transform.rotate(Moving_Enemy, 90),
        "LEFT": pygame.transform.rotate(Moving_Enemy, 180),
        "RIGHT": pygame.transform.rotate(Moving_Enemy, 0),
        "LEFT-UP": pygame.transform.rotate(Moving_Enemy, 225),
        "LEFT-DOWN": pygame.transform.rotate(Moving_Enemy, 135),
        "RIGHT-UP": pygame.transform.rotate(Moving_Enemy, -45),
        "RIGHT-DOWN": pygame.transform.rotate(Moving_Enemy, 45),
    }

    MainMenuBackGround = pygame.image.load("Art/Main-Menu-Image.png")
    Hartje = pygame.image.load("Art/Hartje.png")
    Player_Image = pygame.transform.scale(pygame.image.load("Art/Player-Rocket.png"), (50, 50))
    Home = pygame.image.load("Art/Home.png")
    Restart = pygame.image.load("Art/Restart.png")
class Game_State(Enum):
    Main_Menu = 0
    In_Game = 1
class EnemyTypes(Enum):
    Standard = 0
    PowerUp = 1
    Enemy = 2

class Game_Settings:
    Start_Fullscreen = True
    Screen_Size = (500, 500)
    Debug = False
    Standard_Font = pygame.font.SysFont("Arial", 20)

