import pygame as pg


pg.init()
screen = pg.display.set_mode((600, 400))
# ====================

class Sprite:
    def __init__(self, image, x, y):
        self.x = x
        self.y = y
        self.go = 'right'
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
    screen.blit(enemy.image, (enemy.x, enemy.y))
    screen.blit(player.image, (player.x, player.y))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            loop = 0

    pg.display.update()

pg.quit()
