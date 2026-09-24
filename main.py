# Benodigde libraries voor de game. Inclusief eigen bestanden
import sys, pygame
from Game import Game
#Initialisatie van de verschillende programma's, oa schermgrootte,
# beetje illegale python maar 1 lijn code vind ik netter dan 3
pygame.init(); pygame.font.init(); pygame.display.set_caption("Racegame! :)")
# Maakt het scherm resizable. TODO KIjken naar hoe efficient dit is?
Screen = pygame.display.set_mode((500, 500), pygame.SCALED | pygame.FULLSCREEN)
# Niet fullscreen init van de game
#Screen = pygame.display.set_mode((500, 500))
#Initialisatie van de game! :)
_Game = Game(Screen)

# Game loop met exit conditie
while True:
    for Event in pygame.event.get():
        # Quit bij wegklikken
        if Event.type == pygame.QUIT:
            sys.exit()
        # Quit ook bij escape
        elif Event.type == pygame.KEYDOWN:
            if Event.key == pygame.K_ESCAPE:
                sys.exit()
    # Update ALLES, Tekent ALLES
    _Game.Update()
    _Game.Draw()
    # Volgende frame
    pygame.display.flip()