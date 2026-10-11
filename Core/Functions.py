import pygame
import random
from Core import Constants
import json


# Bestandje voor vaak gebruikte functies :) Hier staat echt van alles in, en er is niet echt een samenhang. Implementaties
# zouden duidelijk moeten zijn en overal in het programma terug te vinden

# Ik begrijp de python interpreter niet helemaal, die geeft mij de warning: Expected type 'float', got 'SupportsDunderLT[Any] | SupportsDunderGT[Any]' instead
# Dit levert geen foutmelding op. Hierom negeer ik het dus.

# Eigenlijk mijn eerdere clamp-functie, maar nu zonder Numpy, die steeds mijn types veranderde, Returned ALTIJD een pygame vector
def Clamp_Vector(vector, minimum, maximum):
    return pygame.Vector2(max(minimum.x, min(vector.x, maximum.x)), max(minimum.y, min(vector.y, maximum.y)))
# Rond de x en de y van een vector af. Gebruikt voor debug display redenen
def Round_Vector(vector, precision: int = 0):
    return pygame.Vector2(round(vector.x, precision), round(vector.y, precision))

# Vind het centrum van een surface TOV je eigen grootte. Hierna kan een offset toegepast worden in de x en de y richting. Hiermee kan je
# UI elements centreren
def Find_Center(Size_Self, Surface):
    return (pygame.Vector2(Surface) - pygame.Vector2(Size_Self)) / 2 # een nieuwe pygame vector

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
    StarAmount = 250 # Hoeveel sterren?
    for i in range(StarAmount):
        x = random.randint(3, 497)
        y = random.randint(3, 497)
        pygame.draw.circle(Background, (round(255 * random.uniform(0.8, 1)), 255, 255),
                       pygame.Vector2(x, y), random.randint(1, 2))

    # Easter eggs genereren, Heel weinig planeten
    for i in range(random.randint(1, 2)):
        x = random.randint(50, 450)
        y = random.randint(50, 450)
        RGB = (round(255*random.uniform(0.0, 1)), round(255*random.uniform(0.0, 1)), round(255*random.uniform(0.0, 1)))
        pygame.draw.circle(Background, RGB, pygame.Vector2(x, y), random.randint(3, 8))

    # Offset wordt geregeld zodra het spel genereerd. Zodat het bovenste gedeelte buiten het spel valt.
    return [Background, pygame.Vector2(0, 0)] # achtergrond, en de positie van de achtergrond

# Veranderd de fullscreen modus van het spel.
def ChangeFullscreen(Fullscreen):
    if Fullscreen: pygame.display.set_mode(Constants.Game_Settings.Screen_Size, pygame.FULLSCREEN | pygame.SCALED)
    else: pygame.display.set_mode(Constants.Game_Settings.Screen_Size, pygame.SCALED)

# SCOREBOARD functionaliteit, reading en writing met super simpele python functionaliteit

def ReadHighScoreFile():
    try:
        with open("Scores.json", "r") as file:
            print("Bestand gelezen!")
            return json.load(file)
    # Lege highscore file, invalide json return gewoon een lege array
    except FileNotFoundError :
        # Als het bestand nog niet bestaat maakt hij deze aan
        print("Bestand niet gevonden!")
        with open("Scores.json", "w") as file:
            json.dump([], file)
        return []
    except json.decoder.JSONDecodeError:
        print("Foute JSON!")
        return []
# Schrijft de highscore in een document
def WriteHighScoreFile(HighScoreList):
    with open("Scores.json", "w") as file:
        print("Bestand geschreven!")
        json.dump(HighScoreList, file)


# Schaalt een rect naar een nieuwe rect, deze functie gebruik ik om de hitboxes van de enemies iets kleiner te maken, en het
# spel hierdoor wat leuker te maken.
def Scale_Rect_From_Center(rect, Scaling):
    Center = rect.center
    New_rect = pygame.Rect(0, 0, rect.width * Scaling, rect.height * Scaling)
    New_rect.center = Center
    return New_rect