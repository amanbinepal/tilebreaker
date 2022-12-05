import pygame

from .sprite import MySprite


class Score(MySprite):
    def __init__(self, width, height, score, **kwargs):
        super().__init__(**kwargs)
        pygame.font.init()
        self.image = pygame.Surface((width, height)) 
        font = pygame.font.SysFont("Times New Roman", 25)
        score_num = font.render("Score: " + str(score), True, (0, 255, 0))
        #self.image.set_colorkey((0,0,0))
        self.rect = score_num.get_rect()
        self.image.blit(score_num, (0, 0))
        pygame.display.update()

        