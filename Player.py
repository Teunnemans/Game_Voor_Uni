import pygame
from Entity import Entity
from Functions import Clamp_Vector

# Speler class, handlet input en is centraal voor het spel. Is er maar 1 van in het spel.
class Player(Entity):
    def __init__(self, _Game, Position: pygame.Vector2 = pygame.Vector2(0,0), Rotation: int = 0):
        super().__init__(pygame.transform.scale(pygame.image.load("Art/Player.png"), (50, 50)), _Game, Position, Rotation)

        # Hoe snel beweegt de speler?
        self.MaxSpeed = pygame.Vector2(250, 250)
        self.Speed = pygame.Vector2(0, 0)
        # Hoe snel versnelt de speler?
        self.Acceleration = pygame.Vector2(5000, 5000)

    # Input die de speler verplaatst aan de hand van een paar variabelen zoals acceleratie etc.
    def Handle_Movement(self):
        # TODO Uitvogelen hoe mijn trekkracht moet werken
        # Input die de speler verplaatst aan de hand van een paar variabelen zoals acceleratie etc.
        Keys = pygame.key.get_pressed()
        # Coole compactere versie van de inputregelaar die ik eerst had. Maakt van Direction een richtingvector die gebruikt
        # wordt bij het berekenen van de snelheid
        Direction = pygame.Vector2(
            Keys[pygame.K_RIGHT] - Keys[pygame.K_LEFT],
            Keys[pygame.K_DOWN] - Keys[pygame.K_UP] )

        # Nu ben je diagonaal niet meer sneller
        if Direction.length_squared() > 0:
            Direction = Direction.normalize()

        # Elementwise omdat hij anders het inproduct berekent en de snelheid omzet naar een scalar. Kostte mij veel debugtijd
        self.Speed += (Direction * self.Acceleration.elementwise() * self._Game.Get_GameInfo().Deltatime)
        # Frictie
        self.Speed *= max(0, 1 - self._Game.Get_GameInfo().Friction * self._Game.Get_GameInfo().Deltatime)
        self.Speed = Clamp_Vector(self.Speed, -self.MaxSpeed, self.MaxSpeed) # Houdt de snelheid van de spelers binnen de kaders van het spel.

        # Hier oefent de snelheid de verplaatsing uit als functie van de acceleratie.
        self.Position += (self.Speed * self._Game.Get_GameInfo().Deltatime)
        # Houdt de speler binnen de kaders van het spel.
        self.Position = Clamp_Vector(self.Position, (0, 0) + self.Size.elementwise(), pygame.Vector2(self._Game.Get_Screen().get_size()) - (2, 2) * self.Size.elementwise())

    def Update(self):
        super().Update()
        self.Handle_Movement()

    def Draw(self):
        super().Draw()
        pass

