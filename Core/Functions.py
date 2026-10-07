import pygame
import random
from Core import Constants


# Bestandje voor vaak gebruikte functies :)

# Ik begrijp de python intreperter niet helemaal, die geeft mij de warning: Expected type 'float', got 'SupportsDunderLT[Any] | SupportsDunderGT[Any]' instead
# Dit levert geen foutmelding op. Hierom negeer ik het dus.

# Eigenlijk mijn eerdere clamp-functie, maar nu zonder Numpy, die steeds mijn types veranderde Returned ALTIJD een pygame vector
def Clamp_Vector(vector, minimum, maximum) -> pygame.Vector2:
    return pygame.Vector2( max(minimum.x, min(vector.x, maximum.x)), max(minimum.y, min(vector.y, maximum.y)))

def Round_Vector(vector, precision: int = 0) -> pygame.Vector2:
    return pygame.Vector2(round(vector.x, precision), round(vector.y, precision))

# Vind het centrum van een surface TOV je eigen grootte. Hierna kan een offset toegepast worden in de x en de y richting
def Find_Center(Size_Self, Surface):
    return (pygame.Vector2(Surface) - pygame.Vector2(Size_Self)) / 2

# Kiest willekeurig 1 van de zijden van het scherm uit voor het spawnen van nieuwe enemies, gaat steeds uit van 50 pixels breed en groot
def Random_Outside_Position_And_Direction(Diagonal):
    Side = random.randint(0, 3)

    # Punt op het scherm zodat hij altijd de juiste richting neemt
    Target = pygame.Vector2(random.randint(0, 500), random.randint(0, 500))

    match Side:
        case 0:  Position = pygame.Vector2(random.randrange(0, 501), -50) # boven
        case 1: Position = pygame.Vector2(random.randrange(0, 501), 550) # onder
        case 2: Position = pygame.Vector2(-50, random.randrange(0, 501)) # links
        case 3: Position = pygame.Vector2(550, random.randrange(0, 501)) # rechts

    # richtingsvector
    Direction = Target - Position
    # Eenheidsvector van de richtingsvector
    Direction.normalize_ip()

    # Richting beklemmen zodat hij niet gekke hoeken maakt
    Direction.x = max(-1, min(1, round(Direction.x)))
    Direction.y = max(-1, min(1, round(Direction.y)))

    return Position, Direction


# Genereert 1 achtergrond! surface en een positie die bestaat uit een 10x10 grid aan surfaces die allemaal willekeurige vierkanten met "sterren erin"
def Generate_Background():
    Background = pygame.Surface(pygame.Vector2(500, 500))
    Background.fill((0, 0, 0))

    # OUDE VERSIE
    #for i in range(10):
      #  for j in range(10):
       #     Tile = pygame.Surface(pygame.Vector2(50, 50))
        #    Tile.fill((0, 0, 0))
         #   # Genereer random sterren
          #  for x in range(random.randrange(3, 12)):
           #     pygame.draw.circle(Tile, (round(255* random.uniform(0.8, 1)), 255, 255), pygame.Vector2(random.randint(2,48), random.randint(2, 48)), random.randint(0,2))
           # Background.blit(Tile, (i*50, j*50))

    # NIEUWE VERSIE, zou veel efficienter moeten zijn UPDATE: Yess is ook zo, ik laat even de oude functie staan, om te laten zien
    # Wat ik daarvoor bedacht had.

    # Sterren genereren
    StarAmount = 500
    for i in range(StarAmount):
        x = random.randint(3, 497)
        y = random.randint(3, 497)
        pygame.draw.circle(Background, (round(255 * random.uniform(0.8, 1)), 255, 255),
                       pygame.Vector2(x, y), random.randint(1, 2))

    # Easter eggs genereren
    for i in range(random.randint(1, 2)):
        x = random.randint(50, 450)
        y = random.randint(50, 450)
        RGB = (round(255*random.uniform(0.0, 1)), round(255*random.uniform(0.0, 1)), round(255*random.uniform(0.0, 1)))
        pygame.draw.circle(Background, RGB, pygame.Vector2(x, y), random.randint(3, 8))

    # Offset wordt geregeld zodra het spel genereerd. Zodat het bovenste gedeelte buiten het spel valt.
    return [Background, (0, 0)]
# Veranderd de fullscreen modus van het spel.
def ChangeFullscreen(Fullscreen):
    if Fullscreen: pygame.display.set_mode(Constants.Game_Settings.Screen_Size, pygame.FULLSCREEN | pygame.SCALED)
    else: pygame.display.set_mode(Constants.Game_Settings.Screen_Size, pygame.SCALED)
