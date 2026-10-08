import pygame

from Core import Constants
from Core.UI.UI_Element import UI_Element, UI_Group


class Image(UI_Element):
    def __init__(self, Root, Name, Image, Position, Visible=True):
        super().__init__(Root, Name, Image, Position, Visible)


# Simpel text element :) Kan gebruikt worden voor alles, zoals bijvoorbeeld IN een button,
class Text_Element(UI_Element):
    def __init__(self,Root, Name, Text, Position, Color=(255, 255, 255), Font= Constants.Game_Settings.Standard_Font,Visible=True):

        # Alles voor het renderen van text
        self.Text = Text
        self.Font = Font
        self.Color = Color

        super().__init__(Root, Name, Font.render(self.Text, True, Color), Position, Visible)

    def Draw(self, Screen, Offset = (0, 0)):
        # Rerenderd de sprite voor als de tekst veranderd is.
        self.Sprite = self.Font.render(self.Text, True, self.Color)
        super().Draw(Screen)

# Als je er goed overna denkt is een knop natuurlijk een tekst+een plaatje, daarom een ui_grouo
class Button(UI_Group):
    def __init__(self, Root,  Name, Position, Size, _Image = None, Text="",  Color=(255, 255, 255), Font=Constants.Game_Settings.Standard_Font, Visible=True):
        super().__init__(Root, Name, Position, Visible)

        # Elke knop bestaat uit een klikbaar deel en een textdeel, zodat je de knop kan zien
        self.Color = Color
        if _Image is not None:
            self.Size = _Image.get_size()
        else:
            self.Size = Size
        self.Rect = pygame.Rect(Position, self.Size)
        # Elke knop bestaat uit een klikbaar deel en een textdeel, zodat je de knop kan zien, op te roepen met Get_Element("Name")
        self.Add_Element(Image(self, Name + "-Image", _Image, (0, 0))) #(0, 0) relatief aan de button
        self.Add_Element(Text_Element(self, Name + "-Text", Text, (0, 0), Color, Font))

        # Toggle functie, zodat hij niet de event queue vult
        self.ShouldPostEvent = True

    def Update(self, Eventstack):
        # Update de text, image :)
        super().Update(Eventstack)

        # Press logica
        self.Rect = pygame.Rect(self.Get_Absolute_Position(), self.Size)
        Mouse_Pos = pygame.mouse.get_pos()
        Mouse_Pressed = pygame.mouse.get_pressed()
        if Mouse_Pressed[0] == 1:
            if self.Rect.collidepoint(Mouse_Pos):
                if self.ShouldPostEvent:
                    self.ShouldPostEvent = False
                    pygame.event.post(pygame.event.Event(pygame.USEREVENT, {"Type": "Button_Pressed", "Name": self.Name}))
        else:
            self.ShouldPostEvent = True
    def Draw(self, Screen, Offset = (0, 0)):
        super().Draw(Screen)
        if Constants.Game_Settings.Debug:
            pygame.draw.rect(Screen, (255, 0,0 ), self.Rect)