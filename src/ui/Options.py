import pygame

class Options():
    def __init__(self, screen):
        self.SCREEN = screen
        self.Title = dict()
        self.MuteButton = dict()
        self.FpsCounter = dict()
        self.Title["pos"] = (400, 200)
        self.Title["obj"] = pygame.font.SysFont("Times New Roman", 40, True).render("Options:", True, (255, 255, 255))
        self.MuteButton["pos"] = (400, 300)
        self.MuteButton["size"] = (200, 100)
        self.MuteButton["obj"] = pygame.transform.scale(pygame.image.load("../img/missing_texture.png"), self.MuteButton["size"])
        self.FpsCounter["pos"] = (400, 450)
        self.FpsCounter["size"] = (200, 100)
        self.FpsCounter["obj"] = pygame.transform.scale(pygame.image.load("../img/missing_texture.png"), self.FpsCounter["size"])
    def Collision(self, player_input : dict):
        if player_input["lmb_just"]:
            if player_input["m_pos"][0] > self.MuteButton["pos"][0] and player_input["m_pos"][0] < self.MuteButton["pos"][0] + self.MuteButton["size"][0]:
                if player_input["m_pos"][1] > self.MuteButton["pos"][1] and player_input["m_pos"][1] < self.MuteButton["pos"][1] + self.MuteButton["size"][1]:
                    return 2
            if player_input["m_pos"][0] > self.FpsCounter["pos"][0] and player_input["m_pos"][0] < self.FpsCounter["pos"][0] + self.FpsCounter["size"][0]:
                if player_input["m_pos"][1] > self.FpsCounter["pos"][1] and player_input["m_pos"][1] < self.FpsCounter["pos"][1] + self.FpsCounter["size"][1]:
                    return 3
        return -1
    def Render(self):
        self.SCREEN.blit(self.Title["obj"], self.Title["pos"])
        self.SCREEN.blit(self.MuteButton["obj"], self.MuteButton["pos"])
        self.SCREEN.blit(self.FpsCounter["obj"], self.FpsCounter["pos"])