import pygame
from text import SysFont
from text import Font


class Title:
    def __init__(self, screen):
        self.title_1 = SysFont("I Wanna Defeat", 'Georgia', [0, 0], 80, (255, 255, 255))
        self.title_2 = SysFont("The Microchip", 'Georgia', [0, 100], 80, (255, 255, 255))
        self.press_enter = Font('Press "Enter"', 'CampanaScript.otf', [0, 200], 40, (255, 255, 255), 1)

        self.texts = [self.title_1, self.title_2, self.press_enter]
        self.game_play_scene = None

    def update(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return self.game_play_scene
        return self

    def draw(self, screen):
        for text in self.texts:
            text.draw(screen)
