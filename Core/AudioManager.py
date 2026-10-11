import pygame

# Een manager voor al het geluid in het spel, laad bestanden uit ART/SFX

class Audio_Manager:
    def __init__(self):

        self.Sounds = {}
        self.Load_Sound("Button_Click", "Button_Click.ogg", 0.1)
        self.Load_Sound("Health", "Health.ogg", 0.3)
        self.Load_Sound("Hit", "Hit.ogg", 0.3)
        self.Load_Sound("Death", "Death.ogg", 0.3)
        self.Load_Sound("Clearing_Bomb", "Clearing_Bomb.ogg", 0.2)

    # Laad en speelt de muziek af
    def Play_Music(self, Filename, Volume=1):
        pygame.mixer.music.load(f"Art/SFX/{Filename}")
        pygame.mixer.music.set_volume(Volume)
        pygame.mixer.music.play(-1)  # -1 = oneindig herhalen, zodat je niet steeds de muziek opnieuw moet oproepen

    # Voorladen van alle geluidsbestanden
    def Load_Sound(self, Name, Filename, Volume=1):
        Sound = pygame.mixer.Sound(f"Art/SFX/{Filename}")
        Sound.set_volume(Volume)
        self.Sounds[Name] = Sound

    # Speelt geluidseffecten af
    def Play_Sound(self, Name):
        if Name in self.Sounds:
            self.Sounds[Name].play()
    # Pause en unpause functionaliteit
    def Pause_Music(self):
        pygame.mixer.music.pause()

    def Resume_Music(self):
        pygame.mixer.music.unpause()