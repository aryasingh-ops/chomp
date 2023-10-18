import pygame
import time

# let's define variables that make the code scale better/ get rid of teal:
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
SAND_HEIGHT = 20
TILE_SIZE = 64  # tiles are square height == width
pygame.init()

WATER_COLOR = (114, 159, 232)
SAND_COLOR = (100, 25, 0)

print(f"the quit event in type {pygame.QUIT}")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Chomp!")
screen.fill(WATER_COLOR)
pygame.draw.rect(screen, SAND_COLOR,
                 (0, SCREEN_HEIGHT - SAND_HEIGHT, SCREEN_WIDTH, SAND_HEIGHT))  # anchor point, height, width
sand = pygame.image.load("assets/images/sand.png").convert()  # load the image then blit it to the screen
# screen.blit(sand,(200,200,64,64))
screen.blit(sand, (200 - 32, 200 - 32))  # (0,0) is top left
pygame.display.flip()  # the screen works like stop-motion.
# there is a ping pong buffer where you draw on one and display on the other
while True:  # The loop defines your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # print("NO YOU CANNOT ESCAPE MY PYGAME!!!")
            print("thanks for playing!")
            pygame.quit()

        # print(event.type)
