import settings
from bullet import Bullet
from player_animation import *


class JumpStates(Enum):
    NO_JUMP = 0
    JUMP_PRESSED = 1
    JUMP_RELEASED = 2
    DOUBLE_JUMP_PRESSED = 3
    DOUBLE_JUMP_RELEASED = 4


class Shoot(Enum):
    NO_SHOOT = 0
    SHOT = 1


class Dash(Enum):
    NO_DASH = 0
    WAITING = 1
    IN_AIR = 2
    NO_MOVE = 3


class Player(PlayerAnimation):
    def __init__(self, x, y):
        super().__init__()

        self.x, self.y = x, y
        self.initial_y = y
        self.jump_speed = 14
        self.initial_jump = 14
        self.is_jump = False
        self.is_double_jump = False
        self.double_jump_ready = JumpStates.NO_JUMP

        self.bullets = []
        self.shoot = Shoot.NO_SHOOT
        self.destroyed_bullets = []

        self.dash = Dash.NO_DASH
        self.speed_dash = player_settings.initial_speed_dash
        self.dash_time = 0

        self.out_right = -12 * player_settings.scale
        self.out_left = -11 * player_settings.scale

    def width(self):
        return self.sprite.width

    def height(self):
        return self.sprite.height

    def update(self):
        # Update the bullets
        for bullet in self.bullets:
            bullet.update()

        # Update Player
        keys = pygame.key.get_pressed()
        if self.dash != Dash.NO_MOVE:
            if keys[player_settings.right] or keys[player_settings.left]:
                if keys[player_settings.right] and (self.x < settings.screen_width + self.out_right):
                    self.direction = 1
                if keys[player_settings.left] and (self.x > self.out_left):
                    self.direction = -1
                self.x += player_settings.player_speed * self.direction
                self.animation = AnimationStates.WALK
            elif self.y == self.initial_y:
                self.animation = AnimationStates.IDLE

            if self.y != self.initial_y:
                if 7 <= self.jump_speed < 14:
                    self.animation = AnimationStates.JUMP1
                elif 0 <= self.jump_speed < 7:
                    self.animation = AnimationStates.JUMP2
                elif (self.jump_speed < 0) and (self.initial_y - self.y) > 40:
                    self.animation = AnimationStates.FALL1
                else:
                    self.animation = AnimationStates.FALL2

            if keys[player_settings.jump]:
                if not self.is_jump:
                    self.do_jump()
                elif self.can_double_jump():
                    self.do_double_jump()
            self.process_jump_ready(keys)

            if keys[player_settings.dash] and (self.dash == Dash.NO_DASH):
                self.dash = Dash.NO_MOVE
                self.animation = AnimationStates.WALK
                self.jump_speed = 0
                self.speed_dash = player_settings.initial_speed_dash
                self.dash_time = 0

        if self.dash == Dash.NO_MOVE:
            self.dash_time += 1
            self.x += self.speed_dash * self.direction
            self.speed_dash += player_settings.acceleration_dash
            if self.dash_time == player_settings.dash_timer:
                if self.double_jump_ready == JumpStates.NO_JUMP:
                    self.dash = Dash.WAITING
                else:
                    self.dash = Dash.IN_AIR
                self.dash_time = 0

        if keys[player_settings.shoot] and (self.shoot == Shoot.NO_SHOOT):
            self.create_a_bullet()
            self.shoot = Shoot.SHOT
        self.process_shoot_ready(keys)

        if (self.dash == Dash.WAITING) or (self.dash == Dash.IN_AIR):
            self.dash_time += 1
            if self.y == self.initial_y:
                self.dash = Dash.WAITING
            if (self.dash == Dash.WAITING) and (self.dash_time >= player_settings.dash_wait_timer):
                if not keys[player_settings.dash]:
                    self.dash = Dash.NO_DASH

        self.check_not_out_screen()
        self.y_motion()
        super().update()

    def draw(self, screen):
        # Draw the bullets
        self.destroyed_bullets = []
        for bullet in self.bullets:
            bullet.draw(screen)
            if bullet.destroyed(screen):
                self.destroyed_bullets.append(bullet)

        for bullet_destroyed in self.destroyed_bullets:
            self.bullets.remove(bullet_destroyed)

        # Draw the player
        if self.direction == 1:
            screen.blit(self.sprite_sheet, [self.x, self.y], self.sprite())
        elif self.direction == -1:
            screen.blit(self.sprite_sheet_rev, [self.x, self.y], self.sprite(-1))

    def y_motion(self):
        if self.is_jump:
            if self.dash != Dash.NO_MOVE:
                reduce_jump = self.height_of_jump()
                self.y -= self.jump_speed * reduce_jump
                self.jump_speed -= settings.gravity
            if self.y >= self.initial_y:
                self.is_jump, self.is_double_jump = False, False
                self.y, self.double_jump_ready = self.initial_y, 0

    def check_not_out_screen(self):
        if not self.x < settings.screen_width + self.out_right:
            self.x = (settings.screen_width +
                      self.out_right)
        if not self.x > self.out_left:
            self.x = self.out_left

    def process_shoot_ready(self, keys):
        if not keys[player_settings.shoot]:
            if self.shoot == Shoot.SHOT:
                self.shoot = Shoot.NO_SHOOT

    def create_a_bullet(self):
        initial_x = self.x if self.direction == -1 else self.x + self.sprite.width
        self.bullets.append(
            Bullet(self.width() / 2 + initial_x + self.direction * 12.5, self.y + self.sprite.height / 2 + 9.5,
                   self.direction))

    def can_double_jump(self):
        return not self.is_double_jump and self.double_jump_ready == JumpStates.JUMP_RELEASED

    def do_jump(self):
        self.jump_speed = 12
        self.is_jump = True
        self.double_jump_ready = JumpStates.JUMP_PRESSED

    def do_double_jump(self):
        self.jump_speed = 12
        self.is_double_jump = True
        self.double_jump_ready = JumpStates.DOUBLE_JUMP_PRESSED

    def process_jump_ready(self, keys):
        if not keys[player_settings.jump]:
            if self.double_jump_ready == JumpStates.JUMP_PRESSED:
                self.double_jump_ready = JumpStates.JUMP_RELEASED
            if self.double_jump_ready == JumpStates.DOUBLE_JUMP_PRESSED:
                self.double_jump_ready = JumpStates.DOUBLE_JUMP_RELEASED

    def height_of_jump(self):
        reduce_jump = 1
        if self.jump_speed > 0 and (
                self.double_jump_ready == JumpStates.JUMP_RELEASED or self.double_jump_ready == JumpStates.DOUBLE_JUMP_RELEASED):
            reduce_jump = 0.5
        return reduce_jump
