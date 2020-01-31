import pygame as pg

pg.init()
screen = pg.display.set_mode((600, 400))

loop = 1
while loop:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            loop = 0

pg.quit()
