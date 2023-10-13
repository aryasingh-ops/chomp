import pygame
import time
pygame.init()

print(f"the quit event in type {pygame.QUIT}")
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Chomp!")
screen.fill((119, 28, 156))
pygame.draw.rect(screen,(100,25,0) , (0, 380, 400, 400) ) #anchor point, height, width
pygame.display.flip() #the screen works like stop-motion. there is a ping pong buffer where you draw on one and display on the other
while True: #The loop defines your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           # print("NO YOU CANNOT ESCAPE MY PYGAME!!!")
            print("thanks for playing!")
            pygame.quit()
            sys.exit()
        #print(event.type)
