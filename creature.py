import matriz
import pygame as py
from random import randint

hero = py.image.load("data/player.png")
hero = py.transform.scale(hero, (100, 100))
hero.set_colorkey((0, 128, 128))
hero_rev = py.transform.flip(hero, True, False)

#monster1 = py.image.load("data/monster.png")
#monster1 = py.transform.scale(monster1, 100, 100)




class Hero:
    def __init__(self, coor, screen):
        self.x, self.y = coor[0], coor[1]
        self.coor = coor
        self.screen = screen
        self.coorcash = (self.coor[0], self.coor[1])

    def otris(self):
        self.screen.blit(hero, (self.x * 100, self.y * 100))

    def take_matriz(self, matriz):
        self.matriz = matriz

    def dviz(self, x, y):
        if self.x + x < 10 and self.x + x >= 0:
            self.x += x
        if self.y + y < 8 and self.y + y >= 0:
            self.y += y
        self.coor = (self.x, self.y)
        self.matriz[self.y][self.x].give_event()
        self.coorcash = (self.x, self.y)
        self.coor= self.coorcash


    def back(self):
        self.x, self.y = self.coorcash[0], self.coorcash[1]

    def portal(self):
        self.take_matriz(matriz.sozd([self.coor[0] + 1, self.coor[1] + 1], [randint(1, 10), 8 - (self.coor[1])], self, self.screen))

    def give_matriz(self):
        return self.matriz

