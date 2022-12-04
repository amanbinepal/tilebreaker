import pygame
from .tile import Tile
import random


class TileGroup(pygame.sprite.Group):
    def __init__(self, level, tile_width=120, tile_height=30):
        super().__init__()

        if level == 0:
            num_tiles = 1
            count=0
            while count < num_tiles:
                x = random.randint(100, 600)
                y = random.randint(100, 600)
                tile = Tile(width=tile_width, height=tile_height)
                tile.move_to(x, y)
                self.add(tile)
                count+=1
        elif level == 1:
            num_tiles = 5
            count=0
            while count < num_tiles:
                x = random.randint(100, 600)
                y = random.randint(100, 600)
                tile = Tile(width=tile_width, height=tile_height)
                tile.move_to(x, y)
                self.add(tile)
                count+=1
        elif level == 2:
            num_tiles = 4
            count=0
            while count < num_tiles:
                x = random.randint(100, 600)
                y = random.randint(100, 600)
                tile = Tile(width=tile_width, height=tile_height)
                tile.move_to(x, y)
                self.add(tile)
                count+=1
        elif level == 3:
            num_tiles = 2
            count=0
            while count < num_tiles:
                x = random.randint(100, 600)
                y = random.randint(100, 600)
                tile = Tile(width=tile_width, height=tile_height)
                tile.move_to(x, y)
                self.add(tile)
                count+=1
        


