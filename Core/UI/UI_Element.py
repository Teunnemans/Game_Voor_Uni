import pygame

# Basis klasse voor alle UI elementen
class UI_Element:
    def __init__(self, Root, Name, Sprite, Position, Visible = True):
        # Root is de groep waartoe de Element behoort
        self._Root = Root

        # Deze moet altijd ingevuld worden door de Class die deze inherit. Een textinput vult natuurlijk iets
        # Anders aan dan een knop.
        self.Sprite = Sprite
        # Naam zodat hij ook weer verwijderd kan worden
        self.Name = Name
        # Simpele positie
        self.Position = pygame.Vector2(Position)
        # Visible is zichtbaar, actief is interactief/klikbaar(bijvoorbeeld)
        self.Visible = Visible
    # Absolute positie van het element op het scherm
    def Get_Absolute_Position(self):
        Position = pygame.Vector2(self.Position)
        Root = self._Root

        while Root != "":
            Position += Root.Position #Self.position is de offset van de groep. verschuift alles bijvoorbeeld (0,50 naar rechts)
            Root = Root._Root

        return Position


    # Waar moet ie op tekenen?
    def Draw(self, Screen):
        # Bovenste laag bereikt.
        if self.Visible:
            Screen.blit(self.Sprite, self.Get_Absolute_Position())

    def Update(self, Eventstack):
        if self.Visible:
            pass
        pass

# Verzameling van UI elementen, kan gebruikt worden om UI te structureren. MAAKT UI HIERARCHISCH
class UI_Group:
    def __init__(self, Root, Name, Position, Visible = True):
        # Root is de groep waartoe de Element behoort
        self._Root = Root

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

    # Absolute positie van het element op het scherm
    def Get_Absolute_Position(self):
        Position = pygame.Vector2(self.Position)
        Root = self._Root

        while Root != "":
            Position += Root.Position #Self.position is de offset van de groep. verschuift alles bijvoorbeeld (0,50 naar rechts)
            Root = Root._Root

        return Position

    def Update(self, Eventstack):
        if self.Visible:
            for Element in self.Elements:
                Element.Update(Eventstack)

    def Draw(self, Screen):
        if self.Visible:
            for Element in self.Elements:
                Element.Draw(Screen)