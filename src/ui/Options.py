import pygame

class Options():
    def __init__(self, screen, show_fps : bool):
        self.SCREEN = screen
        self.Background = dict()
        self.MuteButton = dict()
        self.FpsCounter = dict()
        self.Background["pos"] = (350, 200)
        self.Background["size"] = (300, 400)
        self.Background["obj"] = pygame.transform.scale(pygame.image.load("../img/ui/options_bg2.png"), self.Background["size"])
        self.MuteButton["pos"] = (400, 315)
        self.MuteButton["size"] = (200, 100)
        self.MuteButton[True] = pygame.transform.scale(pygame.image.load("../img/ui/soundOn.png"), self.MuteButton["size"])
        self.MuteButton[False] = pygame.transform.scale(pygame.image.load("../img/ui/soundOff.png"), self.MuteButton["size"])
        self.NotMuted = True # pygame.mixer.music.get_volume() != 0
        self.FpsCounter["pos"] = (400, 455)
        self.FpsCounter["size"] = (200, 100)
        self.FpsCounter[True] = pygame.transform.scale(pygame.image.load("../img/ui/FPSOn.png"), self.FpsCounter["size"])
        self.FpsCounter[False] = pygame.transform.scale(pygame.image.load("../img/ui/FPSOff.png"), self.FpsCounter["size"])
        self.ShowFPS = show_fps
    def Collision(self, player_input : dict):
        if player_input["lmb_just"]:
            if player_input["m_pos"][0] > self.MuteButton["pos"][0] and player_input["m_pos"][0] < self.MuteButton["pos"][0] + self.MuteButton["size"][0]:
                if player_input["m_pos"][1] > self.MuteButton["pos"][1] and player_input["m_pos"][1] < self.MuteButton["pos"][1] + self.MuteButton["size"][1]:
                    self.NotMuted = not self.NotMuted
                    return 2
            if player_input["m_pos"][0] > self.FpsCounter["pos"][0] and player_input["m_pos"][0] < self.FpsCounter["pos"][0] + self.FpsCounter["size"][0]:
                if player_input["m_pos"][1] > self.FpsCounter["pos"][1] and player_input["m_pos"][1] < self.FpsCounter["pos"][1] + self.FpsCounter["size"][1]:
                    self.ShowFPS = not self.ShowFPS
                    return 3
        return -1
    def Render(self):
        self.SCREEN.blit(self.Background["obj"], self.Background["pos"])
        self.SCREEN.blit(self.MuteButton[self.NotMuted], self.MuteButton["pos"])
        self.SCREEN.blit(self.FpsCounter[self.ShowFPS], self.FpsCounter["pos"])