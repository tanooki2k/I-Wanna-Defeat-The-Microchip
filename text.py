import pygame


class Text:
    def __init__(self, position, animate):
        if not isinstance(position, list):
            raise ValueError(f'You tried to use "{position.__class__.__name__}" when list is required')
        elif len(position) != 2:
            raise IndexError(f"You need just 2 values for (x, y), but you put {len(position)}")
        self.position = position

        self.animation = animate
        self.counter = 0
        self.timer = 4

    def draw(self, screen):
        if self.animation:
            self.counter += 1
            if self.counter == self.timer * 2:
                self.counter = 0
            if self.counter >= self.timer:
                return
        screen.blit(self.content, self.position)


class SysFont(Text):
    def __init__(self, text, font, position, size, color, animate=0):
        super().__init__(position, animate)
        self.font = pygame.font.SysFont(font, size)

        if len(color) != 3:
            raise IndexError(f"You need just 3 values for (red, green, blue), but you put {len(position)}")
        self.content = self.font.render(text, True, color)


class Font(Text):
    def __init__(self, text, font, position, size, color, animate=0):
        super().__init__(position, animate)
        self.font = pygame.font.Font(f'fonts/{font}', size)

        if len(color) != 3:
            raise IndexError(f"You need just 3 values for (red, green, blue), but you put {len(position)}")
        self.content = self.font.render(text, True, color)
