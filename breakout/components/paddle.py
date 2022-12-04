import pygame

from .sprite import MySprite


class Paddle(MySprite):
    """Represents the game paddle"""

    def __init__(self, width, height, color=(0, 0, 0), **kwargs):
        super().__init__(**kwargs)
        size = (width, height)
        self.image = pygame.image.load('breakout/components/ruby.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect()
        pygame.display.update()

        if self.limits:
            self.move_to(
                self.limits.center[0] - self.rect.width / 2,
                self.limits.bottom - self.rect.height,
            )
