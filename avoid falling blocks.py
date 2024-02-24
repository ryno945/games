import pygame
import random

# Game Initialization
pygame.init()

win_height = 480
win_width = 700
win = pygame.display.set_mode((win_width, win_height))

# Player
player_width = 64
player_height = 64
player_x = 50
player_y = win_height - player_height - 50
player_vel = 5

# Enemy
enemy_width = 64
enemy_height = 64
enemy_x = random.randrange(0, win_width - enemy_width)
enemy_y = -enemy_height
enemy_vel = 2

run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > player_vel:
        player_x -= player_vel
    if keys[pygame.K_RIGHT] and player_x < win_width - player_width - player_vel:
        player_x += player_vel

    enemy_y += enemy_vel
    if enemy_y > win_height:
        enemy_y = -enemy_height
        enemy_x = random.randrange(0, win_width - enemy_width)

    win.fill((0,0,0))
    pygame.draw.rect(win, (255,0,0), (player_x, player_y, player_width, player_height))
    pygame.draw.rect(win, (0,0,255), (enemy_x, enemy_y, enemy_width, enemy_height))
    pygame.display.update()

pygame.quit()
