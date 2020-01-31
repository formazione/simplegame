import pygame as pg
from pygame.locals import *
from random import random, randrange


pg.init()
screen = pg.display.set_mode((600, 400))
# ====================


class Sprite:
    def __init__(self, img, x, y):
        self.x = x
        self.y = y
        self.dir = 'stop'
        self.image = pg.image.load(img)
        self.w, self.h = self.image.get_rect().size
        self.start = y
        self.update()

    def update(self):
        self.rect = pg.Rect(int(self.x), int(self.y), int(self.w), int(self.h))


enemy = Sprite("enemy.png", 0, 10)
player = Sprite("player.png", 250, 350)
bullet = Sprite("bullet.png", 280, 345)


loop = 1
go = .1
score = 0
charged = 1
# ==================== THE WHILE LOOP ========
tragitto = 1000
count = tragitto
# Whe the enemy's hit
hit = 0
while loop:
    if hit == 1:
        enemy.y += .1
        if enemy.y > 400:
            enemy.y = 10
            enemy.x = randrange(1, 500)
            hit = 0

    screen.fill((0, 0, 0))
    count -= 1
    if count == 0:
        if random() > .5:
            go = -.1
        else:
            go = .1
        count = tragitto
    enemy.x += go
    if enemy.x > 600:
        enemy.x = -100
    if enemy.x < 0:
        enemy.x = 600

    bullet.update()
    enemy.update()

    if bullet.dir == "up":
        bullet.y -= .1
        if bullet.rect.colliderect(enemy.rect):
            score += 10
            print("Score = " + str(score))
            hit = 1
            bullet.y = bullet.start
            bullet.dir = "stop"
            charged = 1
            bullet.x = player.x + 30
        elif bullet.y < 0: 
            bullet.y = bullet.start
            bullet.x = player.x + 30
            bullet.dir = "stop"
            charged = 1


    if player.dir == "left":
        if player.x > 0:
            player.x -= .1
            if bullet.dir == "stop":
                bullet.x -= .1

    if player.dir == "right":
        if player.x < 495:
            player.x += .1
            if bullet.dir == "stop":
                bullet.x += .1


    screen.blit(enemy.image, (int(enemy.x), int(enemy.y)))
    screen.blit(player.image, (int(player.x), int(player.y)))
    screen.blit(bullet.image, (int(bullet.x), int(bullet.y)))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            loop = 0

        if charged:
            if event.type == pg.KEYDOWN:
                if event.key == K_UP:
                    bullet.dir = "up"
                    charged = 0
        if pg.key.get_pressed():
            keys = pg.key.get_pressed()
            # if keys[K_UP]:
            if keys[K_RIGHT]:
                player.dir = "right"
            if keys[K_LEFT]:
                player.dir = "left"


        # if event.type == pg.KEYUP:
        #     player.dir = "stop"




    pg.display.update()

pg.quit()
