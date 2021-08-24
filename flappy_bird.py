import pygame
import random
import math

pygame.init()

screen = pygame.display.set_mode((300, 450))
pygame.display.set_caption("FLAPPYBIRD")
icon = pygame.image.load("images/flappy_bird_images/1.png")
pygame.display.set_icon(icon)

b_x = 0
b_xchange = 0


def background():
    bg_img = pygame.image.load("images/flappy_bird_images/bg.png")
    screen.blit(bg_img, (0, 0))


def base(b_x):
    base_img = pygame.image.load("images/flappy_bird_images/base.png")
    for i in range(50):
        screen.blit(base_img, (b_x, 380))
        b_x += 300


pipex = [200, 400]
pipey_down = [random.randint(230, 300), random.randint(230, 300)]
pipey_up = [random.randint(-100, -30), random.randint(-100, -30)]
pipex_change = 0

pipe_down_img = [pygame.image.load("images/flappy_bird_images/pipe_down.png"), pygame.image.load("images/flappy_bird_images/pipe_down.png")]
pipe_up_img = [pygame.image.load("images/flappy_bird_images/pipe_up.png"), pygame.image.load("images/flappy_bird_images/pipe_up.png")]


def pipe_down(x, y, i):
    screen.blit(pipe_down_img[i], (x, y))


def pipe_up(x, y, i):
    screen.blit(pipe_up_img[i], (x, y))


def collision(x1, y1, x2, y2):
    dist = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))
    if dist < 30:
        return True
    else:
        return False


birdx = 300 / 2
birdy = 450 / 2
birdx_change = 0
birdy_change = 0


def bird(birdx, birdy):
    bird_img = pygame.image.load("images/flappy_bird_images/bird.png")
    screen.blit(bird_img, (birdx, birdy))


scr = 0

fonts = pygame.font.Font('pixel.ttf', 50)


def score(scr):
    font = fonts.render(str(scr), True, (236, 215, 116))
    screen.blit(font, (135, 100))


def gameover():
    over=fonts.render("GameOver",True,(236, 215, 116))
    screen.blit(over, (40, 200))
    return



run = True
while run:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                b_xchange = -1
                pipex_change = -1
                birdy_change = -3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                birdy_change = 3

    background()

    for i in range(2):
        pipex[i] += pipex_change

        if pipex[i] == -100:
            pipex[i] = 300
            pipey_down[i] = random.randint(230, 300)
        collide = collision(birdx, birdy, pipex[i], pipey_down[i])
        if collide:
            birdy_change = 0
            pipex_change = 0
            b_xchange = 0

        pipe_down(pipex[i], pipey_down[i], i)

    for i in range(2):
        pipex[i] += pipex_change

        if pipex[i] == -100:
            pipex[i] = 300
            pipey_up[i] = random.randint(-100, -30)
        collide = collision(birdx, birdy, pipex[i], pipey_up[i] + 180)
        if collide:
            birdy_change = 0
            pipex_change = 0
            b_xchange = 0
            gameover()

        pipe_up(pipex[i], pipey_up[i], i)
        if pipex[i] == 150:
            scr += 1

    b_x += b_xchange
    birdy += birdy_change
    base(b_x)
    bird(birdx, birdy)
    score(scr)
    pygame.display.update()
