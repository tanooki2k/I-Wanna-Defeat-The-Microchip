from pygame.locals import *
from sprite import Sprite

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
scale = 2

IDLE1 = Sprite([1, 3, 24, 21], 348)
IDLE2 = Sprite([28, 3, 24, 21], 348)
IDLE3 = Sprite([56, 3, 24, 21], 348)
IDLE4 = Sprite([83, 3, 24, 21], 348)
IDLE = [IDLE1, IDLE2, IDLE3, IDLE4]
IDLE_LEN = len(IDLE)
IDLE_FPS = 6
