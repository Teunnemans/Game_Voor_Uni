# Benodigde libraries voor de game. Inclusief eigen bestanden
import sys, pygame

from Core import Constants
from Core.Game import Game

# Maakt het scherm resizable. Default automatisch naar fullscreen
if Constants.Game_Settings.Start_Fullscreen: Flags = pygame.SCALED | pygame.FULLSCREEN
else: Flags = pygame.SCALED
Screen = pygame.display.set_mode(Constants.Game_Settings.Screen_Size, Flags)

#Initialisatie van de game! :)
_Game = Game(Screen)

# Core loop met exit conditie
while True:
    # Haalt eens per frame alle Events op
    Eventstack = pygame.event.get()
    for Event in Eventstack:
        # Quit bij wegklikken, ook bij backspace
        if Event.type == pygame.QUIT or (Event.type == pygame.KEYDOWN and Event.key == pygame.K_BACKSPACE) or (Event.type == pygame.USEREVENT and Event.dict["Type"] == "Button_Pressed" and Event.dict["Name"] == "QuitButton"):
            sys.exit(); pygame.quit()

    # Update ALLES, Tekent ALLES Geeft eventstack mee, omdat het roepen van die functie de queue cleart. Dat wil je niet.
    _Game.Update(Eventstack)
    _Game.Draw()
    # Volgende frame
    pygame.display.flip()