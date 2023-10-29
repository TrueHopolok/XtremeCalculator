import pygame
import math

class Player():
    def __init__(self, screen):
        self.Screen = screen
        self.Pos = [460,335]
        self.Speed = 4
        self.Health = 6
        self.Invulnerable = 60
        self.Reload = 20
        self.Rampage = 0
        self.Upgrade = 20
        self.Direction = [0, 0]
        self.Aim = [0, 0]
        self.Animations = []
        self.Animations.append(pygame.transform.scale(pygame.image.load(f"../img/player/idle.png"), (80, 80)))
        self.Animations.append(pygame.transform.scale(pygame.image.load(f"../img/player/gameover.png"), (600, 300)))
        self.Animations.append(pygame.transform.scale(pygame.image.load(f"../img/player/heart2.png"), (32, 32)))
        self.Animations.append(pygame.transform.scale(pygame.image.load(f"../img/player/heart1.png"), (32, 32)))
        self.Animations.append(pygame.transform.scale(pygame.image.load(f"../img/player/heart0.png"), (32, 32)))
    def Update(self, player_input : dict, player_bullets : list, enemy_bullets : list, enemy_killed : int):
        self.Direction[0] = player_input["direction"][0]
        self.Direction[1] = player_input["direction"][1]
        # dead
        if self.Health == 0:
            if player_input["lmb_just"]:
                return 1
            else:
                return -1
        # move
        self.Pos[0] = max(70, min(840, self.Pos[0] + player_input["direction"][0] * self.Speed))
        self.Pos[1] = max(40, min(575, self.Pos[1] + player_input["direction"][1] * self.Speed))
        # rampage
        if enemy_killed != 0:
            self.Reload = 0
            self.Rampage = 300
            self.Upgrade = max(4, min(20, self.Upgrade - 4))
        elif self.Rampage != 0:
            self.Rampage -= 1
        elif self.Upgrade != 20:
            self.Upgrade = max(4, min(20, self.Upgrade + 4))
            self.Rampage = 120
        # shoot
        if self.Reload != 0:
            self.Reload -= 1
        elif player_input["mouse"][0]:
            self.Reload = self.Upgrade
            vector = [player_input["m_pos"][0] - self.Pos[0] - 35, player_input["m_pos"][1] - self.Pos[1] - 40]
            magnitude = math.sqrt(vector[0] * vector[0] + vector[1] * vector[1])
            vector[0] /= magnitude
            vector[1] /= magnitude
            self.Aim[0] = vector[0]
            self.Aim[1] = vector[1]
            vector[0] *= 5
            vector[1] *= 5
            player_bullets.append({"pos": [self.Pos[0] + 35 + self.Aim[0], self.Pos[1] + 40 + self.Aim[1]], "dir":vector})
        # collide
        if self.Invulnerable != 0:
            self.Invulnerable -= 1
        else:
            b = 0
            for b in range(len(enemy_bullets)):
                if (self.Pos[0] + 10 < enemy_bullets["pos"][0] and enemy_bullets["pos"] < self.Pos[0] + 70) or (self.Pos[0] + 10 < enemy_bullets["pos"][0] + 32 and enemy_bullets["pos"] + 32 < self.Pos[0] + 70):
                    if (self.Pos[1] + 10 < enemy_bullets["pos"][1] and enemy_bullets["pos"] < self.Pos[1] + 70) or (self.Pos[1] + 10 < enemy_bullets["pos"][1] + 32 and enemy_bullets["pos"] + 32 < self.Pos[1] + 70): 
                        enemy_bullets.pop(b)
                        self.Invulnerable = 60
                        break
                b += 1
        return -1
    def Render(self):
        if self.Health == 0:
            self.Screen.blit(self.Animations[1], (200, 200))
            return
        if self.Invulnerable != 0:
            hearts = self.Health
            heartpos = [self.Pos[0] - 16, self.Pos[1] - 16]
            for i in range(3):
                if hearts == 0:
                    self.Screen.blit(self.Animations[4], heartpos)
                elif hearts == 1:
                    self.Screen.blit(self.Animations[3], heartpos)
                    hearts -= 1
                else:
                    self.Screen.blit(self.Animations[2], heartpos)
                    hearts -= 2
                heartpos[0] += 40
        self.Screen.blit(self.Animations[0], self.Pos)
        pass