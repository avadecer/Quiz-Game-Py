import pygame
import random

# initialize the game
pygame.init()

# display or the screen (width, height)
screen = pygame.display.set_mode((800, 600))

# title and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# player
PlayerImg = pygame.image.load('space-invaders.png')
PlayerImg_final = pygame.transform.scale(PlayerImg, (50, 50))
playerX = 370
playerY = 480
playerX_change = 0

# enemy
EnemyImg = pygame.image.load('alien.png')
EnemyImg_final = pygame.transform.scale(EnemyImg, (50, 50))
enemyX = random.randint(0, 800)      # random position of enemy in x coordinate
enemyY = random.randint(50, 150)     # random position of enemy in y coordinate
enemyX_change = 0.15
enemyY_change = 40


def player(x, y):
    screen.blit(PlayerImg_final, (x, y))  # (image, (x coordinate, y coordinate))  blit = use to draw

def enemy(x, y):
    screen.blit(EnemyImg_final, (x, y))

# prevent from shutting down/ crashing == game loop
running = True
while running:

    # RGB (Red, Green, Blue)
    screen.fill((204, 204, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # keystroke left or right -- movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.2
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.2
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    playerX += playerX_change

    # boundaries for player
    if playerX <= 0:
        playerX = 0
    elif playerX >= 750:
        playerX = 750

    enemyX += enemyX_change

    # enemy movement
    if enemyX <= 0:
        enemyX_change = 0.15
        enemyY += enemyY_change
    elif enemyX >= 750:
        enemyX_change = -0.15
        enemyY += enemyY_change

    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()  # need this to appear the updates

    print("kwek kwek and isaw.")