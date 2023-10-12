import pygame
import time
pygame.init()

print(f"the quit event in type {pygame.QUIT}")
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Chomp!")
screen.fill((119, 28, 156))
pygame.draw.rect(screen,(100,25,0) , (0, 380, 400, 400) )
pygame.display.flip()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("NO YOU CANNOT ESCAPE MY PYGAME!!!")
        #print(event.type)

