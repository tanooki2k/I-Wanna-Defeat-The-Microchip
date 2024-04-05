import pygame


class Text:
    def __init__(self, text, font, position, size, color, gap=False):
        self.font = pygame.font.SysFont(font, size)

        self.title = self.font.render(text, True, color)
        self.gap = gap

        if not isinstance(position, list):
            raise ValueError(f"You tried to use {position.__class__.__name__} when list is required")
        elif len(position) != 2:
            raise IndexError(f"You need just 2 values for (x, y), but you put {len(position)}")
        self.position = position
