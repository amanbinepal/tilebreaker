import random
import pygame
import requests
import json
from screens import BaseScreen

from ..components import Paddle, Ball, TileGroup, Score
from components import TextBox




class GameScreen(BaseScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Create the paddle
        self.paddle = Paddle(200, 30, (0, 255, 0), limits=self.rect)

        # Create the ball
        self.ball = Ball(limits=self.rect)
        self.ball.speed = 8

        self.ball.angle = random.randint(0, 31416) / 10000

        # Create the tiles
        self.level = 0
        self.tiles = TileGroup(self.level, tile_width=120, tile_height=30)
       

        #Score
        self.score = Score(100,60,0)


        # Put all sprites in the group
        self.sprites = pygame.sprite.Group()
        self.sprites.add(self.paddle)
        self.sprites.add(self.ball)
        self.sprites.add(self.score)
        self.score_value=0
        self.combo = False
        self.multiplier = 1
        self.first_collision = True

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.paddle.move("left")

        if keys[pygame.K_RIGHT]:
            self.paddle.move("right")

        self.sprites.update()
        collided = self.ball.collidetiles(self.tiles)
        caught_the_ball = self.ball.collidepaddle(self.paddle.rect)
        

        if collided or caught_the_ball:
            if collided:
                if self.first_collision:
                    self.score_value += 1
                    self.first_collision = False
                else:
                    self.score_value += (1 + self.multiplier)
                    self.multiplier += 1
            else:
                self.multiplier = 1
                self.first_collision = True

            self.score = Score(100, 60, self.score_value)
            self.sprites.add(self.score)
            pygame.display.update


        clock = pygame.time.Clock()
        clock.tick(144)
        text_font = pygame.font.SysFont("Times New Roman", 25)
        time_secs = int(pygame.time.get_ticks() / 1000)
        self.time = text_font.render("Time: " + str(time_secs), True, (0, 255, 0))
        

        if self.ball.rect.bottom > self.paddle.rect.top and not caught_the_ball:
            self.running = False
            self.next_screen = "game_over"
          
            requests.post("http://127.0.0.1:5000/add", json={"Score": self.score_value})
        

        if not self.tiles:
            
            self.level += 1
            self.ball.speed += 1
            self.tiles = TileGroup(level=self.level)
            
            if self.level == 4:
        
                self.level = -1
                self.ball.speed += 2

            

    def draw(self):
        bkgrd = pygame.image.load('breakout/screens/final_valley.jpg').convert_alpha()
        self.window.fill((255, 255, 255))
        self.window.blit(bkgrd,(0,-50))
        self.sprites.draw(self.window)
        self.tiles.draw(self.window)
        self.window.blit(self.time, (0,28))
        

    def manage_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.running = False
            self.next_screen = "welcome"

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.ball.speed = 10
                self.ball.angle = 1.5

    