import pygame
import random
from ui.MainMenu import MainMenu
from ui.Options import Options
from entities.Player import Player
from entities.Boss import Boss
from entities.Button import Button
from entities.Doors import Doors
from entities.Portal import Portal

class MiniBoss():
    def __init__(self):
        self.Rate = 0
        self.Chance = 0
        self.Respawn = 0

class MainInfo():
    def __init__(self):
        self.Loaded = False
        self.Rooms = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        self.CurrentRoom = 0
        self.ProblemsSolved = 0
        self.Problem = ""
        self.Answer = ""
        self.CurrentAnswer = ""
        self.MiniBoss = MiniBoss()

class Menus():
    def __init__(self, is_main_menu : bool, is_options : bool):
        self.IsMainMenu = is_main_menu
        self.IsOptionsMenu = is_options
        self.MainMenu = MainMenu()
        self.OptionsMenu = Options()
    def Collision(self, player_input : dict):
        if self.IsMainMenu and (not self.IsOptionsMenu):
            self.MainMenu.Collision(player_input)
        elif self.IsOptionsMenu:
            self.OptionsMenu.Collision(player_input)
    def Render(self):
        if self.IsMainMenu:
            self.MainMenu.Render()
        if self.OptionsMenu:
            self.OptionsMenu.Render()

class Entities():
    def __init__(self):
        self.Player = Player()
        self.PlayerBullets = []
        self.Enemies = []
        self.EnemyBullets = []
        self.Boss = Boss()
        self.Button = Button()
        self.Doors = Doors()
        self.Portal = Portal()

class GameManager():
    def __init__(self, game_screen, start_in_main_menu : bool):
        self.SCREEN = game_screen
        self.INPUT = {"direction": [0, 0], "mouse": (), "m_pos": ()}
        self.INFO = MainInfo()
        self.MENUS = Menus(start_in_main_menu, False)
        self.ENTITIES = Entities()
    def EnterNewRoom(self):
        self.ENTITIES.Player.Pos[0] = 1000 - self.ENTITIES.Player.Pos[0]
        self.ENTITIES.Player.Pos[1] = 750 - self.ENTITIES.Player.Pos[1]
        self.ENTITIES.EnemyBullets = []
        self.ENTITIES.PlayerBullets = []
        self.ENTITIES.Enemies = []
        if self.INFO.CurrentRoom == 10:
            return
        if self.INFO.MiniBoss.Respawn > 0:
            self.INFO.MiniBoss.Respawn -= 1
        elif random.randint(0, 99) < self.INFO.MiniBoss.Chance:
            self.INFO.MiniBoss.Chance += self.INFO.MiniBoss.Rate
        else:
            self.INFO.MiniBoss.Chance = 0
            self.INFO.MiniBoss.Respawn = 3
            # spawn miniboss in center of the room
        # spawn enemies with random pos but 100 pixel away from screen 
    def update(self, events):
        ## Input handle
        self.INPUT["mouse"] = pygame.mouse.get_pressed(3)
        self.INPUT["m_pos"] = pygame.mouse.get_pos()
        for e in events:
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    self.MENUS.IsOptionsMenu = False
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
        if self.MENUS.IsMainMenu or self.MENUS.IsOptionsMenu:
            self.MENUS.Collision(self.INPUT)
        
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
            self.ENTITIES.Player.Reset()
            self.ENTITIES.PlayerBullets = []
            self.ENTITIES.Enemies = []
            self.ENTITIES.EnemyBullets = []
            self.ENTITIES.Boss.Reset()
            self.INFO.MiniBoss.Chance = 0
            self.INFO.MiniBoss.Rate = self.INFO.ProblemsSolved
            self.INFO.MiniBoss.Respawn = 0
        
        ## Game logic
        else:
            b = 0
            while b < len(self.ENTITIES.PlayerBullets):
                self.ENTITIES.PlayerBullets[b]["pos"] += self.ENTITIES.PlayerBullets[b]["dir"]
                if self.ENTITIES.PlayerBullets[b]["pos"][0] * self.ENTITIES.PlayerBullets[b]["pos"][1] < 0 or self.ENTITIES.PlayerBullets[b]["pos"][0] + self.ENTITIES.PlayerBullets[b]["pos"][1] > 1750:
                    self.ENTITIES.PlayerBullets.pop(b)
                    continue
                b += 1
            b = 0
            while b < len(self.ENTITIES.EnemyBullets):
                self.ENTITIES.EnemyBullets[b]["pos"] += self.ENTITIES.EnemyBullets[b]["dir"]
                if self.ENTITIES.EnemyBullets[b]["pos"][0] * self.ENTITIES.EnemyBullets[b]["pos"][1] < 0 or self.ENTITIES.EnemyBullets[b]["pos"][0] + self.ENTITIES.EnemyBullets[b]["pos"][1] > 1750:
                    self.ENTITIES.EnemyBullets.pop(b)
                    continue
                b += 1
            self.ENTITIES.Player.Update(self.INPUT, self.ENTITIES.PlayerBullets, self.ENTITIES.EnemyBullets)
            e = 0
            status = 0
            while e < len(self.ENTITIES.Enemies):
                status = self.ENTITIES.Enemies[e].Update(self.ENTITIES.PlayerBullets, self.ENTITIES.EnemyBullets)
                if status == -1:
                    self.ENTITIES.Enemies.pop(e)
                    continue
                e += 1
            if self.ENTITIES.Boss.State == "alive":
                self.ENTITIES.Boss.Update(self.ENTITIES.PlayerBullets, self.ENTITIES.EnemyBullets)
            if self.ENTITIES.Boss.State == "notspawned" and len(self.ENTITIES.Enemies) == 0:
                status = self.ENTITIES.Button.Update(self.ENTITIES.Player.Pos, self.INPUT, self.INFO.CurrentRoom, self.INFO.Answer, self.INFO.CurrentAnswer)
                if status != -1:
                    self.ENTITIES.Boss.Spawn()
                else:
                    status = self.ENTITIES.Doors.Update(self.ENTITIES.Player.Pos, self.INPUT, self.INFO.CurrentRoom, self.INFO.Rooms)
                    if status != -1:
                        self.INFO.CurrentRoom = status
            if self.ENTITIES.Boss.State == "dead" and len(self.ENTITIES.Enemies) == 0:
                status = self.ENTITIES.Portal.Update(self.ENTITIES.Player.Pos, self.INPUT)
                if status != -1:
                    self.INFO.ProblemsSolved += 1
                    self.INFO.Loaded = False

        ## Rendering
        if not self.MENUS.IsMainMenu:
            # walls (write code here)
            self.ENTITIES.Doors.Render(self.INFO.CurrentRoom, self.INFO.Rooms)
            self.ENTITIES.Button.Render(self.INFO.CurrentRoom)
            self.ENTITIES.Portal.Render(self.ENTITIES.Boss.State == "dead")
            for e in self.ENTITIES.Enemies:
                e.Render()
            if self.ENTITIES.Boss.State == "alive":
                self.ENTITIES.Boss.Render()
            self.ENTITIES.Player.Render()
            # bullet render (write code here)
            for b in self.ENTITIES.PlayerBullets:
                pass
            for b in self.ENTITIES.EnemyBullets:
                pass
        self.MENUS.Render()