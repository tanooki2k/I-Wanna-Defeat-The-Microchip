import pygame

speed = 18


class Bullet:
    def __init__(self, x, y, direction):
        self.x, self.y = x, y
        self.radius = 10
        self.direction = direction

    def width(self):
        return self.radius * 2

    def height(self):
        return self.radius * 2

    def draw(self, screen):
        pygame.draw.circle(screen, (0, 0, 0), [self.x, self.y], self.radius)
        self.x += speed * self.direction

    def destroyed(self, screen):
        if (self.x <= -self.width()) or (self.x >= screen.get_width()):
            return True
        return False
