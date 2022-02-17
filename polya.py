import pygame as py

black = py.image.load("data/Black.png")
grass = py.image.load("data/grass.jpg")
grass = py.transform.scale(grass, (100, 100))
portal = py.image.load("data/portal2.png")
portal = py.transform.scale(portal, (100, 100))


class Clet:
    def __init__(self, Hero, coor, screen):
        self.x, self.y = coor[0], coor[1]
        self.screen = screen
        self.hero = Hero

    def otris(self):
        self.screen.blit(grass, (self.x * 100, self.y * 100))

    def give_event(self):
        pass



class Block(Clet):
    def give_event(self):
        self.hero.back()

    def otris(self):
        self.screen.blit(black, (self.x * 100, self.y * 100))

class Evac(Clet):
    def give_event(self):
        return self.hero.portal()

    def otris(self):
        self.screen.blit(portal, (self.x * 100, self.y * 100))