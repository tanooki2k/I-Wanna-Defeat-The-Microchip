import pygame

speed = 18


class Bullet:
    def __init__(self, x, y, direction):
        self.x, self.y = x, y
        self.radius = 4
        self.thickness = 100
        self.color = (255, 255, 0)
        self.border_color = (0, 0, 0)
        self.border_radius = 1.5
        self.direction = direction

    def update(self):
        self.x += speed * self.direction

    def draw(self, screen):
        pygame.draw.circle(screen, self.border_color, [self.x, self.y], self.radius+self.border_radius)
        pygame.draw.circle(screen, self.color, [self.x, self.y], self.radius)

    def width(self):
        return self.radius * 2

    def height(self):
        return self.radius * 2

    def destroyed(self, screen):
        if (self.x <= -self.width()) or (self.x >= screen.get_width()):
            return True
        return False
