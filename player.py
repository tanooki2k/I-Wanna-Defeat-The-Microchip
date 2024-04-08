import pygame
import settings
from pygame.locals import *

NO_JUMP = 0
JUMP_PRESSED = 1
JUMP_RELEASED = 2
DOUBLE_JUMP_PRESSED = 3
DOUBLE_JUMP_RELEASED = 4

class Player:
    def __init__(self, x, y):
        self.width, self.height = 50, 50
        self.x, self.y = x, y
        self.initial_y = y
        self.jump_speed = 0
        self.is_jump = False
        self.is_double_jump = False
        self.double_jump_ready = NO_JUMP

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

        if keys[K_UP]:
            if not self.is_jump:
                self.do_jump()
            elif self.can_double_jump():
                self.do_double_jump()

        self.process_jump_ready(keys)

    def can_double_jump(self):
        return not self.is_double_jump and self.double_jump_ready == JUMP_RELEASED

    def do_jump(self):
        self.jump_speed = 12
        self.is_jump = True
        self.double_jump_ready = JUMP_PRESSED

    def do_double_jump(self):
        self.jump_speed = 12
        self.is_double_jump = True
        self.double_jump_ready = DOUBLE_JUMP_PRESSED

    def process_jump_ready(self, keys):
        if not keys[K_UP]:
            if self.double_jump_ready == JUMP_PRESSED:
                self.double_jump_ready = JUMP_RELEASED
            if self.double_jump_ready == DOUBLE_JUMP_PRESSED:
                self.double_jump_ready = DOUBLE_JUMP_RELEASED

    def draw(self, screen):
        if self.is_jump:
            reduce_jump = 1
            if self.jump_speed > 0 and (self.double_jump_ready == JUMP_RELEASED or self.double_jump_ready == DOUBLE_JUMP_RELEASED):
                reduce_jump = 0.5
            self.y -= self.jump_speed * reduce_jump
            self.jump_speed -= settings.gravity
            if self.y >= self.initial_y:
                self.is_jump, self.is_double_jump = False, False
                self.y, self.double_jump_ready = self.initial_y, 0
        pygame.draw.rect(screen, (255, 0, 0), [self.x, self.y, self.width, self.height])
