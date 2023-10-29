import pygame

'''
0 1 2
3 4 5
6 7 8
9 10 11
if 0, 3, 8, 11: check 2 doors
lower +3 (cur//3!=4) / higher -3 (cur-3>=0)
left -1 (cur%3!=0) / right +1 (cur%3!=2)
'''

class Doors():
    def __init__(self, screen):
        self.Screen = screen
        self.IsOpen = False
        self.Doors = {"left" : {}, "right" : {}, "up" : {}, "bottom" : {}, "size" : []}
        self.Doors["size"] = [100, 100]
        self.Doors["left"]["pos"] = [5, 325]
        self.Doors["left"][True] = pygame.transform.rotate(pygame.transform.scale(pygame.image.load(f"../img/doors/dooropen.png"), self.Doors["size"]), 90)
        self.Doors["left"][False] = pygame.transform.rotate(pygame.transform.scale(pygame.image.load(f"../img/doors/doorclose.png"), self.Doors["size"]), 90)
        self.Doors["right"]["pos"] = [895, 325]
        self.Doors["right"][True] = pygame.transform.rotate(pygame.transform.scale(pygame.image.load(f"../img/doors/dooropen.png"), self.Doors["size"]), -90)
        self.Doors["right"][False] = pygame.transform.rotate(pygame.transform.scale(pygame.image.load(f"../img/doors/doorclose.png"), self.Doors["size"]), -90)
        self.Doors["up"]["pos"] = [450, 5]
        self.Doors["up"][True] = pygame.transform.scale(pygame.image.load(f"../img/doors/dooropen.png"), self.Doors["size"])
        self.Doors["up"][False] = pygame.transform.scale(pygame.image.load(f"../img/doors/doorclose.png"), self.Doors["size"])
        self.Doors["bottom"]["pos"] = [450, 645]
        self.Doors["bottom"][True] = pygame.transform.rotate(pygame.transform.scale(pygame.image.load(f"../img/doors/dooropen.png"), self.Doors["size"]), 180)
        self.Doors["bottom"][False] = pygame.transform.rotate(pygame.transform.scale(pygame.image.load(f"../img/doors/doorclose.png"), self.Doors["size"]), 180)
    def Update(self, player_pos : list, player_input : dict, current_room : int, rooms : list):
        self.IsOpen = True
        if not player_input["space_just"]:
            return -1
        player_size = [80, 80]
        if self.RoomExist(current_room, current_room - 1, rooms) and self.Collide(self.Doors["left"]["pos"], self.Doors["size"], player_pos, player_size):
            player_pos[0] = 840
            player_pos[1] = 335
            return current_room - 1
        if self.RoomExist(current_room, current_room + 1, rooms) and self.Collide(self.Doors["right"]["pos"], self.Doors["size"], player_pos, player_size):
            player_pos[0] = 70
            player_pos[1] = 335
            return current_room + 1
        if self.RoomExist(current_room, current_room - 3, rooms) and self.Collide(self.Doors["up"]["pos"], self.Doors["size"], player_pos, player_size):
            player_pos[0] = 460
            player_pos[1] = 575
            return current_room - 3
        if self.RoomExist(current_room, current_room + 3, rooms) and self.Collide(self.Doors["bottom"]["pos"], self.Doors["size"], player_pos, player_size):
            player_pos[0] = 460
            player_pos[1] = 40
            return current_room + 3
        return -1
    def Render(self, current_room : int, rooms : list):
        if self.RoomExist(current_room, current_room - 1, rooms):
            self.Screen.blit(self.Doors["left"][self.IsOpen], self.Doors["left"]["pos"])
        if self.RoomExist(current_room, current_room + 1, rooms):
            self.Screen.blit(self.Doors["right"][self.IsOpen], self.Doors["right"]["pos"])
        if self.RoomExist(current_room, current_room - 3, rooms):
            self.Screen.blit(self.Doors["up"][self.IsOpen], self.Doors["up"]["pos"])
        if self.RoomExist(current_room, current_room + 3, rooms):
            self.Screen.blit(self.Doors["bottom"][self.IsOpen], self.Doors["bottom"]["pos"])
        self.IsOpen = False
    def RoomExist(self, prev : int, id : int, rooms : list):
        if id < 0 or id > 11:
            return False
        if rooms[id] == 11:
            return False
        match id - prev:
            case -1:
                return prev%3 > 0
            case 1:
                return prev%3 < 2
            case 3:
                return prev<9
            case -3:
                return prev>2
            case _:
                return False
    def Collide(self, r1 : list, s1 : list, r2 : list, s2 : list):
        if (r1[0] < r2[0] and r2[0] < r1[0] + s1[0]) or (r1[0] < r2[0] + s2[0] and r2[0] + s2[0] < r1[0] + s1[0]):
            return (r1[1] < r2[1] and r2[1] < r1[1] + s1[1]) or (r1[1] < r2[1] + s2[1] and r2[1] + s2[1] < r1[1] + s1[1])
        return False