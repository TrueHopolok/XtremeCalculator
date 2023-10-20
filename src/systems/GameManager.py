import pygame
import random
from ui.Menu import Menu
from entities.Player import Player
from entities.Boss import Boss

class GameState():
    def __init__(self, pause, mainmenu):
        self.Paused = pause
        self.MainMenu = mainmenu

class MiniBoss():
    def __init__(self):
        self.Rate = 0
        self.Chance = 0
        self.Respawn = 0

class GameInfo():
    def __init__(self):
        self.Loaded = False
        self.Rooms = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        self.CurrentRoom = 0
        self.ProblemsSolved = 0
        self.Problem = ""
        self.Answer = ""
        self.CurrentAnswer = ""
        self.MiniBoss = MiniBoss()

class GameManager():
    def __init__(self, pause, main_menu, loaded_menu):
        self.INPUT = {"direction": [0, 0], "mouse": (), "m_pos": ()}
        self.STATE = GameState(pause, main_menu)
        self.INFO = GameInfo()
        self.Player = Player()
        self.PlayerBullets = []
        self.Enemies = []
        self.EnemyBullets = []
        self.Boss = Boss()
        self.Button = Button()
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
        # print(self.INPUT) # DEBUG
        
        ## Menu logic
        if self.STATE.Paused:
            self.MENU.collision(self.INPUT["m_pos"])
        
        ## Load game
        elif not self.INFO.Loaded:
            self.INFO.Loaded = True
            self.INFO.Rooms[0] = 0
            self.INFO.CurrentRoom = 0
            for i in range(1, 12):
                j = random.randint(0, i)
                if self.INFO.Rooms[j] == 0:
                    self.INFO.CurrentRoom = i
                self.INFO.Rooms[i], self.INFO.Rooms[j] = self.INFO.Rooms[j], i
            match random.randint(0, 4):
                case 0: # +
                    a = random.randint(1, pow(10, max(0, min((self.INFO.ProblemsSolved+3)//2, 7))))
                    b = random.randint(1, pow(10, max(0, min((self.INFO.ProblemsSolved+3)//2, 7))))
                    self.INFO.Answer = f"{a+b}"
                    self.INFO.Problem = f"{a}+{b}="
                case 1: # -
                    a = random.randint(1, pow(10, max(0, min((self.INFO.ProblemsSolved+3)//2, 8))))
                    b = random.randint(1, pow(10, max(0, min((self.INFO.ProblemsSolved+3)//2, 8))))
                    if a < b:
                        a, b = b, a
                    self.INFO.Answer = f"{a-b}"
                    self.INFO.Problem = f"{a}-{b}="
                case 2: # *
                    a = random.randint(1, pow(10, max(0, min((self.INFO.ProblemsSolved+4)//4, 4))))
                    b = random.randint(1, pow(10, max(0, min((self.INFO.ProblemsSolved+4)//4, 4))))
                    self.INFO.Answer = f"{a*b}"
                    self.INFO.Problem = f"{a}*{b}="
                case 3: # /
                    a = random.randint(1, pow(10, max(0, min((self.INFO.ProblemsSolved+5)//4, 8))))
                    b = random.randint(1, pow(10, max(0, min((self.INFO.ProblemsSolved+4)//4, 3))))
                    if a < b:
                        a, b = b, a
                    self.INFO.Answer = f"{a//b}"
                    self.INFO.Problem = f"{a}//{b}="
            # print(self.INFO.Rooms, "\n", self.INFO.Problem, self.INFO.Answer, sep="") # DEBUG
            self.Player.Reset()
            self.PlayerBullets = []
            self.Enemies = []
            self.EnemyBullets = []
            self.Boss.Reset()
            self.INFO.MiniBoss.Chance = 0
            self.INFO.MiniBoss.Rate = self.INFO.ProblemsSolved
            self.INFO.MiniBoss.Respawn = 0
        
        ## Game logic
        else:
            b = 0
            while b < len(self.PlayerBullets):
                self.PlayerBullets[b]["pos"] += self.PlayerBullets[b]["dir"]
                if self.PlayerBullets[b]["pos"][0] * self.PlayerBullets[b]["pos"][1] < 0 or self.PlayerBullets[b]["pos"][0] + self.PlayerBullets[b]["pos"][1] > 1750:
                    self.PlayerBullets.pop(b)
                    continue
                b += 1
            b = 0
            while b < len(self.EnemyBullets):
                self.EnemyBullets[b]["pos"] += self.EnemyBullets[b]["dir"]
                if self.EnemyBullets[b]["pos"][0] * self.EnemyBullets[b]["pos"][1] < 0 or self.EnemyBullets[b]["pos"][0] + self.EnemyBullets[b]["pos"][1] > 1750:
                    self.EnemyBullets.pop(b)
                    continue
                b += 1
            self.Player.Update(self.INPUT, self.PlayerBullets, self.EnemyBullets)
            e = 0
            status = 0
            while e < len(self.Enemies):
                status = self.Enemies[e].Update(self.PlayerBullets, self.EnemyBullets)
                if status == -1:
                    self.Enemies.pop(e)
                    continue
                e += 1
            if self.Boss.State == "alive":
                self.Boss.Update(self.PlayerBullets, self.EnemyBullets)
            if self.Boss.State = "notspawned" and len(self.Enemies) == 0:
                status = self.Button.Update(self.Player.Pos, self.INPUT, self.INFO.CurrentRoom, self.INFO.Answer, self.INFO.CurrentAnswer)
                match status:
                    case 1:
                        self.Boss.State = "alive"
                    case 2:
                        # add to answer
                        pass
                    case 3:
                        # delete answer
                        pass
                    
            if self.Boss.State = "dead" and len(self.Enemies) == 0:
                self.Portal.Update(self.Player.Pos, self.INPUT)
                self.Doors.Update(self.INFO.Rooms)
            
            
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