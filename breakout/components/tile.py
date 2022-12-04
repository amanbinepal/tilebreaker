import pygame
from .sprite import MySprite
import random


class Tile(MySprite):
    """Tile - meant to be hit with the ball"""

    def __init__(self, *args, width=80, height=80, **kwargs):
        super().__init__(*args, **kwargs)
        size = (width, height)
        self.image = pygame.image.load('breakout/components/emerald.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect()
        pygame.display.update()
