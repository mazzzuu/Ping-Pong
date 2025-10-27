import pygame,sys

pygame.init()

screen_widht = 1280
screen_height = 800

screen = pygame.display.set_mode((screen_widht,screen_height))
pygame.display.set_caption("Ping Pong")

clock = pygame.time.Clock()

ball = pygame.Rect((0,0,30,30))
ball.center = (screen_widht/2,screen_height/2)
ball_speed_x = 6
ball_speed_y = 6



cpu = pygame.Rect(0,0,20,100)
cpu.centery = (screen_height/2)

player = pygame.Rect(0,0,20,100)
player.midright = (screen_widht,screen_height/2)

while True:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    ball.x += ball_speed_x
    ball.y += ball_speed_y
    
    if ball.bottom >= screen_height or ball.top <=0 :
        ball_speed_y *=-1

    if ball.right>=screen_widht or ball.left <= 0:
        ball_speed_x *=-1

    screen.fill('black')
    pygame.draw.aaline(screen,'white',(screen_widht/2,0),(screen_widht/2,screen_height))
    pygame.draw.ellipse(screen,'white',ball)
    pygame.draw.rect(screen,'white',cpu)
    pygame.draw.rect(screen,'white',player)

    pygame.display.update()
    clock.tick(60)
    