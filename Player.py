import pygame, numpy as np
from Entity import Entity

# Speler class, handlet input en is centraal voor het spel. Is er maar 1 van in het spel.
class Player(Entity):
    def __init__(self, _Game, X: int = 0 , Y: int = 0, Z: int = 0, Rotation: int = 0):
        super().__init__(pygame.transform.scale(pygame.image.load("Art/Player.png"), (50, 50)), _Game, X, Y, Z, Rotation)

        # Hoe snel beweegt de speler?
        self.MaxSpeed_X, self.MaxSpeed_Y = 250, 250
        self.Speed_X, self.Speed_Y = 0, 0
        # Hoe snel valt de speler als je het gas niet indrukt?
        #self.Falling_Speed_Acceleration = 10000
        # Acceleratie in de x richting, met max snelheid 250 is de snelheid in 250/5000 seconden bereikt.
        self.Acceleration_X, self.Acceleration_Y = 5000, 5000
        # wrijving zodat de auto natuurlijk tot stilstand komt,
        # gegeven als vertragingsfactor 1/Friction zodat ie inzichtelijker is(Vind ik fijn)
        self.Friction = 1.005

    def Handle_Movement(self):
        # Input die de speler verplaatst aan de hand van een paar variabelen zoals acceleratie etc.
        Keys = pygame.key.get_pressed()
        if Keys[pygame.K_UP]:
            self.Speed_Y -= self.Acceleration_Y * self._Game._GameInfo.Deltatime
        if Keys[pygame.K_DOWN]:
            self.Speed_Y += self.Acceleration_Y * self._Game._GameInfo.Deltatime
        # Niet omhoog betekent omlaag.

        # TODO Uitvogelen hoe mijn trekkracht moet werken
        # else:
        #    if not Keys[pygame.K_DOWN]:
        #        # "Trekkracht van de baan": Gaat achteruit als je geen gas geeft
        #        self.Speed_Y += self.Falling_Speed_Acceleration * self._Game._GameInfo.Deltatime
        #    else:
        #        # "Trekkracht van de baan": Gaat achteruit als je geen gas geeft, Harder nu als je remt.
        #        self.Speed_Y += 2*(self.Falling_Speed_Acceleration * self._Game._GameInfo.Deltatime)
        #        print("We go  up")

        if Keys[pygame.K_LEFT]:
            self.Speed_X -= self.Acceleration_X * self._Game._GameInfo.Deltatime
        if Keys[pygame.K_RIGHT]:
            self.Speed_X += self.Acceleration_X * self._Game._GameInfo.Deltatime

        # Wrijvingscoefficient toepassen. Straks Alleen op X-as. Voor nu ook op de Y-As
        self.Speed_X *= 1 / self.Friction
        self.Speed_Y *= 1 / self.Friction

        # Houdt de snelheid van de spelers binnen de kaders van het spel.
        self.Speed_X = np.clip(self.Speed_X, -self.MaxSpeed_X, self.MaxSpeed_X)
        self.Speed_Y = np.clip(self.Speed_Y, -self.MaxSpeed_Y, self.MaxSpeed_Y)

        # Hier oefent de snelheid de verplaatsing uit als functie van de acceleratie.
        self.X += (self.Speed_X * self._Game._GameInfo.Deltatime)
        self.Y += (self.Speed_Y * self._Game._GameInfo.Deltatime)

        # Houdt de speler binnen de kaders van het spel, *2 omdat ie de rect vanaf links berekent
        self.X = np.clip(self.X, 0 + self.Width, self._Game._Screen.get_width() - 2 * self.Width)
        self.Y = np.clip(self.Y, 0 + self.Height, self._Game._Screen.get_height() - 2 * self.Height)

        # Debug statement
        # print(f"X: {self.X}, Y: {self.Y},\n Speed_X: {self.Speed_X}, Speed_Y: {self.Speed_Y},\n Acceleration: {self.Acceleration_X},\n Acceleration: {self.Acceleration_Y}")

        return None

    def Update(self):
        super().Update()
        self.Handle_Movement()

    def Draw(self):
        super().Draw()
        pass

