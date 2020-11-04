import sys
import pygame

size = width, height = 640, 480
speed = [2, 2]  # this is a vector [left-right speed, top-down speed]
black = 0, 0, 0

screen = pygame.display.set_mode(size)


class Ball:
    def __init__(self, image_path, speed: list = None):
        self.speed = speed or [2, 2]
        self.ball = pygame.image.load(image_path)
        self.rect = self.ball.get_rect()

    def move(self):
        self.rect = self.rect.move(self.speed)
        if self.rect.left < 0 or self.rect.right > width:
            self.speed[0] = -self.speed[0]
        if self.rect.top < 0 or self.rect.bottom > height:
            self.speed[1] = -self.speed[1]


first_ball = Ball(image_path="./images/intro_ball.gif")

balls = [first_ball]


def add_ball(image_path: str = None):
    image_path = image_path or "./images/soccer_ball.gif"
    another_ball = Ball(image_path=image_path, speed=[1, 1])
    balls.append(another_ball)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            add_ball()

    for ball in balls:
        ball.move()
    screen.fill(black)
    for ball in balls:
        screen.blit(ball.ball, ball.rect)

    pygame.display.flip()
