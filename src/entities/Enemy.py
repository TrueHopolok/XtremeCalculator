import pygame
import random
import math

class Enemy():
    def __init__(self, screen, number : int):
        self.Screen = screen
        self.Pos = [random.randint(200, 700), random.randint(200, 500)]
        self.Size = [80, 100]
        self.Health = 2
        self.MovSpeed = 1
        self.AtkSpeed = 60
        self.AtkSpread = 1
        self.Wait = 0
        self.WaitTime = 5
        self.BulletSpeed = 2
        self.Distance = 10000
        self.Aim = [0, 0]
        self.Sprites = []
        self.CurrentSprite = 0
        self.AnimationTimer = 0
        match number:
            case 1:
                self.Sprites.append(pygame.transform.scale(pygame.image.load(f"../img/enemies/1.png"), self.Size))
            case 2:
                self.Sprites.append(pygame.transform.scale(pygame.image.load(f"../img/enemies/2.png"), self.Size))
                self.MovSpeed = 2
            case 3:
                self.Sprites.append(pygame.transform.scale(pygame.image.load(f"../img/enemies/3.png"), self.Size))
                self.AtkSpeed = 25
            case 4:
                self.Sprites.append(pygame.transform.scale(pygame.image.load(f"../img/enemies/4.png"), self.Size))
                self.AtkSpeed = 90
                self.BulletSpeed = 3
                self.AtkSpread = 5
                self.WaitTime = 10
            case 5:
                self.Sprites.append(pygame.transform.scale(pygame.image.load(f"../img/enemies/5.png"), self.Size))
                self.BulletSpeed = 3
                self.AtkTime = 30
                self.WaitTime = 30
            case 6:
                self.Size = [80, 120]
                self.Sprites.append(pygame.transform.scale(pygame.image.load(f"../img/enemies/6.png"), self.Size))
                self.Health = 4
                self.MovSpeed = 3
                self.Distance = 625
            case 7:
                self.Sprites.append(pygame.transform.scale(pygame.image.load(f"../img/enemies/7.png"), self.Size))
                self.Health = 3
                self.MovSpeed = 2
                self.BulletSpeed = 5
                self.AtkSpeed = 120
                self.Distance = 22500
                self.WaitTime = 20
            case 8:
                self.Size = [200, 150]
                self.Sprites.append(pygame.transform.scale(pygame.image.load(f"../img/enemies/8.png"), self.Size))
                self.Health = 8
                self.AtkSpeed = 120
                self.AtkSpread = 10
                self.Distance = 0
                self.WaitTime = 30
            case 9:
                self.Sprites.append(pygame.transform.scale(pygame.image.load(f"../img/enemies/9.png"), self.Size))
                self.Health = 3
                self.MovSpeed = 3
                self.BulletSpeed = 1
                self.AtkSpread = 30
                self.AtkSpeed = 300
                self.WaitTime = 60
            case _:
                self.Sprites.append(pygame.transform.scale(pygame.image.load(f"../img/enemies/0.png"), self.Size))
        self.Reload = random.randint(self.AtkSpeed//2, self.AtkSpeed)
        self.MaxX = 920 - self.Size[0]
        self.MaxY = 655 - self.Size[1]
        self.RandX = 1
        self.RandY = 1
        self.RandTimer = 0
        self.RandSign = [1, -1]
    def Update(self, player_pos : list, player_bullets : list, enemy_bullets : list):
        # dead
        if self.Health <= 0:
            return 1
        # collide
        bullet_size = [20, 20]
        b = 0
        while b < len(player_bullets):
            if self.Collide(self.Pos, self.Size, player_bullets[b]["pos"], bullet_size):
                player_bullets.pop(b)
                self.Health -= 1
                if self.Health <= 0:
                    return 1
                continue
            b += 1
        # move
        if self.Reload != 0:
            self.Reload -= 1
            if self.Wait != 0:
                self.Wait -= 1
            else:
                distance = abs((player_pos[0] - self.Pos[0]) * (player_pos[1] - self.Pos[1]))
                if self.RandTimer != 0:
                    self.RandTimer -= 1
                    self.Pos[0] = max(70, min(self.MaxX, self.Pos[0]+self.MovSpeed*self.RandX))
                    self.Pos[1] = max(40, min(self.MaxY, self.Pos[1]+self.MovSpeed*self.RandY))
                elif distance < self.Distance:
                    if player_pos[0] < self.Pos[0]:
                        self.Pos[0] = max(70, min(self.MaxX, self.Pos[0]+self.MovSpeed))
                    else:
                        self.Pos[0] = max(70, min(self.MaxX, self.Pos[0]-self.MovSpeed))
                    if player_pos[1] < self.Pos[1]:
                        self.Pos[1] = max(40, min(self.MaxY, self.Pos[1]+self.MovSpeed))
                    else:
                        self.Pos[1] = max(40, min(self.MaxY, self.Pos[1]-self.MovSpeed))
                elif distance > self.Distance * 2 or self.Pos[0] == 70 or self.Pos[0] == self.MaxX or self.Pos[1] == 40 or self.Pos[1] == self.MaxY:
                    if player_pos[0] < self.Pos[0]:
                        self.Pos[0] = max(70, min(self.MaxX, self.Pos[0]-self.MovSpeed))
                    else:
                        self.Pos[0] = max(70, min(self.MaxX, self.Pos[0]+self.MovSpeed))
                    if player_pos[1] < self.Pos[1]:
                        self.Pos[1] = max(40, min(self.MaxY, self.Pos[1]-self.MovSpeed))
                    else:
                        self.Pos[1] = max(40, min(self.MaxY, self.Pos[1]+self.MovSpeed))
                else:
                    self.RandTimer = 90
                    self.RandX = self.RandSign[random.randint(0, 1)]
                    self.RandY = self.RandSign[random.randint(0, 1)]
        # shoot
        else:
            self.Wait = self.WaitTime
            self.Reload = self.AtkSpeed
            vector = [player_pos[0] - self.Pos[0] - self.Size[0]//2, player_pos[1] - self.Pos[1] - self.Size[1]//2]
            magnitude = math.sqrt(vector[0] * vector[0] + vector[1] * vector[1])
            vector[0] /= magnitude
            vector[1] /= magnitude
            self.Aim[0] = vector[0]
            self.Aim[1] = vector[1]
            vector[0] *= self.BulletSpeed
            vector[1] *= self.BulletSpeed
            enemy_bullets.append({"pos": [self.Pos[0] + self.Size[0]//2, self.Pos[1] + self.Size[1]//2], "dir":vector.copy()})
            for i in range(1, self.AtkSpread):
                vector[0] += (random.random() - 0.5) * 2
                vector[1] += (random.random() - 0.5) * 2
                enemy_bullets.append({"pos": [self.Pos[0] + self.Size[0]//2, self.Pos[1] + self.Size[1]//2], "dir":vector.copy()})
        return -1
    def Collide(self, r1 : list, s1 : list, r2 : list, s2 : list):
        if (r1[0] < r2[0] and r2[0] < r1[0] + s1[0]) or (r1[0] < r2[0] + s2[0] and r2[0] + s2[0] < r1[0] + s1[0]):
            return (r1[1] < r2[1] and r2[1] < r1[1] + s1[1]) or (r1[1] < r2[1] + s2[1] and r2[1] + s2[1] < r1[1] + s1[1])
        return False
    def Render(self):
        if self.AnimationTimer == 0:
            self.AnimationTimer = 15
            self.CurrentSprite += 1
            if self.CurrentSprite >= len(self.Sprites):
                self.CurrentSprite = 0
        self.AnimationTimer -= 1
        self.Screen.blit(self.Sprites[self.CurrentSprite], self.Pos)