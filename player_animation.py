import pygame
import player_settings
from enum import Enum


class AnimationStates(Enum):
    IDLE = 0
    WALK = 1
    JUMP1 = 2
    JUMP2 = 3
    FALL1 = 4
    FALL2 = 5


class PlayerAnimation:
    def __init__(self):
        self.image = pygame.image.load('image/player.png')
        self.sprite_sheet = pygame.transform.scale(self.image, (
            self.image.get_width() * player_settings.scale, self.image.get_height() * player_settings.scale))
        self.sprite_sheet_rev = pygame.transform.flip(self.sprite_sheet, True, False)

        self.index = 0
        self.counter = 0
        # self.animation = AnimationStates.IDLE
        self.animation = AnimationStates.WALK
        self.prev_animation = self.animation
        self.sprite = player_settings.IDLE[0]

        self.direction = 1

    def update(self):
        if self.prev_animation != self.animation:
            self.index = 0
            self.counter = 0

        self.idle_animation()
        self.walk_animation()
        self.jump_animation()
        self.fall_animation()

        self.prev_animation = self.animation

    def fall_animation(self):
        if self.animation == AnimationStates.FALL1:
            self.sprite = player_settings.FALL1
        if self.animation == AnimationStates.FALL2:
            self.sprite = player_settings.FALL2

    def jump_animation(self):
        if self.animation == AnimationStates.JUMP1:
            self.sprite = player_settings.JUMP1
        if self.animation == AnimationStates.JUMP2:
            self.sprite = player_settings.JUMP2

    def idle_animation(self):
        if self.animation == AnimationStates.IDLE:
            self.sprite = player_settings.IDLE[self.index]
            self.counter += 1
            if self.counter == player_settings.IDLE[self.index].FPS:
                self.counter = 0
                self.index += 1

                if self.index == player_settings.IDLE_LEN:
                    self.index = 0

    def walk_animation(self):
        if self.animation == AnimationStates.WALK:
            self.sprite = player_settings.WALK[self.index]
            self.counter += 1
            if self.counter == player_settings.WALK[self.index].FPS:
                self.counter = 0
                self.index += 1

                if self.index == player_settings.WALK_LEN:
                    self.index = 0
