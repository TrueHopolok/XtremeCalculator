import pygame

class Button():
    def __init__(self, screen, pos, size, img, text):
        self.SCREEN = screen
        self.POS = pos
        self.SIZE = size
        self.IMG = img
        self.TEXT = text
    def pressed(self):
        pass
    def render(self):
        self.SCREEN.blit(img, self.POS)
        self.SCREEN.blit(text, self.POS)