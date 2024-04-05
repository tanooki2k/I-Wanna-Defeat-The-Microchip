import pygame


class Title:
    def __init__(self, screen):
        self.font1 = pygame.font.SysFont('Comic Sans', 100)
        self.font2 = pygame.font.SysFont('Comic Sans', 80)

        self.title1 = self.font1.render("I Wanna Defeat", True, (255, 255, 255))
        self.title2 = self.font2.render("The Microchip", True, (255, 255, 255))
        self.gap1 = 100

        self.title1_position = ((screen.get_width() - self.title1.get_width()) / 2,
                                (screen.get_height() - self.title1.get_height() - self.gap1) / 2)
        self.title2_position = ((screen.get_width() - self.title2.get_width()) / 2,
                                (screen.get_height() - self.title2.get_height() + self.gap1) / 2)

        self.game_play_scene = None

    def update(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return self.game_play_scene
        return self

    def draw(self, screen):
        screen.blit(self.title1, self.title1_position)
        screen.blit(self.title2, self.title2_position)
