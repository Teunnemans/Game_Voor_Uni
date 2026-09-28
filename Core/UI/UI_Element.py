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
        if self.Visible:
            Screen.blit(self.Sprite, self.Position)
    def Update(self, Eventstack):
        if self.Visible:
            pass
        pass

# Verzameling van UI elementen, kan gebruikt worden om UI te structureren. MAAKT UI HIERARCHISCH
class UI_Group:
    def __init__(self, Name, Position, Visible = True):
        self.Name = Name
        self.Position = pygame.Vector2(Position)
        self.Visible = Visible

        self.Elements = []

    def Add_Element(self, Element): self.Elements.append(Element)
    def Remove_Element(self, Element): self.Elements.remove(Element)

    # Returned een element
    def Get_Element(self, ID):
        for Element in self.Elements:
            if Element.Name == ID:
                return Element
        return None

    def Update(self, Eventstack):
        if self.Visible:
            for Element in self.Elements:
                Element.Update(Eventstack)
    def Draw(self, Screen):
        if self.Visible:
            for Element in self.Elements:
                Element.Draw(Screen)