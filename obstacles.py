import pygame as py
from random import randrange, choice

from config import Velocity, spriteSwap

class Ptera(py.sprite.Sprite):
    def __init__(self, y):
        py.sprite.Sprite.__init__(self)
        self.imagens = [py.image.load('./assets/sprites/ptera1.png'),
                        py.image.load('./assets/sprites/ptera2.png')]
        self.image = py.image.load('./assets/sprites/ptera1.png')
        self.rect = self.image.get_rect()
        self.rect[0] = 800
        self.rect[1] = choice(y)
        self.speedX = randrange(4, 6) + Velocity / 2
        self.index = 0
        self.time = 5

    def update(self):
        self.rect[0] -= self.speedX
        
        if self.rect[0] < 0:
            self.kill()
        
        self.time -= 1
        if self.time == 0:
            self.image = spriteSwap(self.imagens, self.index)
            self.index += 1
            if self.index >= 2:
                self.index = 0
            self.time = 15


class Cactus(py.sprite.Sprite):
    def __init__(self):
        py.sprite.Sprite.__init__(self)
        self.imagens = [py.image.load('./assets/sprites/cactus1.png'),
                        py.image.load('./assets/sprites/cactus2.png'),
                        py.image.load('./assets/sprites/cactus3.png'),
                        py.image.load('./assets/sprites/cactus4.png')]
        self.image = self.imagens[randrange(1, 4)]
        self.rect = self.image.get_rect()
        self.rect[0] = 800
        self.rect[1] = 400
        self.speedX = Velocity
    def update(self):
        self.rect[0] -= self.speedX

        if self.rect[0] < 0:
            self.kill()


class Spike(py.sprite.Sprite):
    def __init__(self, start = False):
        py.sprite.Sprite.__init__(self)
        self.image = py.image.load('./assets/sprites/spike.png')
        self.rect = self.image.get_rect()
        self.rect[0] = 800
        self.rect[1] = 400
        self.speedX = Velocity
        self.isActive = start
    def update(self):
        self.rect[0] -= self.speedX

        if self.rect.right < 0:
            self.kill()
            self.isActive = False

