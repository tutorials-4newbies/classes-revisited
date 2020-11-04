import sys
import pygame

size = width, height = 640, 480
speed = [2, 2]  # this is a vector [left-right speed, top-down speed]
black = 0, 0, 0

screen = pygame.display.set_mode(size)
ball = pygame.image.load("./images/intro_ball.gif")
ballrect = ball.get_rect()

another_ball = False
soccer_ball = False
soccer_ball_rect = False


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if not another_ball:
                    another_ball = True
                    soccer_ball = pygame.image.load("./images/soccer_ball.gif")
                    soccer_ball_rect = soccer_ball.get_rect()

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    if another_ball:
        soccer_ball_rect = soccer_ball_rect.move(speed)
        if soccer_ball_rect.left < 0 or soccer_ball_rect.right > width:
            speed[0] = -speed[0]
        if soccer_ball_rect.top < 0 or soccer_ball_rect.bottom > height:
            speed[1] = -speed[1]

    screen.fill(black)
    screen.blit(ball, ballrect)
    if another_ball:
        screen.blit(soccer_ball, soccer_ball_rect)
    pygame.display.flip()
