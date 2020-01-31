import pygame as pg
from pygame.locals import *

pg.init()
screen = pg.display.set_mode((600, 400))
# ====================


class Sprite:
    def __init__(self, img, x, y):
        self.x = x
        self.y = y
        self.dir = 'stop'
        self.image = pg.image.load(img)


enemy = Sprite("enemy.png", 0, 10)
player = Sprite("player.png", 250, 300)

loop = 1
# ==================== THE WHILE LOOP ========
while loop:
    screen.fill((0, 0, 0))
    if enemy.x < 600:
        enemy.x += .1
    else:
        enemy.x = -100

    if player.dir == "left":
        if player.x >0:
            player.x -= .1

    if player.dir == "right":
        if player.x < 495:

            player.x += .1

    screen.blit(enemy.image, (enemy.x, enemy.y))
    screen.blit(player.image, (player.x, player.y))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            loop = 0
        if event.type == pg.KEYDOWN:
            keys = pg.key.get_pressed()
            if keys[K_RIGHT]:
                player.dir = "right"
            if keys[K_LEFT]:
                player.dir = "left"
        if event.type == pg.KEYUP:
            player.dir = "stop"




    pg.display.update()

pg.quit()
