import pygame as pg
import random as rd
#Initialize pygame


pg.init()
        #Define the screen
screen=pg.display.set_mode((800,600))
pg.display.set_caption("Space Invader")
background=pg.image.load('background.png')
icon=pg.image.load("ufo.png")
pg.display.set_icon(icon)
playerImg=pg.image.load('player.png')
playerX=370
playerY=480
playerX_change=0
# Enemy
enemyImg=pg.image.load('enemy.png')
enemyX=rd.randint(0,800)
enemyY=rd.randint(50,150)
enemyX_change = 4
enemyY_change= 40


def player(x,y):
    screen.blit(playerImg,(x,y))


def enemy(x,y):
    screen.blit(enemyImg,(x,y))


running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(background,(0,0))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                playerX_change= -5
            if event.key == pg.K_RIGHT:
                playerX_change = 5

        if event.type == pg.KEYUP:
            playerX_change = 0

    playerX+=playerX_change
    enemyX += enemyX_change
    if playerX <=0:
        playerX=2
    elif playerX >= 736:
        playerX=734

    if enemyX <=0:
        enemyX_change = 4
        enemyY += enemyY_change
    elif enemyX >= 736:
        enemyX=736
        enemyX_change = -4
        enemyY +=enemyY_change
    
    enemy(enemyX,enemyY)
    player(playerX,playerY)
    pg.display.update()




