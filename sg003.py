import pygame as pg
from pygame.locals import *

pg.init()
screen = pg.display.set_mode((600, 400))
# ====================

class Sprite:
    def __init__(self, image, x, y):
        self.x = x
        self.y = y
        self.go = 'right'
        self.dir = 0
        self.image = pg.image.load(image)

# pass: image, starting x and y position
enemy = Sprite("enemy.png", 300, 10)
player = Sprite("player.png", 300, 350)

# ====================
loop = 1
while loop:
    if enemy.x < 600:
        enemy.x += .05
    else:
        enemy.x = -100
    if player.dir == "left":
        if player.x > 0:
            player.x -= .1
    if player.dir == "right":
        if player.x < 560:
            player.x += .1
    screen.blit(enemy.image, (enemy.x, enemy.y))
    screen.blit(player.image, (player.x, player.y))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            loop = 0
        if event.type == pg.KEYDOWN:
            keys = pg.key.get_pressed()
            if keys[K_LEFT]:
                player.dir = "left"
            if keys[K_RIGHT]:
                player.dir = "right"
        if event.type == pg.KEYUP:
            player.dir = "stop"
   

    pg.display.update()

pg.quit()
