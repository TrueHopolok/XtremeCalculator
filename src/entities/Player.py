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
            self.Rampage = 20
            self.Upgrade = max(8, min(20, self.Upgrade - 3))
        elif self.Rampage != 0:
            self.Rampage -= 1
        elif self.Upgrade != 20:
            self.Upgrade = max(8, min(20, self.Upgrade + 1))
            self.Rampage = 20
        # shoot
        if self.Reload != 0:
            self.Reload -= 1
        elif player_input["mouse"][0]:
            self.Reload = 1
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
            player_pos = [self.Pos[0] + 30, self.Pos[1] + 30]
            player_size = [20, 20]
            bullet_pos = [0, 0]
            bullet_size = [14, 14]
            b = 0
            for b in range(len(enemy_bullets)):
                bullet_pos = [enemy_bullets[b]["pos"][0] + 3, enemy_bullets[b]["pos"][1] + 3]
                if self.Collide(player_pos, player_size, bullet_pos, bullet_size):
                    enemy_bullets.pop(b)
                    self.Health -= 1
                    self.Invulnerable = 60
                    break
                b += 1
        return -1
    def Collide(self, r1 : list, s1 : list, r2 : list, s2 : list):
        if (r1[0] < r2[0] and r2[0] < r1[0] + s1[0]) or (r1[0] < r2[0] + s2[0] and r2[0] + s2[0] < r1[0] + s1[0]):
            return (r1[1] < r2[1] and r2[1] < r1[1] + s1[1]) or (r1[1] < r2[1] + s2[1] and r2[1] + s2[1] < r1[1] + s1[1])
        return False
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