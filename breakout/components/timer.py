import pygame



class Timer():
    def __init__(self, width, height):
        self.clock = pygame.time.Clock()
        self.c_time = 0
        current_time = pygame.time.get_ticks()
        current_time_sec = current_time / 1000
        current_time_int = int(current_time_sec)
        #pygame.font.init()
        #frame_count = 0
        #frame_rate = 60
        #total_seconds = frame_count // frame_rate
        #seconds = total_seconds % 60
        self.image = pygame.Surface((width, height)) 
        self.font = pygame.font.SysFont("Times New Roman", 18)
        self.time = self.font.render(str(current_time_int), True, (0, 255, 0))
        #self.image.fill((255,255,255))
        self.image.blit(self.time, (150, 150))
        #frame_count += 1
        #clock.tick(frame_rate)
        self.event = pygame.USEREVENT + 0
        pygame.time.set_timer(self.event, 1000)

        pygame.display.flip()
        
