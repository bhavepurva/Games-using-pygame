import pygame
import math

pygame.init()

screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("BRICKS")
pygame.display.set_icon(screen)

player_x = 200
player_y = 280
player_x_change = 0
player_y_change = 0

ball_x = 200
ball_y = 250
ball_x_change = 0.2
ball_y_change = -0.2

brick_x = []
brick_y = []
brick_img = []
no_of_bricks = 32
p = 5
q = 10

font = pygame.font.Font("pixel.ttf", 50)
fonts=pygame.font.Font("pixel.ttf",15)

def ball(x, y):
    pygame.draw.rect(screen, (255, 255, 0), (ball_x, ball_y, 10, 10))


def collision(x1, y1, x2, y2):
    dist = math.sqrt(math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2))
    if dist < 30:
        return True
    else:
        return False


def player_collision(x1, y1, x2, y2):
    dist = math.sqrt(math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2))
    if dist < 30:
        return True
    else:
        return False


def player(x, y):
    pygame.draw.rect(screen, (0, 0, 255), (player_x, player_y, 50, 10))


def gameover(x):
    screen.fill((255, 0, 0))
    over = font.render("GAME OVER", True, (0, 0, 0))
    screen.blit(over, (40, 120))
    s=font.render("SCORE: "+ str(score),True,(255,255,255))
    screen.blit(s, (50, 170))


score=0
def show_score(x):
    s=fonts.render("SCORE: "+ str(score),True,(255,0,0))
    screen.blit(s,(10,280))




run = True
while run:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player_x_change = 0.3
            if event.key == pygame.K_LEFT:
                player_x_change = -0.3
            if event.key==pygame.K_SPACE:
                ball_y=200

        if event.type == pygame.KEYUP:
            player_x_change = 0

    player_x += player_x_change
    ball_x += ball_x_change
    ball_y += ball_y_change

    if player_x <= 10:
        player_x = 10
    if player_x >= 340:
        player_x = 340

    if ball_x >= 390:
        ball_x_change = -0.2
    if ball_y <= 0:
        ball_y_change = 0.2
    if ball_x <= 0:
        ball_x_change = 0.2
    if ball_y >= 290:
        gameover(score)

    for i in range(no_of_bricks):
        for j in range(4):
            brick_x.append(p)
            brick_y.append(q)
            brick_img.append(pygame.draw.rect(screen, (255, 0, 0), (brick_x[i], brick_y[i], 40, 20)))
            q += 30
        q = 10
        p += 50
        collide = collision(ball_x, ball_y, brick_x[i], brick_y[i])
        if collide:
            ball_y_change = 0.2
            brick_x[i] = 1000
            score+=1

    player_collide = player_collision(player_x, player_y, ball_x, ball_y)
    if player_collide:
        ball_y_change = -0.2

    player(player_x, player_y)
    ball(ball_x, ball_y)
    show_score(score)
    pygame.display.update()
