import random
import math

import pygame
from pygame import mixer

pygame.init()

# pygame.event.__init__()
screen = pygame.display.set_mode((1000, 700))

playerimg = pygame.image.load('images/space_invaders_images/spaceship2.png')
playerx = 470
playery = 620
playerx_change = 0
playery_change = 0

bulletimg = pygame.image.load('images/space_invaders_images/bullet.png')
bulletx = 0
bullety = 620
bulletx_change = 0
bullety_change = 70
bullet_state = "ready"

alienimg = []
alienx = []
alieny = []
alienx_change = []
alieny_change = []
no_of_aliens = 6
for i in range(no_of_aliens):
    alienimg.append(pygame.image.load('images/space_invaders_images/arcade.jpg'))
    alienx.append(random.randint(0, 900))
    alieny.append(random.randint(0, 550))
    alienx_change.append(25)
    alieny_change.append(50)

score_value = 0
font = pygame.font.Font('freesansbold.ttf', 35)
textx = 10
texty = 10

over_font = pygame.font.Font('freesansbold.ttf', 100)


def show_score(x, y):
    score = font.render("SCORE: " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


def game_over_text():
    gameover = over_font.render("GAME OVER ", True, (255, 255, 255))
    screen.blit(gameover, (200, 300))


def player(x, y):
    screen.blit(playerimg, (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletimg, (x + 16, y + 10))


def alien(x, y, i):
    screen.blit(alienimg[i], (x, y))


# def alien1(x, y):
#   screen.blit(alien1img, (x, y))


def iscollision(alienx, alieny, bulletx, bullety):
    distance = math.sqrt((math.pow(alienx - bulletx, 2)) + (math.pow(alieny - bullety, 2)))
    if distance <= 27:
        return True
    else:
        return False


# mixer.music.load('The-Island-of-Dr-Sinister.mp3')
# mixer.music.play(-1)
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('images/space_invaders_images/spaceship.png')
pygame.display.set_icon(icon)

run = True
while run:
    screen.fill((0, 0, 0))
    background = pygame.image.load('images/space_invaders_images/bgnd.png')
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerx_change = -28
            if event.key == pygame.K_RIGHT:
                playerx_change = 28
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bulletx = playerx
                    fire_bullet(bulletx, bullety)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerx_change = 0

    playerx += playerx_change
    if playerx <= 0:
        playerx = 0
    elif playerx >= 950:
        playerx = 950

    for i in range(no_of_aliens):
        if alieny[i] > 600:
            for j in range(no_of_aliens):
                alieny[i] = 10000
            game_over_text()
            break

        alienx[i] += alienx_change[i]
        if alienx[i] <= 0:
            alienx_change[i] = 25
            alieny[i] += alieny_change[i]
        elif alienx[i] >= 950:
            alienx_change[i] = -25
            alieny[i] += alieny_change[i]

        collision = iscollision(alienx[i], alieny[i], bulletx, bullety)
        if collision:
            bullety = 620
            bullet_state = "ready"
            score_value += 1
            alienx[i] = random.randint(0, 900)
            alieny[i] = random.randint(0, 450)
        alien(alienx[i], alieny[i], i)
    if bullety <= 0:
        bullety = 620
        bullet_state = "ready"

    if bullet_state is "fire":
        fire_bullet(bulletx, bullety)
        bullety -= bullety_change

    player(playerx, playery)
    show_score(textx, texty)
    pygame.display.update()
