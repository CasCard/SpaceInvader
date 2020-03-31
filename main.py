import pygame as pg
import random as rd
import math

# Initialize pygame


pg.init()
score = 0
# Define the screen
screen = pg.display.set_mode((800, 600))
pg.display.set_caption("Space Invader")
background = pg.image.load('background.png')
icon = pg.image.load("ufo.png")
pg.display.set_icon(icon)
playerImg = pg.image.load('player.png')
playerX = 370
playerY = 480
playerX_change = 0
# Enemy
enemyImg = []
enemyY = []
enemyX = []
enemyX_change = []
enemyY_change = []
numberOfEnemy = 6
for i in range(numberOfEnemy):
    enemyImg.append(pg.image.load('enemy.png'))
    enemyX.append(rd.randint(0, 735))
    enemyY.append(rd.randint(50, 150))
    enemyX_change.append(4)
    enemyY_change.append(40)

# Bullete
bulletState = "ready"
bulletImg = pg.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10


def fireBullet(x, y):
    global bulletState
    bulletState = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))


def player(x, y):
    screen.blit(playerImg, (x, y))


def isCollision(bulletX, bulletY, enemyX, enemyY):
    distance = math.sqrt(math.pow((bulletX - enemyX), 2) + math.pow((bulletY - enemyY), 2))
    if distance < 27:
        return True
    else:
        return False


def enemy(x, y,i):
    screen.blit(enemyImg[i], (x, y))


running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                playerX_change = -5
            if event.key == pg.K_RIGHT:
                playerX_change = 5
            if event.key == pg.K_SPACE:
                if bulletState is "ready":
                    bulletX = playerX
                    fireBullet(bulletX, bulletY)

        if event.type == pg.KEYUP:
            playerX_change = 0

    playerX += playerX_change
    enemyX += enemyX_change
    if playerX <= 0:
        playerX = 2
    elif playerX >= 736:
        playerX = 736

    for i in range(numberOfEnemy):
        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 4
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX[i] = 736
            enemyX_change[i] = -4
            enemyY[i] += enemyY_change[i]

        collision = isCollision(bulletX, bulletY, enemyX[i], enemyY[i])
        if collision:
            bulletY = 480
            enemyX[i] = rd.randint(0, 735)
            enemyY[i] = rd.randint(50, 150)
            score += 1
            print(score)
            bulletState = "ready"

        enemy(enemyX[i], enemyY[i],i)

    if bulletY <= 0:
        bulletY = 480
        bulletState = "ready"

    if bulletState is "fire":
        fireBullet(bulletX, bulletY)
        bulletY -= bulletY_change




    player(playerX, playerY)
    pg.display.update()
