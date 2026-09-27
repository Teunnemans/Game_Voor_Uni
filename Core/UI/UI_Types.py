from Core.UI.UI_Element import UI_Element


class Image(UI_Element):
    def __init__(self, Name, Image, Position,  Visible=True):
        super().__init__(Name, Image, Position, Visible)

    def Draw(self, Screen):
        Screen.blit(self.Sprite, self.Position)

# Simpel text element :) Kan gebruikt worden voor alles/
class Text_Element(UI_Element):
    def __init__(self, Name, Text, Position, Font= None, Color=(255, 255, 255), Visible=True):

        # Alles voor het renderen van text
        self.Text = Text
        self.Font = Font
        self.Color = Color

        super().__init__(Name, Font.render(self.Text, True, Color), Position, Visible)

    def Draw(self, Screen):
        # Rerenderd de sprite voor als de tekst veranderd is.
        self.Sprite = self.Font.render(self.Text, True, self.Color)
        Screen.blit(self.Sprite, self.Position)
