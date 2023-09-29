import pygame

class Button():
    def __init__(self, screen, pos, size, img, text):
        self.SCREEN = screen
        self.POS = pos
        self.SIZE = size
        self.IMG = img
        self.TEXT = text
    def pressed():
        pass
    def render():
        self.SCREEN.blit(img, self.POS)
        self.SCREEN.blit(text, self.POS)