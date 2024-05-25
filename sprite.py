class Sprite:
    def __init__(self, sprite, sprite_sheet_size, fps=0, scale=1):
        if not isinstance(sprite, list):
            raise TypeError(f'You tried to use "{sprite.__class__.__name__}" when list is required')
        elif len(sprite) != 4:
            raise IndexError(f"You need 4 values for (x1, y1, x2, y2), but you put {len(sprite)}")

        if not isinstance(fps, int):
            raise TypeError(f'You tried to use "{sprite.__class__.__name__}" when int is required')
        elif fps < 0:
            raise ValueError(f'You have a negative value on FPS, value sent: {fps}')

        self.sprite = [scale * n for n in sprite]
        self.sprite_rev = [sprite_sheet_size * scale - self.sprite[2] - self.sprite[0], self.sprite[1],
                           self.sprite[2],
                           self.sprite[3]]
        self.width = sprite[2]
        self.height = sprite[3]
        self.FPS = fps

    def __call__(self, direction=1):
        if direction == 1:
            return self.sprite
        elif direction == -1:
            return self.sprite_rev
        raise ValueError(f"Only acceptable values are 1 or -1, inserted {direction}")
