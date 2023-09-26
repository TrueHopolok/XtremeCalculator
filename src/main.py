import pygame
# print(pygame.ver)
from systems.GameManager import GameManager

## Constants
FPS = 60
HEIGHT = 1000
WIDTH = 800
TITLE = "Xtreme Calculator"
# ICON = ""

## Screen init 
pygame.init()
screen = pygame.display.set_mode((HEIGHT, WIDTH))
pygame.display.set_caption(TITLE)
# pygame.display.set_icon(pygame.image.load(ICON))

## Cursor
pygame.mouse.set_cursor(*pygame.cursors.broken_x)

## Fonts init
pygame.font.init()
Fps_Font = pygame.font.SysFont('Cascadia Code', 25)

## FPS init
clock = pygame.time.Clock()
running = True
delta = 1000/FPS

## Game logic init
game_manager = GameManager()

## Load saved settings
#! TODO

## Load saved run
#! TODO

## Game loop
while running:
    
    ## Events handle
    events = pygame.event.get()
    for e in events:
        if e.type == pygame.QUIT:
            running = False
            break
        
    ## reset screen (set black background)
    screen.fill((0, 0, 0))
    
    ## Game logic and render update
    game_manager.update(events)
    
    ## FPS counter
    screen.blit(Fps_Font.render(f"{int(clock.get_fps())}", True, (0, 255, 0)), (5, 5))
    
    ## Screen update
    pygame.display.update()
    delta = clock.tick(FPS)

## Close the game
pygame.quit()