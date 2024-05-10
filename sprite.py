import player_settings


class Sprite:
    def __init__(self, sprite):
        if not isinstance(sprite, list):
            raise ValueError(f'You tried to use "{sprite.__class__.__name__}" when list is required')
        elif len(sprite) != 4:
            raise IndexError(f"You need 4 values for (x1, y1, x2, y2), but you put {len(sprite)}")

        self.sprite = [player_settings.scale * n for n in sprite]
        self.width = sprite[2] - sprite[0]
        self.height = sprite[3] - sprite[1]

    def __call__(self):
        return self.sprite
