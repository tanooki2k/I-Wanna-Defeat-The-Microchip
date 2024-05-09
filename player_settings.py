from pygame.locals import *

player_speed = 4
initial_speed_dash = 12
acceleration_dash = -0.32
dash_timer = 25
dash_wait_timer = 12

# Player controls:
left = K_LEFT
right = K_RIGHT
jump = K_a
shoot = K_s
dash = K_d


# Player Sprites
class PlayerSprite:
    def __init__(self, sprite):
        if not isinstance(sprite, tuple):
            raise ValueError(f'You tried to use "{sprite.__class__.__name__}" when tuple is required')
        elif len(sprite) != 4:
            raise IndexError(f"You need 4 values for (x1, y1, x2, y2), but you put {len(sprite)}")

        self.sprite = sprite
        self.width = sprite[2] - sprite[0]
        self.height = sprite[3] - sprite[1]


IDLE = PlayerSprite((3, 3, 25, 24))
