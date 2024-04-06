import pygame
from text import SysFont
from text import Font


class Menu:
    def __init__(self, screen):
        self.title_1 = SysFont("I Wanna Defeat", 'Georgia', int(screen.get_height() * (80 / 700)), (255, 255, 255),
                               [0, 0])
        self.title_2 = SysFont("The Microchip", 'Georgia', int(screen.get_height() * (75 / 700)), (255, 255, 255),
                               [0, 0])
        self.play = Font('Play', 'CampanaScript.otf', int(screen.get_height() * (64 / 700)), (255, 255, 255), [0, 0])
        self.controls = Font('Controls', 'CampanaScript.otf', int(screen.get_height() * (64 / 700)), (255, 255, 255),
                             [0, 0])
        self.arrows = Font(f'>{15 * " "}<', 'CampanaScript.otf', int(screen.get_height() * (64 / 700)), (255, 255, 255),
                           [0, 0])

        self.gap_1 = screen.get_height() * (80 / 700) - self.title_1.height()
        self.gap_2 = screen.get_height() * (145 / 700) - self.title_2.height()
        self.gap_3 = screen.get_height() * (114 / 700) - self.play.height()

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
        self.arrows.position = [
            (screen.get_width() - self.arrows.width()) / 2,
            self.play["y"]
        ]

        self.texts = [self.title_1, self.title_2, self.play, self.controls, self.arrows]
        self.options = 0
        self.title = None
        self.gameplay = None
        self.control = None

    def update(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return self.title
                if event.key == pygame.K_UP:
                    self.options += 1
                if event.key == pygame.K_DOWN:
                    self.options -= 1
                if event.key == pygame.K_RETURN:
                    if self.options % 2:
                        return self.control
                    else:
                        return self.gameplay

        return self

    def draw(self, screen):
        if self.options % 2:
            self.arrows.position[1] = self.controls["y"]
        else:
            self.arrows.position[1] = self.play["y"]
        self.texts = [self.title_1, self.title_2, self.play, self.controls, self.arrows]
        for text in self.texts:
            text.draw(screen)
