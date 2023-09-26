import pygame

class GameManager():
    def __init__(self):
        pass
    def update(self, events):
        pygame.mouse.get_pressed(3)
        for e in events:
            # e.key == pygame.mouse.get_pressed
            # e.type == pygame.MOUSEBUTTONDOWN
            
            # if e.key
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    print(True)
                if e.key == pygame.K_RIGHT:
                    print("pressed right")
            if e.type == pygame.KEYUP:
                if e.key == pygame.K_RIGHT:
                    print("pressed right")