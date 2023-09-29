import pygame
from ui.Button import Button

class Menu():
    def __init__(self, screen, buttons, texts):
        self.SCREEN = screen
        self.BUTTONS = buttons
        self.TEXTS = texts
    def collision(self, m_pos):
        for b in self.BUTTONS:
            if b.POS[0] < m_pos and m_pos < b.SIZE[0] + b.POS[0]:
                if b.POS[1] > m_pos and m_pos > b.SIZE[1] + b.POS[1]:
                    b.pressed()
    def render(self):
        for t in self.TEXTS:
            self.SCREEN.blit(t)
        for b in self.BUTTONS:
            b.render()
        