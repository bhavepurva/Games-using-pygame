import pygame
import random
import math
from pygame import mixer

pygame.init()
screen = pygame.display.set_mode((500, 600))
pygame.display.set_caption("SLYTHERIN")

pygame.display.set_icon(screen)

snake_x = 250
snake_y = 300
snake_x_change = 0
snake_y_change = 0

food_x = random.randint(20, 480)
food_y = random.randint(20, 580)
snake_list = []
snake_length = 1
clock = pygame.time.Clock()


def snake_body(screen, color, snake_list, snake_size):
    for x, y in snake_list:
        pygame.draw.rect(screen, color, [x, y, snake_size, snake_size])


def snake(x, y):
    snake = pygame.draw.rect(screen, (0, 0, 255), (snake_x, snake_y, 20, 20))


def food():
    food = pygame.draw.rect(screen, (255, 0, 0), (food_x, food_y, 20, 20))


def collision(snake_x, snake_y, food_x, food_y):
    dist = math.sqrt(math.pow((snake_x - food_x), 2) + math.pow(snake_y - food_y, 2))
    if dist <= 20:
        return True
    else:
        return False


font = pygame.font.Font("pixel.ttf", 20)
fonts = pygame.font.Font("pixel.ttf", 40)

score_val = 0


def show_score():
    score = font.render("SCORE: " + str(score_val), True, (204, 0, 102))
    screen.blit(score, (200, 5))


def game_over(x):
    over = fonts.render("GAME OVER", True, (0, 255, 0))
    screen.blit(over, (130, 200))
    score = font.render("SCORE: " + str(score_val), True, (204, 0, 102))
    screen.blit(score, (200, 300))


run = True
while run:

    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                snake_x_change = 20
                snake_y_change = 0

            if event.key == pygame.K_LEFT:
                snake_x_change = -20
                snake_y_change = 0

            if event.key == pygame.K_UP:
                snake_y_change = -20
                snake_x_change = 0

            if event.key == pygame.K_DOWN:
                snake_y_change = 20
                snake_x_change = 0


    snake_x += snake_x_change
    snake_y += snake_y_change

    eat = collision(snake_x, snake_y, food_x, food_y)
    if eat:
        food_x = random.randint(20, 480)
        food_y = random.randint(20, 580)
        score_val += 5
        snake_length += 1
        mixer.music.load("hit.mp3")
        mixer.music.play(0)

    head = []
    head.append(snake_x)
    head.append(snake_y)
    snake_list.append(head)

    if len(snake_list) > snake_length:
        del snake_list[0]
    if head in snake_list[:-1]:
        game_over(score_val)
        snake_x = 10000
        snake_y = 10000

    if snake_x <= -20 or snake_x >= 520 or snake_y <= -20 or snake_y >= 620:
        game_over(score_val)
        snake_x = 10000
        snake_y = 10000

    food()
    snake(snake_x, snake_y)
    show_score()
    snake_body(screen, (0, 0, 255), snake_list, 20)
    pygame.display.update()
    clock.tick(10)
