import pygame,sys

def animate_ball():
    global ball_speed_x, ball_speed_y
    ball.x += ball_speed_x
    ball.y += ball_speed_y
    
    if ball.bottom >= screen_height or ball.top <=0 :
        ball_speed_y *=-1

    if ball.right>=screen_widht or ball.left <= 0:
        ball_speed_x *=-1

def animate_player():
    player.y += player_speed

    if player.top <= 0:
        player.top = 0

    if player.bottom >= screen_height:
        player.bottom = screen_height

def animate_cpu():
    cpu.y += cpu_speed

    if ball.centery <= cpu.centery:
        cpu_speed = -6
    if ball.centery >= cpu.centery:
        cpu_speed = 6

    if cpu.bottom >= screen_height:
        cpu.bottom=screen_height
    if cpu.top <= 0:
        cpu.top=0

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
cpu_speed = 6


player = pygame.Rect(0,0,20,100)
player.midright = (screen_widht,screen_height/2)
player_speed = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player_speed =-6
            if event.key == pygame.K_DOWN:
                player_speed = +6
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player_speed = 0
            if event.key == pygame.K_DOWN:
                player_speed = 0

    animate_ball()
    animate_player()


    screen.fill('black')
    pygame.draw.aaline(screen,'white',(screen_widht/2,0),(screen_widht/2,screen_height))
    pygame.draw.ellipse(screen,'white',ball)
    pygame.draw.rect(screen,'white',cpu)
    pygame.draw.rect(screen,'white',player)

    pygame.display.update()
    clock.tick(60)
    