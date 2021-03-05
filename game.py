import pygame,sys

pygame.init()
from wall import Wall
from paddle import Paddle
from ball import Ball



BRICK_WIDTH,BRICK_HEIGHT = 100,50
ROWS = 6
COLS = 6
GAP_BETWEEN = 5
WIDTH,HEIGHT = BRICK_WIDTH * COLS + GAP_BETWEEN * (COLS - 1),600
screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()
FPS = 60
BGCOLOR = (210,180,140)
pygame.display.set_caption("Breakout")


wall = Wall(ROWS,COLS,BRICK_HEIGHT,BRICK_WIDTH)
paddle_height,paddle_width = 20,100
paddle_color = (128,128,128)

ball_color= (255,255,0)
ball_radius = 10
paddle = pygame.sprite.GroupSingle(Paddle(paddle_width,paddle_height,paddle_color,HEIGHT,WIDTH))
paddle_midtop = paddle.sprite.rect.midtop
ball = pygame.sprite.GroupSingle(Ball(paddle_midtop,ball_radius,ball_color,WIDTH,HEIGHT))

WHITE= (255,255,255)
font = pygame.font.SysFont("comicsansms",42)

start_text = font.render("Click Anywhere To Start!",True,WHITE)
start_text_rect = start_text.get_rect(center=(WIDTH//2,HEIGHT//2 +50))
game_over_text = font.render("GAME OVER",True,WHITE)
game_over_text_rect = game_over_text.get_rect(center=(WIDTH//2,HEIGHT//2 +50))
game_over_text_2 = font.render("Hit Enter to Play Again!",True,WHITE)
game_over_text_rect_2 = game_over_text_2.get_rect(center=(WIDTH//2,game_over_text_rect.bottom + 50))

started = False

game_over = False


def reset():
    ball.sprite.reset()
    paddle.sprite.reset()
    wall.reset()

while True:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif not started and event.type == pygame.MOUSEBUTTONDOWN:
            started = True
        elif game_over and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                started = False
                game_over = False
                reset()
    
    

    if started and not game_over:
        pressed_keys = pygame.key.get_pressed()

        paddle.update(pressed_keys)
        game_over = ball.sprite.update(paddle.sprite,wall.bricks)

            
    screen.fill(BGCOLOR)
    wall.draw(screen)
    paddle.draw(screen)
    ball.sprite.draw(screen)

    if not started:
        screen.blit(start_text,start_text_rect)
    elif game_over:
        screen.blit(game_over_text,game_over_text_rect)
        screen.blit(game_over_text_2,game_over_text_rect_2)



    pygame.display.update()
    clock.tick(FPS)







