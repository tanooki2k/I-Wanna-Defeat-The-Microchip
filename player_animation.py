import pygame
import player_settings


class PlayerAnimation:
    def __init__(self):
        self.image = pygame.image.load('image/player.png')
        self.sprite_sheet = pygame.transform.scale(self.image, (
            self.image.get_width() * player_settings.scale, self.image.get_height() * player_settings.scale))
        self.index = 0
        self.sprite = player_settings.IDLE1
