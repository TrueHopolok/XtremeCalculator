import pygame

class Boss():
    def __init__(self):
        self.State = "notspawned"
    def Reset(self):
        self.State = "notspawned"
    def Update(self, player_pos, _player_bullets, _enemy_bullets):
        pass