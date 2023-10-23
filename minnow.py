import pygame
from settings import *
import fish


class Minnow(pygame.sprite.Sprite):
    def __init__(self, x, y):

        self.right_image = pygame.image.load("assets/images/purple_minnow.png")
        self.right_image.set_colorkey((0, 0, 0))
        self.image = self.right_image
        self.left_image = pygame.transform.flip(self.image, True, False)
        self.rect = pygame.rect.Rect(x, y, self.image.get_width(), self.image.get_height())
        self.moving_left = False
        self.moving_right = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        if self.moving_left:
            self.rect.x -= 10
            self.image = self.left_image

        elif self.moving_right:
            self.rect.x += 10
            self.image = self.right_image

        elif self.moving_up:
            self.rect.y -= 10

        elif self.moving_down:
            self.rect.y += 10

        if self.rect.left < 0:
            self.rect.x = 0
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.bottom > SCREEN_HEIGHT - 2 * TILE_SIZE:
            self.rect.bottom = SCREEN_HEIGHT - 2 * TILE_SIZE

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))