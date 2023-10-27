import pygame

class Boss():
    def __init__(self):
        self.State = "notspawned"
    def Reset(self):
        self.State = "notspawned"
    def Update(self, player_pos : list, player_input : dict, player_bullets : list, enemy_bullets : list):
        pass
    def Spawn(self):
        self.State = "alive"
        # give hp and etc
    def Render(self):
        pass