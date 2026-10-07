import pygame
import random
from Core import Constants
from Core.Entities.Enemies import OscilatingEnemy, ClearingBomb, TailGater, SimpleEnemy
from Core.Functions import Random_Outside_Position_And_Direction


class Spawner:
    def __init__(self, Game_Info):
        self._Game_Info = Game_Info
        # interval in seconden, die steeds kleiner wordt
        self.SpawnInterval = 2
        # Tijd sinds laatste spawn
        self.SpawnTimer = 0
    def Update(self):
        self.SpawnTimer += self._Game_Info._Game.Deltatime
        if self.SpawnTimer > self.SpawnInterval:
            #pass
            self.Spawn_Enemy()
    def Spawn_Enemy(self, Enemy=None):
        self.SpawnTimer = 0
        if Enemy is None:
            self._Game_Info.Add_Entity(self.Generate_Group())
        else:
            self._Game_Info.Add_Entity(Enemy)


    # Standaard is 1, zo kun je dus ook gewoon 1 enemy toevoegen
    def Generate_Group(self, Amount = None):
        Group = []

        #TODO HIER ENEMYKEUZE BEPALEN

        if Amount is None:
            Amount = random.randint(1, 10)

        # Richting, positie en snelheid, elke sprite moet dit hebben
        Position, Direction = Random_Outside_Position_And_Direction(False) # Diagonaal is False
        Speed = random.randint(100, 200)

        # Hoeveelheid enemies
        for i in range(Amount):
            SpawnPosition = Position - 3 * Direction * (i * 50) # offset tussen de enemies, 10 pixels speling
            Group.append(SimpleEnemy(Constants.Images.Player, self._Game_Info._Game, SpawnPosition, Speed*Direction))
        return Group