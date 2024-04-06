import pygame
from text import SysFont
from text import Font


class Title:
    def __init__(self, screen):
        self.title_1 = SysFont("I Wanna Defeat", 'Georgia', 80, (255, 255, 255), [0, 0])
        self.title_2 = SysFont("The Microchip", 'Georgia', 75, (255, 255, 255), [0, 0])
        self.press_enter = Font('Press "Enter"', 'CampanaScript.otf', 70, (255, 255, 255), [0, 0], 1)

        self.gap_1 = 80 - self.title_1.height()
        self.gap_2 = 170 - 80 - self.title_2.height()

        self.title_1.position = [
            (screen.get_width() - self.title_1.width()) / 2,
            (screen.get_height() - self.title_1.height() - self.title_2.height() - self.press_enter.height() - self.gap_1 - self.gap_2) / 2
        ]
        self.title_2.position = [
            (screen.get_width() - self.title_2.width()) / 2,
            self.title_1["y"] + self.title_1.height() + self.gap_1
        ]
        self.press_enter.position = [
            (screen.get_width() - self.press_enter.width()) / 2,
            self.title_2["y"] + self.title_2.height() + self.gap_2
        ]

        self.texts = [self.title_1, self.title_2, self.press_enter]
        self.menu = None

    def update(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return self.menu
        return self

    def draw(self, screen):
        for text in self.texts:
            text.draw(screen)
