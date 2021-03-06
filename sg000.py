import pygame as pg


pg.init()
screen = pg.display.set_mode((600, 400))
# ====================


class Enemy:
    def __init__(self):
        self.x = 300
        self.y = 10
        self.go = 'right'
        self.image = pg.image.load("enemy.png")


enemy = Enemy()


# ====================
loop = 1
while loop:
    screen.blit(enemy.image, (enemy.x, enemy.y))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            loop = 0

    pg.display.update()

pg.quit()
