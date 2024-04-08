import pygame
import settings
from pygame.locals import *


class Player:
    def __init__(self, x, y):
        self.width, self.height = 50, 50
        self.x, self.y = x, y
        self.initial_y = y
        self.jump_speed = 0
        self.is_jump = False

    def width(self):
        return self.width

    def height(self):
        return self.height

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[K_RIGHT] and (self.x < settings.screen_width - self.width / 2):
            self.x += 4
        if keys[K_LEFT] and (self.x > -self.width / 2):
            self.x -= 4
        if keys[K_UP] and not self.is_jump:
            self.jump_speed = 12
            self.is_jump = True

    def draw(self, screen):
        if self.is_jump:
            self.y -= self.jump_speed
            self.jump_speed -= settings.gravity
            if self.y >= self.initial_y:
                self.is_jump, self.y = False, self.initial_y
        pygame.draw.rect(screen, (255, 0, 0), [self.x, self.y, self.width, self.height])
