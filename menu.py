import pygame
from text import SysFont
from text import Font


class Menu:
    def __init__(self, screen):
        self.title_1 = SysFont("I Wanna Defeat", 'Georgia', 80, (255, 255, 255), [0, 0])
        self.title_2 = SysFont("The Microchip", 'Georgia', 75, (255, 255, 255), [0, 0])
        self.play = Font('Play', 'CampanaScript.otf', 64, (255, 255, 255), [0, 0])
        self.controls = Font('Controls', 'CampanaScript.otf', 64, (255, 255, 255), [0, 0])

        self.gap_1 = 80 - self.title_1.height()
        self.gap_2 = 70
        self.gap_3 = 50

        self.title_1.position = [
            (screen.get_width() - self.title_1.width()) / 2,
            (
                    screen.get_height() - self.title_1.height() - self.title_2.height() - self.play.height() - self.controls.height() - self.gap_1 - self.gap_2 - self.gap_3) / 2
        ]
        self.title_2.position = [
            (screen.get_width() - self.title_2.width()) / 2,
            self.title_1["y"] + self.title_1.height() + self.gap_1
        ]
        self.play.position = [
            (screen.get_width() - self.controls.width()) / 2,
            self.title_2["y"] + self.title_2.height() + self.gap_2
        ]
        self.controls.position = [
            (screen.get_width() - self.controls.width()) / 2,
            self.play["y"] + self.play.height() + self.gap_3
        ]

        self.texts = [self.title_1, self.title_2, self.play, self.controls]
        self.title = None

    def update(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return self.title
        return self

    def draw(self, screen):
        for text in self.texts:
            text.draw(screen)
