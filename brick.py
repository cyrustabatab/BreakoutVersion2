import pygame


RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
PURPLE = (128,0,128)

class Brick(pygame.sprite.Sprite):
    

    color_mapping = {1: BLUE,2: GREEN,3: RED,4: PURPLE}

    def __init__(self,x,y,width,height,hits_required=1):
        super().__init__()
        self.width = width
        self.height = height
        self.image = pygame.Surface((self.width,self.height))
        self.hits_required = hits_required
        self.color = self.color_mapping[hits_required]
        self.image.fill(self.color)
        self.rect = self.image.get_rect(topleft=(x,y))


    def update(self):

        self.hits_required -= 1

        if self.hits_required == 0:
            self.kill()
        else:
            self.image.fill(self.color_mapping[self.hits_required])






