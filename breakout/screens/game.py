import random
import pygame
from screens import BaseScreen

from ..components import Paddle, Ball, TileGroup, Score
from components import TextBox

#from components import score



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
        self.score = Score(100,100,0)

        # Put all sprites in the group
        self.sprites = pygame.sprite.Group()
        self.sprites.add(self.paddle)
        self.sprites.add(self.ball)
        self.sprites.add(self.score)
        self.score_value=0

    def update(self):
        #global score
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.paddle.move("left")

        if keys[pygame.K_RIGHT]:
            self.paddle.move("right")

        self.sprites.update()
        collided = self.ball.collidetiles(self.tiles)
        #score = 0
        #while self.running == True:
        #score = 0
        if collided == True:
            self.score_value += 1
            self.score = Score(100, 100, self.score_value)
            self.sprites.add(self.score)
            print(self.score_value)
            pygame.display.update
            #print(score`)

        #if collided == True:
            #self.score = score.Score(width=100, height=100)

        caught_the_ball = self.ball.collidepaddle(self.paddle.rect)

        if self.ball.rect.bottom > self.paddle.rect.top and not caught_the_ball:
            self.running = False
            self.next_screen = "game_over"
        
        #self.tiles.num_tiles
        if not self.tiles:
            #self.running == False
            #self.next_screen = "game_over"
            #print(self.tiles.num_tiles)
            self.level += 1
            self.tiles = TileGroup(level=self.level)
            
            if self.level == 4:
                self.running == False
                self.next_screen = "game_over"

    def draw(self):
        bkgrd = pygame.image.load('breakout/screens/final_valley.jpg').convert_alpha()
        self.window.fill((255, 255, 255))
        self.window.blit(bkgrd,(0,-50))
        self.sprites.draw(self.window)
        self.tiles.draw(self.window)
        

    def manage_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.running = False
            self.next_screen = "welcome"

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.ball.speed = 10
                self.ball.angle = 1.5

    