import pygame

class Player():
    def __init__(self, screen):
        self.Screen = screen
        self.Pos = [460,335]
        self.Speed = 4
        self.Health = 3
        self.Invulnerable = 0
        self.Reload = 0
        self.Animations = []
        self.Animations.append(pygame.transform.scale(pygame.image.load(f"../img/player/idle.png"), (80, 80)))
    def Update(self, player_input : dict, player_bullets : list, enemy_bullets : list):
        # restart the game if player is dead
        if self.Health == 0 and self.Invulnerable == 0:
            return 1
        # move
        self.Pos[0] = max(70, min(840, self.Pos[0] + player_input["direction"][0] * self.Speed))
        self.Pos[1] = max(40, min(575, self.Pos[1] + player_input["direction"][1] * self.Speed))
        # shoot
        if self.Reload != 0:
            self.Reload -= 1
        elif player_input["mouse"][0]:
            self.Reload = 20
            player_bullets.append({"pos":self.Pos.copy(), "dir":[5, 5]})
            pass
        # collide
        if self.Invulnerable != 0:
            self.Invulnerable -= 1
        else:
            # check collision with bullets
            pass
        return -1
    def Render(self):
        if self.Health == 0:
            return
        self.Screen.blit(self.Animations[0], self.Pos)
        pass