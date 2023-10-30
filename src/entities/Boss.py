import pygame

class Boss():
    def __init__(self, screen):
        self.Screen = screen
        self.State = "notspawned"
        self.Health = 20
    def Reset(self):
        self.State = "notspawned"
    def Update(self, player_pos : list, player_bullets : list, enemy_bullets : list):
        self.State = "dead"
    def Spawn(self):
        self.State = "alive"
        self.Health = 100
    def Render(self):
        pass