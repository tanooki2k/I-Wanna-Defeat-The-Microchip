import pygame


class Title:
    def __init__(self, screen):
        self.game_play_scene = None

    def update(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return self.game_play_scene
        return self

    def draw(self, screen):
        screen.blit(self.title, self.position)
