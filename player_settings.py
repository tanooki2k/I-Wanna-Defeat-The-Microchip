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

IDLE_FPS = 5
IDLE1 = Sprite([0, 3, 25, 21], 348, IDLE_FPS+1)
IDLE2 = Sprite([27, 3, 25, 21], 348, IDLE_FPS)
IDLE3 = Sprite([55, 3, 25, 21], 348, IDLE_FPS)
IDLE4 = Sprite([82, 3, 25, 21], 348, IDLE_FPS+1)
IDLE = [IDLE1, IDLE2, IDLE3, IDLE4]
IDLE_LEN = len(IDLE)

WALK_FPS = 5
WALK1 = Sprite([1, 29, 25, 21], 348, WALK_FPS)
WALK2 = Sprite([31, 29, 25, 21], 348, WALK_FPS)
WALK3 = Sprite([59, 29, 25, 21], 348, WALK_FPS-1)
WALK4 = Sprite([87, 29, 25, 21], 348, WALK_FPS)
WALK5 = Sprite([118, 29, 25, 21], 348, WALK_FPS-1)
WALK = [WALK1, WALK2, WALK3, WALK4, WALK5]
WALK_LEN = len(WALK)
