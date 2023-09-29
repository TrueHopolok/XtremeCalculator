import pygame
from ui.Menu import Menu

class GameState():
    def __init__(self, pause, mainmenu):
        self.Paused = pause
        self.MainMenu = mainmenu

class GameManager():
    def __init__(self, pause, main_menu, loaded_menu):
        self.INPUT = {"direction": [0, 0], "mouse": (), "m_pos": ()}
        self.STATE = GameState(pause, main_menu)
        self.MENU = loaded_menu
        # self.MENU = # main menu class #
    def update(self, events):
        ## Input handle
        self.INPUT["mouse"] = pygame.mouse.get_pressed(3)
        self.INPUT["m_pos"] = pygame.mouse.get_pos()
        for e in events:
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    ## TODO open option menu
                    pass
                if e.key == pygame.K_RIGHT:
                    self.INPUT["direction"][0] = 1
                if e.key == pygame.K_LEFT:
                    self.INPUT["direction"][0] = -1
                if e.key == pygame.K_DOWN:
                    self.INPUT["direction"][1] = 1
                if e.key == pygame.K_UP:
                    self.INPUT["direction"][1] = -1
            elif e.type == pygame.KEYUP:
                if e.key == pygame.K_RIGHT:
                    if self.INPUT["direction"][0] != -1:
                        self.INPUT["direction"][0] = 0
                if e.key == pygame.K_LEFT:
                    if self.INPUT["direction"][0] != 1:
                        self.INPUT["direction"][0] = 0
                if e.key == pygame.K_DOWN:
                    if self.INPUT["direction"][1] != -1:
                        self.INPUT["direction"][1] = 0
                if e.key == pygame.K_UP:
                    if self.INPUT["direction"][1] != 1:
                        self.INPUT["direction"][1] = 0
        print(self.INPUT) # DEBUG
        
        ## Menu logic
        if self.STATE.Paused:
            self.MENU.collision(self.INPUT["m_pos"])
        
        ## Game logic
        else:
            pass
            
        ## Rendering
        if not self.STATE.MainMenu:
            # walls
            # doors
            # buttons
            # obstacles
            # enemies
            # boses
            pass
        if self.STATE.Paused:
            self.MENU.render()