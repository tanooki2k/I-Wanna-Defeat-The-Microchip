import pygame
from pygame.locals import *


class Player:
    def __init__(self, x, y):
        self.width, self.height = 50, 50
        self.x, self.y = x, y

    def update(self, events):
        keys = pygame.key.get_pressed()
        if keys[K_RIGHT]:
            self.x += 10
        if keys[K_LEFT]:
            self.x -= 10

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), [self.x, self.y, self.width, self.height])
