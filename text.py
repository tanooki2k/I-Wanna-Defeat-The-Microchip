import pygame


class Text:
    """
    Defining a "Text"
    """

    def __init__(self, font, text, color, position, animate):
        self.font = font

        if len(color) != 3:
            raise IndexError(f"You need just 3 values for (red, green, blue), but you put {len(position)}")
        self.content = self.font.render(text, True, color)

        if not isinstance(position, list):
            raise ValueError(f'You tried to use "{position.__class__.__name__}" when list is required')
        elif len(position) != 2:
            raise IndexError(f"You need just 2 values for (x, y), but you put {len(position)}")
        self.position = position
        self.index = {
            "x": 0,
            "y": 1
        }

        self.define_animation = {
            "0": True,
            "1": Text.animate_1
        }
        self.animate = self.define_animation[str(animate)]
        self.blit = True
        self.counter = 0
        self.timer = 5

    def __getitem__(self, item):
        return self.position[self.index[item]]

    def width(self):
        return self.content.get_width()

    def height(self):
        return self.content.get_height()

    def draw(self, screen):
        self.blit = True
        if not isinstance(self.animate, bool):
            self.blit = self.animate(self)
        if self.blit and self.animate:
            screen.blit(self.content, self.position)

    # Methods for animate text
    def animate_1(self):
        self.counter += 1
        if self.counter == self.timer * 2:
            self.counter = 0
        if self.counter >= self.timer:
            return False
        return True


class SysFont(Text):
    """
    For calling Fonts in Python's defaults fonts
    """

    def __init__(self, text, font, size, color, position, animate=0):
        super().__init__(pygame.font.SysFont(font, size), text, color, position, animate)


class Font(Text):
    """
    For calling external Fonts
    """

    def __init__(self, text, font, size, color, position, animate=0):
        super().__init__(pygame.font.Font(f'fonts/{font}', size), text, color, position, animate)
