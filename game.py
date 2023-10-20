import pygame
import random

import fish
from fish import *
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
fish_graphic = pygame.image.load("assets/images/orange_fish.png").convert()
fish_graphic.set_colorkey((0, 0, 0))

my_fish = fish.Fish(200, 200)
background = screen.copy()
clock = pygame.time.Clock()


def draw_background():
    background.fill(WATER_COLOR)
    # blit sand tiles across the bottom of the screen:
    for i in range(SCREEN_WIDTH // TILE_SIZE):
        background.blit(sand, (TILE_SIZE * i, SCREEN_HEIGHT - TILE_SIZE))
        background.blit(sand_top, (TILE_SIZE * i, SCREEN_HEIGHT - (2 * TILE_SIZE)))

    # randomly place 5 pieces of grass along the bottom of the screen
    for _ in range(5):
        x = random.randint(0, SCREEN_WIDTH)
        # offset the seaweed so it looks better
        y = random.randint(SCREEN_HEIGHT - 3 * TILE_SIZE, SCREEN_HEIGHT) + (0.5 * TILE_SIZE)
        background.blit(seaweed, (x, y))
    # Draw the CHOMP! title
    text = game_font.render("CHOMP!", True, (5, 31, 125))
    text.get_width()
    background.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, SCREEN_HEIGHT // 2))
    pygame.display.flip()


draw_background()

fish_x = 168
fish_y = 168

pygame.display.flip()  # the screen works like stop-motion.
# there is a ping pong buffer where you draw on one and display on the other
while True:  # The loop defines your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                my_fish.moving_left = True
            if event.key == pygame.K_RIGHT:
                my_fish.moving_right = True
            if event.key == pygame.K_UP:
                my_fish.moving_up = True
            if event.key == pygame.K_DOWN:
                my_fish.moving_down = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                my_fish.moving_left = False
            if event.key == pygame.K_RIGHT:
                my_fish.moving_right = False
            if event.key == pygame.K_UP:
                my_fish.moving_up = False
            if event.key == pygame.K_DOWN:
                my_fish.moving_down = False

    my_fish.update()
    screen.blit(background, (0, 0))
    my_fish.draw(screen)
    pygame.display.flip()
    clock.tick(60)
