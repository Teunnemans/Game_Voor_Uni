import random, pygame
from Core import Constants
from Core.Entities.Enemies import OscilatingEnemy, ClearingBomb, TailGater, SimpleEnemy, Heart
# Alle enemy gamelogica wordt in deze class gehandled. schaalt de moeilijkheid van het spel langzaam op.
class Spawner:
    def __init__(self, Game_Info):
        self._Game_Info = Game_Info
        # interval in seconden, die steeds kleiner wordt
        self.SpawnInterval = self.InitSpawnInterval = 5
        # Tijd sinds laatste spawn
        self.SpawnTimer = 0
        self.EnemyTypes = [OscilatingEnemy, TailGater, SimpleEnemy]


    def Update(self):
        self.SpawnTimer += self._Game_Info.Get_Game().Deltatime
        # Spawnrate schaalt liniair met de score. Hoe hoger de score, hoe lager de spawninterval
        self.SpawnInterval = max(0.5, self.InitSpawnInterval - (self._Game_Info.Score/2000)) # Elke 2000 punten 1 seconde sneller, korte potjes hierdoor, neemt steeds de hoogste waarde
        if self.SpawnTimer > self.SpawnInterval:
            self.Spawn_Enemy()

    # Functie zo geschreven dat je zelf ook enemies kan spawnen
    def Spawn_Enemy(self, Enemy=None):
        self.SpawnTimer = 0
        if Enemy is None:
            # Game spawn logica
            EnemyChoice = random.randint(0, len(self.EnemyTypes)-1)
            match EnemyChoice:
                case 0:
                    self._Game_Info.Add_Entity(self.Generate_Group())
                case 1:
                    # Richting, positie en snelheid
                    Position, Direction, SpriteDirection = self.Random_Outside_Position_And_Direction(False)
                    self._Game_Info.Add_Entity(OscilatingEnemy(Constants.Images.Oscillating_Enemy[SpriteDirection], self._Game_Info.Get_Game(), Position, (random.randint(100, 200) + 1 * self._Game_Info.Score/100)*Direction))
                case 2:
                    # Richting, positie en snelheid
                    Position, Direction, SpriteDirection = self.Random_Outside_Position_And_Direction(True)
                    self._Game_Info.Add_Entity(TailGater(Constants.Images.Tailgater_Enemy[SpriteDirection], self._Game_Info.Get_Game(), Position, (random.randint(100, 200) + 1 * self._Game_Info.Score/100)*Direction))
        else:
            self._Game_Info.Add_Entity(Enemy)


    # Standaard is 1, zo kun je dus ook gewoon 1 enemy toevoegen, maakt een groep standaard-enemies met een kans op een powerup
    def Generate_Group(self, Amount = None, PowerUp = None):
        Group = []
        if Amount is None: Amount = max(random.randint(1, round(self._Game_Info.Score/2000 + 1)), 10) # steeds meer enemies met een maximum van 10
        if PowerUp is None:
            PowerUp = False
            # 10% kans op 1 powerup
            if random.randint(1, 10) > 9:
                PowerUp = True
        # Richting, positie en snelheid, elke sprite moet dit hebben
        Position, Direction, SpriteDirection = self.Random_Outside_Position_And_Direction(True)
        Speed = random.randint(100, 200) + 1 * self._Game_Info.Score/100 # Snelheid schaalt liniair met de score
        Sprite = Constants.Images.Parallel_Enemy[SpriteDirection]
        # Hoeveelheid enemies
        for i in range(Amount):
            SpawnPosition = Position - 3.5 * Direction * (i * 50) # offset tussen de enemies Speling voor de speler
            Group.append(SimpleEnemy(Sprite, self._Game_Info.Get_Game(), SpawnPosition, Speed*Direction))
        # Vervangt 1 van de enemies met een powerup die je dan kunt pakken
        if PowerUp:
            PowerUpPos = random.randint(0, len(Group) - 1)
            PowerUpChoice = random.randint(0, 1) # Of bom, of hartje
            PowerUpChoices = [Heart(self._Game_Info.Get_Game(), Group[PowerUpPos].Position, Speed*Direction), ClearingBomb(self._Game_Info.Get_Game(), Group[PowerUpPos].Position, Speed*Direction)]
            Group[PowerUpPos] = PowerUpChoices[PowerUpChoice]
        return Group

    # Functie voor het genereren van een hele hoop informatie voor de enemy spawner, hopelijk leesbaar genoeg
    def Random_Outside_Position_And_Direction(self, Diagonal=True):
        Side = random.randint(0, 3)  # vanuit welke kant komt de enemy?
        Direction = pygame.Vector2(0, 0)  # Welke richting gaat hij op?
        Position = pygame.Vector2(0, 0)  # Welke positie spawnt hij dan in?
        match Side:
            case 0:  # Boven
                Position = pygame.Vector2(random.randint(0, 500), -50)
                Direction = pygame.Vector2(0, 1)
            case 1:  # Onder
                Position = pygame.Vector2(random.randint(0, 500), 550)
                Direction = pygame.Vector2(0, -1)
            case 2:  # Links
                Position = pygame.Vector2(-50, random.randint(0, 500))
                Direction = pygame.Vector2(1, 0)
            case 3:  # Rechts
                Position = pygame.Vector2(550, random.randint(0, 500))
                Direction = pygame.Vector2(-1, 0)

        if Diagonal:
            Target = pygame.Vector2(random.randint(0, 500), random.randint(0, 500))
            # Richting naar een willekeurig punt op het scherm
            Direction = Target - Position
            # Eenheidsvector van de richtingsvector
            Direction.normalize_ip()
            # Richting beklemmen zodat hij niet gekke hoeken maakt
            Direction.x = max(-1, min(1, round(Direction.x)))
            Direction.y = max(-1, min(1, round(Direction.y)))

        # Genereert een richting voor de sprite, zodat hij de juiste sprite kan displayen
        SpriteDirection = ""
        if Direction == (-1, 0):
            SpriteDirection = "LEFT"
        elif Direction == (1, 0):
            SpriteDirection = "RIGHT"
        elif Direction == (0, -1):
            SpriteDirection = "DOWN"
        elif Direction == (0, 1):
            SpriteDirection = "UP"
        elif Direction == (-1, -1):
            SpriteDirection = "LEFT-DOWN"
        elif Direction == (1, 1):
            SpriteDirection = "RIGHT-UP"
        elif Direction == (1, -1):
            SpriteDirection = "RIGHT-DOWN"
        elif Direction == (-1, 1):
            SpriteDirection = "LEFT-UP"

        return Position, Direction, SpriteDirection
