import pygame
from ui.Menu import Menu
from ui.StartButton import StartButton

class MainMenu(Menu):
    def __init__(self, screen):
        self.SCREEN = screen
        buttons = []
        texts = []
        # BUTTON = StartButton()
        # TEXT = font.render("Vadims Truhanovs, 11.a", True, (0, 60, 60)), (10, SCREEN_HEIGHT - FONT_REGULAR_SIZE - 10)
        # IMG = pygame.transform.scale(pygame.image.load(""), (SCREEN_WIDTH, SCREEN_HEIGHT))
        # Screen.blit
        super(MainMenu, self).__init__(screen, buttons, texts)
    def collision(self, m_pos):
        super(MainMenu, self).collision(m_pos)
    def render(self):
        super(MainMenu, self).render()