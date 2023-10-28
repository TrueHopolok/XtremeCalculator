import pygame

'''
        Xtreme Calculator

             START

          text as guide
             
'''
# START button pos  = ()
# START button size = ()

class MainMenu():
    def __init__(self, screen):
        self.SCREEN = screen
        self.Title = dict()
        self.StartButton = dict()
        self.Guide1 = dict()
        self.Guide2 = dict()
        self.Guide3 = dict()
        self.Title["pos"] = (320, 100)
        self.Title["obj"] = pygame.font.SysFont("Times New Roman", 50).render("Xtreme Calculator", True, (255, 255, 255))
        self.StartButton["pos"] = (400, 300)
        self.StartButton["size"] = (200, 100)
        self.StartButton["obj"] = pygame.transform.scale(pygame.image.load("../img/missing_texture.png"), self.StartButton["size"])
        self.Guide1["pos"] = (50, 650)
        self.Guide1["obj"] = pygame.font.SysFont("Arial", 20).render("To aim move mouse | To shoot use left mouse button", True, (255, 255, 255))
        self.Guide2["pos"] = (50, 670)
        self.Guide2["obj"] = pygame.font.SysFont("Arial", 20).render("To move use ARROWS | To interact use SPACEBAR | ESC to open options menu", True, (255, 255, 255))
        self.Guide3["pos"] = (50, 690)
        self.Guide3["obj"] = pygame.font.SysFont("Arial", 20).render("Your goal is to solve as many math problems as possible while not dying", True, (255, 255, 255))
    def Collision(self, player_input : dict):
        if player_input["lmb_just"]:
            if player_input["m_pos"][0] > self.StartButton["pos"][0] and player_input["m_pos"][0] < self.StartButton["pos"][0] + self.StartButton["size"][0]:
                if player_input["m_pos"][1] > self.StartButton["pos"][1] and player_input["m_pos"][1] < self.StartButton["pos"][1] + self.StartButton["size"][1]:
                    return 1
        return -1
    def Render(self):
        self.SCREEN.blit(self.Title["obj"], self.Title["pos"])
        self.SCREEN.blit(self.StartButton["obj"], self.StartButton["pos"])
        self.SCREEN.blit(self.Guide1["obj"], self.Guide1["pos"])
        self.SCREEN.blit(self.Guide2["obj"], self.Guide2["pos"])
        self.SCREEN.blit(self.Guide3["obj"], self.Guide3["pos"])