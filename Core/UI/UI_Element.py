import pygame

# Basis klasse voor alle UI elementen
class UI_Element:
    def __init__(self, Name, Sprite, Position, Visible = True):

        # Deze moet altijd ingevuld worden door de Class die deze inherit. Een textinput vult natuurlijk iets
        # Anders aan dan een knop.
        self.Sprite = Sprite
        # Naam zodat hij ook weer verwijderd kan worden
        self.Name = Name
        # Simpele positie
        self.Position = pygame.Vector2(Position)
        # Visible is zichtbaar, actief is interactief/klikbaar(bijvoorbeeld)
        self.Visible = Visible

    # Waar moet ie op tekenen?
    def Draw(self, Screen):
        Screen.blit(self.Sprite, self.Position)
    def Update(self):
        pass
