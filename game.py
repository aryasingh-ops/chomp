import pygame

pygame.init()
# let's define variables that make the code scale better/ get rid of teal:
TILE_SIZE = 64  # tiles are square height == width

SCREEN_WIDTH = 8 * TILE_SIZE
SCREEN_HEIGHT = 8 * TILE_SIZE
SAND_HEIGHT = 20

WATER_COLOR = (114, 159, 232)
SAND_COLOR = (100, 25, 0)

print(f"the quit event in type {pygame.QUIT}")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Chomp!")
screen.fill(WATER_COLOR)
pygame.draw.rect(screen, SAND_COLOR,
                 (0, SCREEN_HEIGHT - SAND_HEIGHT, SCREEN_WIDTH, SAND_HEIGHT))  # anchor point, height, width
sand = pygame.image.load("assets/images/sand.png").convert()  # load the image then blit it to the screen

# blit sand tiles across the bottom of the screen:

for i in range(SCREEN_WIDTH // TILE_SIZE):
    screen.blit(sand, (TILE_SIZE * i, SCREEN_HEIGHT-(2*TILE_SIZE)))

screen.blit(sand, (SCREEN_WIDTH // 2 - TILE_SIZE // 2,
                   SCREEN_HEIGHT // 2 - TILE_SIZE // 2))

pygame.display.flip()  # the screen works like stop-motion.
# there is a ping pong buffer where you draw on one and display on the other
while True:  # The loop defines your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # print("NO YOU CANNOT ESCAPE MY PYGAME!!!")
            print("thanks for playing!")
            pygame.quit()

        # print(event.type)
