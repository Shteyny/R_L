import pygame as py
from pygame import mixer
import polya, creature
import matriz

Width = 1000
Heigth = 800
FPS = 30




WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

py.init()
py.mixer.init()
screen = py.display.set_mode((Width, Heigth))
py.display.set_caption("RogueLike")
clock = py.time.Clock()


running = True
her = creature.Hero((0, 0), screen)
spis = matriz.sozd([1, 1], [10, 8], her, screen)
her.take_matriz(spis)
while running:
    screen.fill((0, 0, 0))
    clock.tick(FPS)
    for i in spis:
        for j in i:
            j.otris()
    her.otris()
    for event in py.event.get():
        if event.type == py.KEYDOWN:
            if event.key == py.K_RIGHT or event.key == py.K_d:
                her.dviz(1, 0)
            elif event.key == py.K_DOWN or event.key == py.K_s:
                her.dviz(0, 1)
            elif event.key == py.K_LEFT or event.key == py.K_a:
                her.dviz(-1, 0)
            elif event.key == py.K_UP or event.key == py.K_w:
                her.dviz(0, -1)
            spis = her.give_matriz()

        elif event.type == py.QUIT:
            running = False
    py.display.update()
py.quit()
