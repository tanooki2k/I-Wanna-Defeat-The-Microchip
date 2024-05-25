import pygame


class Background:
    def __init__(self, image, position, scale_x=1, scale_y=1):
        self.image = pygame.image.load(f'image/{image}')
        self.scaled = pygame.transform.scale(self.image,
                                             (self.image.get_width() * scale_x, self.image.get_height() * scale_y))

        if not isinstance(position, list):
            raise ValueError(f'You tried to use "{position.__class__.__name__}" when list is required')
        elif len(position) != 2:
            raise IndexError(f"You need just 2 values for (x, y), but you put {len(position)}")

        self.x, self.y = position

    def draw(self, screen):
        screen.blit(self.scaled, [self.x, self.y])
