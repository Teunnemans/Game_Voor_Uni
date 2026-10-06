import pygame
import random
from Core import Constants
from Core.Entities.Enemies import TestEnemy


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
            self.SpawnEnemy()

    def SpawnEnemy(self):
        self.SpawnTimer = 0
        self._Game_Info.EntityList.append(TestEnemy(Constants.Images.Player, self._Game_Info._Game, pygame.Vector2(random.randint(0,500), 0)))

        # HIER DE SPAWNLOGICA
        # HIER DE LOGICA VOOR HET UPDATEN VAN DE SPAWNINTERVAL AAN DE HAND VAN EEN SCORE