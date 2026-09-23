import pygame
# Bestandje voor vaak gebruikte functies :)

# Ik begrijp de python intreperter niet helemaal, die geeft mij de warning: Expected type 'float', got 'SupportsDunderLT[Any] | SupportsDunderGT[Any]' instead
# Dit levert geen foutmelding op.

# Eigenlijk mijn eerdere clamp-functie, maar nu zonder Numpy, die steeds mijn types veranderde Returned ALTIJD een pygame vector
def Clamp_Vector(vector, minimum, maximum) -> pygame.Vector2:
    return pygame.Vector2( max(minimum.x, min(vector.x, maximum.x)), max(minimum.y, min(vector.y, maximum.y)))

def Round_Vector(vector, precision: int = 0) -> pygame.Vector2:
    return pygame.Vector2(round(vector.x, precision), round(vector.y, precision))