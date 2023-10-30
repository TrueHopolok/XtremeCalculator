import pygame
import random
import math

class Boss():
    def __init__(self, screen):
        self.Screen = screen
        self.Font = pygame.font.SysFont("Cascadia Code", 40, True)
        self.State = "notspawned"
        self.IsAttacking = False
        self.IsMainAttack = False
        self.Health = 20
        self.Damaged = False
        self.Pos = [100, 100]
        self.Direction = [0, 0]
        self.HitBoxOffset = [40, 20]
        self.Size = [300, 225]
        self.Reload = 0
        self.CurrentSprite = 0
        self.WalkAnimation = []
        self.WalkAnimation.append(pygame.transform.scale(pygame.image.load(f"../img/boss/idle.png"), self.Size))
        self.MainAttackAnimation = []
        self.MainAttackAnimation.append(pygame.transform.scale(pygame.image.load(f"../img/boss/idle.png"), self.Size))
        self.SecondAttackAnimation = []
        self.SecondAttackAnimation.append(pygame.transform.scale(pygame.image.load(f"../img/boss/idle.png"), self.Size))
    def Update(self, player_pos : list, player_bullets : list, enemy_bullets : list):
        # dead
        if self.Health <= 0:
            self.State = "dead"
            return
        # collide
        b = 0
        pos = [self.Pos[0] + self.HitBoxOffset[0], self.Pos[1] + self.HitBoxOffset[1]]
        size = [self.Size[0] - self.HitBoxOffset[0], self.Size[1] - self.HitBoxOffset[1]]
        while b < len(player_bullets):
            if self.Collide(pos, size, player_bullets[b]["pos"], [20, 20]):
                player_bullets.pop(b)
                self.Health -= 1
                self.Damaged = True
                continue
            b += 1
        # walk
        if self.Reload <= 90:
            self.Pos[0] = max(70, min(920 - self.Size[0], self.Pos[0] + self.Direction[0]))
            self.Pos[1] = max(40, min(655 - self.Size[1], self.Pos[1] + self.Direction[1]))
        # reloading
        if self.Reload != 0:
            self.Reload -= 1
        # attack
        else:
            self.CurrentSprite = 0
            self.Direction = [random.randint(-4, 4), random.randint(-4, 4)]
            self.IsAttacking = True
            self.IsMainAttack = random.randint(0, 1) == 0
            self.Reload = 120
            # first attack
            if self.IsMainAttack:
                pos = [self.Pos[0] + self.Size[0]//2, self.Pos[1] + self.Size[1]//2]
                for i in range(0, 360, 10):
                    enemy_bullets.append({"pos":pos.copy(), "dir":[math.cos(math.radians(i))*2, math.sin(math.radians(i))*2]})
                return
            # second attack
            pos = [self.Pos[0], self.Pos[1]]
            step = [self.Size[0]//5, self.Size[1]//5]
            for i in range(25):
                enemy_bullets.append({"pos": pos.copy(), "dir":[0, 0]})
                if i%5==4:
                    pos[0] = self.Pos[0]
                    pos[1] += step[1]
                else:
                    pos[0] += step[0]         
    def Collide(self, r1 : list, s1 : list, r2 : list, s2 : list):
        if (r1[0] < r2[0] and r2[0] < r1[0] + s1[0]) or (r1[0] < r2[0] + s2[0] and r2[0] + s2[0] < r1[0] + s1[0]):
            return (r1[1] < r2[1] and r2[1] < r1[1] + s1[1]) or (r1[1] < r2[1] + s2[1] and r2[1] + s2[1] < r1[1] + s1[1])
        return False
    def Spawn(self, floor : int):
        self.State = "alive"
        self.Health = 20 + floor * 2
        self.Pos = [100, 100]
        self.Reload = 15
        self.CurrentSprite = 0
    def Render(self):
        pos = [self.Pos[0] + self.Size[0] // 2 - 10, self.Pos[1] - 20]
        self.Screen.blit(self.Font.render(f"{self.Health}", False, (0, 255, 255)), pos)
        if self.IsAttacking:
            if self.IsMainAttack:
                self.Screen.blit(self.MainAttackAnimation[self.CurrentSprite], self.Pos)
                self.CurrentSprite += 1
                if self.CurrentSprite >= len(self.MainAttackAnimation):
                    self.CurrentSprite = 0
                    self.IsAttacking = False
            else:
                self.Screen.blit(self.SecondAttackAnimation[self.CurrentSprite], self.Pos)
                self.CurrentSprite += 1
                if self.CurrentSprite >= len(self.SecondAttackAnimation):
                    self.CurrentSprite = 0
                    self.IsAttacking = False
        else:
            self.Screen.blit(self.WalkAnimation[self.CurrentSprite], self.Pos)
            self.CurrentSprite += 1
            if self.CurrentSprite >= len(self.WalkAnimation):
                self.CurrentSprite = 0