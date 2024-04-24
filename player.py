import pygame

import player_settings
import settings
from pygame.locals import *
from enum import Enum
from bullet import Bullet


class JumpStates(Enum):
    NO_JUMP = 0
    JUMP_PRESSED = 1
    JUMP_RELEASED = 2
    DOUBLE_JUMP_PRESSED = 3
    DOUBLE_JUMP_RELEASED = 4


class Shoot(Enum):
    NO_SHOOT = 0
    SHOT = 1


class Dash(Enum):
    NO_DASH = 0
    DASH = 1
    NO_MOVE = 2


class Player:
    def __init__(self, x, y):
        self.width, self.height = 50, 50
        self.x, self.y = x, y
        self.initial_y = y
        self.jump_speed = 0
        self.is_jump = False
        self.is_double_jump = False
        self.double_jump_ready = JumpStates.NO_JUMP
        self.direction = 1

        self.bullets = []
        self.shoot = Shoot.NO_SHOOT
        self.destroyed_bullets = []

        self.dash = Dash.NO_DASH
        self.speed_dash = player_settings.speed_dash
        self.dash_time = 0

    def width(self):
        return self.width

    def height(self):
        return self.height

    def update(self):
        keys = pygame.key.get_pressed()
        if self.dash != Dash.NO_MOVE:
            if keys[K_RIGHT] or keys[K_LEFT]:
                if keys[K_RIGHT] and (self.x < settings.screen_width - self.width / 2):
                    self.direction = 1
                if keys[K_LEFT] and (self.x > -self.width / 2):
                    self.direction = -1
                self.x += player_settings.player_speed * self.direction

            if keys[K_UP]:
                if not self.is_jump:
                    self.do_jump()
                elif self.can_double_jump():
                    self.do_double_jump()
            self.process_jump_ready(keys)

            if keys[K_s] and (self.shoot == Shoot.NO_SHOOT):
                self.create_a_bullet()
                self.shoot = Shoot.SHOT
            self.process_shoot_ready(keys)

            if keys[K_d] and (self.dash == Dash.NO_DASH):
                self.dash = Dash.NO_MOVE
                self.jump_speed = 0
                self.dash_time = 0

        if self.dash == Dash.NO_MOVE:
            self.dash_time += 1
            self.x += self.speed_dash * self.direction
            if self.dash_time == player_settings.dash_timer:
                self.dash = Dash.DASH

        if not keys[K_d]:
            if self.dash == Dash.DASH:
                self.dash = Dash.NO_DASH

        self.check_not_out_screen()

    def check_not_out_screen(self):
        if not self.x < settings.screen_width - self.width / 2:
            self.x = settings.screen_width - self.width / 2
        if not self.x > -self.width / 2:
            self.x = -self.width / 2

    def process_shoot_ready(self, keys):
        if not keys[K_s]:
            if self.shoot == Shoot.SHOT:
                self.shoot = Shoot.NO_SHOOT

    def create_a_bullet(self):
        initial_x = self.x if self.direction == -1 else self.x + self.width
        self.bullets.append(Bullet(initial_x, self.y + self.height / 2, self.direction))

    def can_double_jump(self):
        return not self.is_double_jump and self.double_jump_ready == JumpStates.JUMP_RELEASED

    def do_jump(self):
        self.jump_speed = 12
        self.is_jump = True
        self.double_jump_ready = JumpStates.JUMP_PRESSED

    def do_double_jump(self):
        self.jump_speed = 12
        self.is_double_jump = True
        self.double_jump_ready = JumpStates.DOUBLE_JUMP_PRESSED

    def process_jump_ready(self, keys):
        if not keys[K_UP]:
            if self.double_jump_ready == JumpStates.JUMP_PRESSED:
                self.double_jump_ready = JumpStates.JUMP_RELEASED
            if self.double_jump_ready == JumpStates.DOUBLE_JUMP_PRESSED:
                self.double_jump_ready = JumpStates.DOUBLE_JUMP_RELEASED

    def draw(self, screen):
        # Draw the bullets
        self.destroyed_bullets = []
        for bullet in self.bullets:
            bullet.draw(screen)
            if bullet.destroyed(screen):
                self.destroyed_bullets.append(bullet)

        for bullet_destroyed in self.destroyed_bullets:
            self.bullets.remove(bullet_destroyed)

        # Draw the player
        if self.is_jump:
            if self.dash != Dash.NO_MOVE:
                reduce_jump = self.height_of_jump()
                self.y -= self.jump_speed * reduce_jump
                self.jump_speed -= settings.gravity
            if self.y >= self.initial_y:
                self.is_jump, self.is_double_jump = False, False
                self.y, self.double_jump_ready = self.initial_y, 0
        pygame.draw.rect(screen, (255, 0, 0), [self.x, self.y, self.width, self.height])

    def height_of_jump(self):
        reduce_jump = 1
        if self.jump_speed > 0 and (
                self.double_jump_ready == JumpStates.JUMP_RELEASED or self.double_jump_ready == JumpStates.DOUBLE_JUMP_RELEASED):
            reduce_jump = 0.5
        return reduce_jump
