# Benodigde libraries voor de game. Inclusief eigen bestanden
import sys, pygame, time
from Game import Game

#Initialisatie van de verschillende programma's, oa schermgrootte
pygame.init()
pygame.font.init()
pygame.display.set_caption("Racegame! :)")
Screen = pygame.display.set_mode((500, 500))
#Initialisatie van de game! :)
_Game = Game(Screen)

# Game loop met exit conditie
while True:
    for Event in pygame.event.get():
        if Event.type == pygame.QUIT:
            sys.exit()
    # Update ALLES
    _Game.Update()
    # Teken ALLES
    _Game.Draw()
    # Reset het scherm
    pygame.display.flip()