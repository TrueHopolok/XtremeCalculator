import pygame

class Portal():
    def __init__(self, screen):
        self.Screen = screen
        self.Pos = [450, 450]
        self.Size = [100, 100]
        self.Sprites = []
        self.CurrentSprite = 0
        for i in range(4):
            self.Sprites.append(pygame.transform.scale(pygame.image.load(f"../img/portal/portal{i}.png"), self.Size))
        self.AnimationTimer = 15
    def Update(self, player_pos : list, player_input : dict):
        if not player_input["space_just"]:
            return -1
        if self.Collide(self.Pos, self.Size, player_pos, [90, 90]):
            return 1
        return -1
    def Collide(self, r1 : list, s1 : list, r2 : list, s2 : list):
        if (r1[0] < r2[0] and r2[0] < r1[0] + s1[0]) or (r1[0] < r2[0] + s2[0] and r2[0] + s2[0] < r1[0] + s1[0]):
            return (r1[1] < r2[1] and r2[1] < r1[1] + s1[1]) or (r1[1] < r2[1] + s2[1] and r2[1] + s2[1] < r1[1] + s1[1])
        return False
    def Render(self, show : bool):
        if not show:
            return
        if self.AnimationTimer == 0:
            self.AnimationTimer = 15
            self.CurrentSprite += 1
            if self.CurrentSprite >= len(self.Sprites):
                self.CurrentSprite = 0
        self.AnimationTimer -= 1
        self.Screen.blit(self.Sprites[self.CurrentSprite], self.Pos)
            