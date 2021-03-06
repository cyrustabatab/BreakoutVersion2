import pygame,os
from copy import copy

vec =pygame.math.Vector2




class Ball(pygame.sprite.Sprite):
    

    hit_sound = pygame.mixer.Sound(os.path.join('assets','pong.ogg'))

    def __init__(self,midtop,radius,color,screen_width,screen_height,x_speed=5,y_speed=-5):
        super().__init__()
        self.radius = radius#radius
        self.pos = vec(midtop[0] - radius ,midtop[1] - 2* radius)
        self.original_pos = copy(self.pos)
        self.color = color
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.original_x,self.original_y = x_speed,y_speed
        self.vel = vec(x_speed,y_speed)
        self.speed_x_max = x_speed + 1


        self.rect = pygame.Rect(*self.pos,self.radius * 2,self.radius * 2)
        self.original_center = self.rect.center
    

    def reset(self):
        self.pos = copy(self.original_pos)
        self.rect.center = self.original_center
        self.vel = vec(self.original_x,self.original_y)

    def update(self,paddle,bricks):
        
        collision_thresh = abs(self.vel.y)
        self.pos += self.vel

        self.rect.x,self.rect.y = self.pos.x,self.pos.y
        if self.pos.x <= 0:
            self.vel.x *= -1
        elif self.pos.x + self.rect.width >= self.screen_width:
            self.vel.x *= -1
        elif self.pos.y <= 0:
            self.vel.y *= -1
        elif self.pos.y  + self.rect.height>= self.screen_height:
            return True




        if self.rect.colliderect(paddle.rect):
            self.hit_sound.play()
            if (abs(self.rect.bottom - paddle.rect.top) <= collision_thresh) and self.vel.y > 0:
                self.vel.y *= -1
                self.vel.x += paddle.direction
                if self.vel.x > self.speed_x_max:
                    self.vel.x = self.speed_x_max
                elif self.vel.x < 0 and self.vel.x < -self.speed_x_max:
                    self.vel.x = -self.speed_x_max
            else:
                self.vel.x *= -1
        else:

            bricks_hit = pygame.sprite.spritecollide(self,bricks,dokill=False)
            if bricks_hit:
                self.hit_sound.play()
            for brick in bricks_hit:
                brick.update()
                if abs(self.rect.bottom - brick.rect.top) <= collision_thresh and self.vel.y > 0:
                    self.vel.y *= -1
                elif abs(self.rect.top - brick.rect.bottom) <= collision_thresh and self.vel.y < 0:
                    self.vel.y *= -1
                elif abs(self.rect.right - brick.rect.left) <= collision_thresh and self.vel.x > 0:
                    self.vel.x *= -1
                elif abs(self.rect.left - brick.rect.right) <= collision_thresh and self.vel.x < 0:
                    self.vel.x *= -1
            

        return False 


    def draw(self,screen):

        pygame.draw.ellipse(screen,self.color,self.rect)









