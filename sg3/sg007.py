import pygame as pg
from pygame.locals import *
from random import random, randrange




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

def music_init():
    "Initialize sounds avoiding delay"
    pg.mixer.pre_init(44100, -16, 1, 512)
    pg.init()
    pg.mixer.quit()
    pg.mixer.init(22050, -16, 2, 512)
    pg.mixer.set_num_channels(32)

music_init()
screen = pg.display.set_mode((600, 400))
clock = pg.time.Clock()
# ============= SPRITES
enemy = Sprite("imgs/enemy.png", 0, 10)
player = Sprite("imgs/player.png", 250, 350)
bullet = Sprite("imgs/bullet.png", 272, 345)

# Movement speed
go = 1
# The score
score = 0
# When 1 you can fire the bullet
charged = 1
# This is the time to randomly change enemy path direction
tragitto = 100
count = tragitto
# Whe the enemy's hit
hit = 0





def game_sounds():
    "Loads the sounds for the game"
    sounds_list = "fire",
    sound_dic = {}
    for sound in sounds_list:
        sound_path = f"audio/{sound}.wav"
        print(sound_path)
        sound_dic[sound] = pg.mixer.Sound(sound_path)
    return sound_dic

sounds_dic = game_sounds()

def create_fonts(font_sizes_list):
    fonts = []
    for size in font_sizes_list:
        fonts.append(pg.font.SysFont("Arial", size))
    return fonts


def _display(fnt, what, color, where):
    text_to_show = fnt.render(what, 0, pg.Color(color))
    screen.blit(text_to_show, where)


def display_fps():
    _display(
        fonts[0],
        what=str(int(clock.get_fps())),
        color="white",
        where=(0, 0))

def display_score():
    _display(
        fonts[0],
        what= "Score " + str(score),
        color="white",
        where=(300, 0))

fonts = create_fonts([32, 16, 14, 8])
sound = pg.mixer.Sound.play
# ==================== THE WHILE LOOP ========

def enemy_back():
    enemy.y = 10
    enemy.x = randrange(1, 500)
    hit = 0

loop = 1
while loop:
    # When enemy's hit falls down and can hit the player
    if hit == 1:
        enemy.y += 1
        # if bullet.rect.colliderect(enemy.rect):
        #     score += 100
        #     enemy.y = 10
        #     enemy.x = randrange(1, 500)
        #     hit = 0
        #     print("You killed it definitively")
        if enemy.rect.colliderect(player.rect):
            print("You died!")
            hit = 0
            enemy.y = 10
            enemy.x = randrange(1, 500)
            score -= 10
    if enemy.y > 400:
        enemy.y = 10
        enemy.x = randrange(1, 500)
        hit = 0
        score -= 20
        print("Your score is" + str(score))
        print("Alien reached the Earth")


    screen.fill((0, 0, 0))
    display_fps()
    display_score()
    count -= 1
    if count == 0:
        if random() > .5:
            go = -1
        else:
            go = 1
        count = tragitto
    enemy.x += go
    if enemy.x > 600:
        enemy.x = -100
    if enemy.x < 0:
        enemy.x = 600

    bullet.update()
    enemy.update()
    player.update()

    if bullet.dir == "up":
        bullet.y -= 2
        if bullet.rect.colliderect(enemy.rect):
            score += 10
            print("Score = " + str(score))
            hit = 1
            bullet.y = bullet.start
            bullet.dir = "stop"
            charged = 1
            bullet.x = player.x + 22
        elif bullet.y < 0: 
            bullet.y = bullet.start
            bullet.x = player.x + 22
            bullet.dir = "stop"
            charged = 1


    if player.dir == "left":
        if player.x > 0:
            player.x -= 1
            if bullet.dir == "stop":
                bullet.x -= 1

    if player.dir == "right":
        if player.x < 550:
            player.x += 1
            if bullet.dir == "stop":
                bullet.x += 1


    screen.blit(enemy.image, (int(enemy.x), int(enemy.y)))
    screen.blit(player.image, (int(player.x), int(player.y)))
    screen.blit(bullet.image, (int(bullet.x), int(bullet.y)))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            loop = 0

        if charged:
            if event.type == pg.KEYDOWN:
                if event.key == K_UP:
                    sound(sounds_dic["fire"])
                    bullet.dir = "up"
                    charged = 0
        if pg.key.get_pressed():
            keys = pg.key.get_pressed()
            # if keys[K_UP]:
            if keys[K_RIGHT]:
                player.dir = "right"
            elif keys[K_LEFT]:
                player.dir = "left"
            else:
                player.dir = "stop"

        # if event.type == pg.KEYUP:
        #     player.dir = "stop"

    clock.tick(240)
    pg.display.update()

pg.quit()
