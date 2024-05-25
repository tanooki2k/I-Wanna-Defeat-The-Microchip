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
IDLE1 = Sprite([0, 3, 25, 21], 348, IDLE_FPS+1, scale)
IDLE2 = Sprite([27, 3, 25, 21], 348, IDLE_FPS, scale)
IDLE3 = Sprite([55, 3, 25, 21], 348, IDLE_FPS, scale)
IDLE4 = Sprite([82, 3, 25, 21], 348, IDLE_FPS+1, scale)
IDLE = [IDLE1, IDLE2, IDLE3, IDLE4]
IDLE_LEN = len(IDLE)

WALK_FPS = 5
WALK1 = Sprite([1, 29, 25, 21], 348, WALK_FPS, scale)
WALK2 = Sprite([31, 29, 25, 21], 348, WALK_FPS-1, scale)
WALK3 = Sprite([59, 29, 25, 21], 348, WALK_FPS-1, scale)
WALK4 = Sprite([87, 29, 25, 21], 348, WALK_FPS, scale)
WALK5 = Sprite([118, 29, 25, 21], 348, WALK_FPS-1, scale)
WALK = [WALK1, WALK2, WALK3, WALK4, WALK5]
WALK_LEN = len(WALK)

JUMP1 = Sprite([2, 70, 25, 23], 348, scale=scale)
JUMP2 = Sprite([31, 70, 25, 23], 348, scale=scale)

FALL1 = Sprite([4, 102, 25, 21], 348, scale=scale)
FALL2 = Sprite([31, 102, 25, 21], 348, scale=scale)
