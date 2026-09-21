# Benodigde libraries voor de game.
import sys, pygame

#Initialisatie van de verschillende programma's, oa schermgrootte
pygame.init()
size = width, height = 500, 500
screen = pygame.display.set_mode(size)

# Game loop met exit conditie
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill((0, 0, 0))
    pygame.display.flip()