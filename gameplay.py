import pygame, settings
from player import Player
from text import Font


class Gameplay:
    def __init__(self, screen):
        self.player = Player(200, 558)

        self.pause = Font('Pause', 'CampanaScript.otf', int(screen.get_height() * (100 / 700)), (0, 0, 0), [0, 0])
        self.pause.position = [
            (screen.get_width() - self.pause.width()) / 2,
            (screen.get_height() - self.pause.height()) / 2
        ]

        self.is_pause = 0
        self.texts = [self.pause]
        self.menu = None

    def update(self, events):
        if not self.is_pause % 2:
            self.player.update()

        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.is_pause += 1
        return self

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), [0, 0, screen.get_width(), screen.get_height()])
        pygame.draw.rect(screen, (0, 0, 0), [0, 600, screen.get_width(), 100])
        pygame.draw.rect(screen, settings.floor_color, [0, 605, screen.get_width(), 100])
        self.player.draw(screen)
        if self.is_pause % 2:
            for text in self.texts:
                text.draw(screen)
            return 0
