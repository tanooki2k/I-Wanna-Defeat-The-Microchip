import pygame


class Background:
    def __init__(self, image, position):
        self.image = pygame.image.load(f'image/{image}').convert_alpha()

        if not isinstance(position, list):
            raise ValueError(f'You tried to use "{position.__class__.__name__}" when list is required')
        elif len(position) != 2:
            raise IndexError(f"You need just 2 values for (x, y), but you put {len(position)}")

        self.pos = position

    def draw(self, screen):
        screen.blit(self.image, self.pos)
