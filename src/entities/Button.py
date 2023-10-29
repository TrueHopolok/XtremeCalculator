import pygame

class Button():
    def __init__(self, screen):
        self.Screen = screen
        self.LastRoom = 0
        self.Pressed = True
        self.Size = [80, 80]
        self.Yes = {}
        self.Yes["pos"] = [400, 335]
        self.Yes[True] = pygame.transform.scale(pygame.image.load(f"../img/buttons/yeson.png"), self.Size)
        self.Yes[False] = pygame.transform.scale(pygame.image.load(f"../img/buttons/yesoff.png"), self.Size)
        self.No = {}
        self.No["pos"] = [520, 335]
        self.No[True] = pygame.transform.scale(pygame.image.load(f"../img/buttons/noon.png"), self.Size)
        self.No[False] = pygame.transform.scale(pygame.image.load(f"../img/buttons/nooff.png"), self.Size)
    def Update(self, player_pos : list, player_input : dict, current_room : int, answer : dict):
        if self.LastRoom != current_room:
            self.LastRoom = current_room
            self.Pressed = False
        if not player_input["space_just"]:
            return -1
        if self.Pressed:
            return -1
        player_size = [80, 80]
        if self.Collide(player_pos, player_size, self.Yes["pos"], self.Size):
            self.Pressed = True
            if current_room == 10:
                return 1
            if len(answer["current"]) < 9:
                answer["current"] += str(current_room)
        if self.Collide(player_pos, player_size, self.No["pos"], self.Size):
            self.Pressed = True
            if len(answer["current"]) > 0:
                answer["current"] = answer["current"][:-1]
        return -1
    def Render(self):
        self.Screen.blit(self.Yes[(not self.Pressed)], self.Yes["pos"])
        self.Screen.blit(self.No[(not self.Pressed)], self.No["pos"])
    def Collide(self, r1 : list, s1 : list, r2 : list, s2 : list):
        if (r1[0] < r2[0] and r2[0] < r1[0] + s1[0]) or (r1[0] < r2[0] + s2[0] and r2[0] + s2[0] < r1[0] + s1[0]):
            return (r1[1] < r2[1] and r2[1] < r1[1] + s1[1]) or (r1[1] < r2[1] + s2[1] and r2[1] + s2[1] < r1[1] + s1[1])
        return False