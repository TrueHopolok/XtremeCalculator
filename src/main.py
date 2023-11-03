import pygame
# print(pygame.ver)
from systems.GameManager import GameManager

## Constants
FPS = 60
HEIGHT = 1000
WIDTH = 750
TITLE = "Xtreme Calculator"
ICON = "../img/icon.png"
MUSIC = "../music.mp3"

## Screen init 
pygame.init()
screen = pygame.display.set_mode((HEIGHT, WIDTH))
pygame.display.set_caption(TITLE)
pygame.display.set_icon(pygame.image.load(ICON))

## Cursor
pygame.mouse.set_cursor(*pygame.cursors.broken_x)

## Fonts init
pygame.font.init()
Fps_Font = pygame.font.SysFont('Cascadia Code', 25, False)

## FPS init
clock = pygame.time.Clock()
running = True
delta = 1000/FPS

## Music init
# pygame.mixer.init()
# pygame.mixer.music.load(MUSIC)
# pygame.mixer.music.play(-1)
# pygame.mixer.music.set_volume(0.5)

## Game logic init
game_manager = GameManager(screen, True, True)

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
    status = game_manager.update(events)
    
    ## FPS counter
    if status != -1:
        screen.blit(Fps_Font.render(f"{int(clock.get_fps())}", True, (0, 255, 0)), (975, 5))
    
    ## Screen update
    pygame.display.update()
    delta = clock.tick(FPS)

## Close the game
pygame.quit()