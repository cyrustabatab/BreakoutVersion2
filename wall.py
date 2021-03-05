import pygame
from brick import Brick




class Wall(pygame.sprite.Sprite):


    def __init__(self,rows,cols,brick_height,brick_width,gap_between=5):
        super().__init__()
        self.rows = rows
        self.cols = cols
        self.bricks = pygame.sprite.Group()
        self.brick_height = brick_height
        self.brick_width = brick_width
        self.gap_between = gap_between
        self._create_wall(brick_height,brick_width,gap_between)
    


    def draw(self,screen):

        self.bricks.draw(screen)


    def reset(self):
        self.bricks.empty()
        self._create_wall(self.brick_height,self.brick_width,self.gap_between)



    def _create_wall(self,brick_height,brick_width,gap_between):
        

        for col in range(self.cols):
            hits_required = 4
            for row in range(self.rows):
                if row % 2 == 0:
                    hits_required -= 1
                brick = Brick(col * (gap_between + brick_width),row * (gap_between + brick_height),brick_width,brick_height,hits_required)
                self.bricks.add(brick)
















