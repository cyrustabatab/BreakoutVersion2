import pygame




class Paddle(pygame.sprite.Sprite):


    def __init__(self,width,height,color,screen_height,screen_width,speed=5,bottom_gap=10):
        super().__init__()


        self.image = pygame.Surface((width,height))
        self.image.fill(color)
        self.speed = speed
        self.screen_width = screen_width
        self.rect = self.image.get_rect(center=(screen_width//2,screen_height - bottom_gap - height//2))

        self.original_center = self.rect.center

    
    def reset(self):
        self.rect.center = self.original_center
    
    @property
    def direction(self):
        if self.speed < 0:
            direction = -1
        elif self.speed > 0:
            direction = 1
        else:
            direction = 0

        return direction

    def update(self,pressed_keys):
        

        collision_threshold = 5

        if pressed_keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
            if self.rect.x < 0:
                self.rect.x = 0

        if pressed_keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
            if self.rect.right > self.screen_width:
                self.rect.right = self.screen_width

        

        
