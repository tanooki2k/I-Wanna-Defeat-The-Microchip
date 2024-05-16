import pygame
import player_settings
from enum import Enum


class AnimationStates(Enum):
    IDLE = 0
    WALK = 1
    JUMP = 2
    FALL = 3


class PlayerAnimation:
    def __init__(self):
        self.image = pygame.image.load('image/player.png')
        self.sprite_sheet = pygame.transform.scale(self.image, (
            self.image.get_width() * player_settings.scale, self.image.get_height() * player_settings.scale))
        self.sprite_sheet_rev = pygame.transform.flip(self.sprite_sheet, True, False)
        self.index = 0
        self.counter = 0
        self.animation = AnimationStates.IDLE
        self.sprite = player_settings.IDLE[0]

        self.direction = 1

    def update(self):
        if self.animation == AnimationStates.IDLE:
            self.sprite = player_settings.IDLE[self.index]
            self.counter += 1
            if self.counter == player_settings.IDLE_FPS:
                self.counter = 0
                self.index += 1
                
                if self.index == player_settings.IDLE_LEN:
                    self.index = 0
