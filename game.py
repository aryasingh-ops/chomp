import pygame
import random

from settings import *

pygame.init()

game_font = pygame.font.Font("assets/fonts/Ocean Coastlines.otf", 128)

print(f"the quit event in type {pygame.QUIT}")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Chomp!")
screen.fill(WATER_COLOR)

sand = pygame.image.load("assets/images/sand.png").convert()  # load the image then blit it to the screen
sand_top = pygame.image.load("assets/images/sand_top.png").convert()
sand_top.set_colorkey((0, 0, 0))
seaweed = pygame.image.load("assets/images/seagrass.png").convert()
seaweed.set_colorkey((0, 0, 0))
# blit sand tiles across the bottom of the screen:
for i in range(SCREEN_WIDTH // TILE_SIZE):
    screen.blit(sand, (TILE_SIZE * i, SCREEN_HEIGHT - TILE_SIZE))
    screen.blit(sand_top, (TILE_SIZE * i, SCREEN_HEIGHT - (2 * TILE_SIZE)))

# randomly place 5 pieces of grass along the bottom of the screen
for _ in range(5):
    x = random.randint(0, SCREEN_WIDTH)
    # offset the seaweed so it looks better
    y = random.randint(SCREEN_HEIGHT - 3 * TILE_SIZE, SCREEN_HEIGHT) + (0.5 * TILE_SIZE)
    screen.blit(seaweed, (x, y))
# Draw the CHOMP! title
text = game_font.render("CHOMP!", True, (5, 31, 125))
text.get_width()
screen.blit(text, (SCREEN_WIDTH//2-text.get_width()//2, SCREEN_HEIGHT//2))

pygame.display.flip()  # the screen works like stop-motion.
# there is a ping pong buffer where you draw on one and display on the other
while True:  # The loop defines your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # print("NO YOU CANNOT ESCAPE MY PYGAME!!!")
            print("thanks for playing!")
            pygame.quit()

        # print(event.type)
