import pygame as py
from random import choice, randrange

from config import Velocity, width, heigth 

img = (0,1,2,3)
class Ground(py.sprite.Sprite):
    def __init__(self, x):
        py.sprite.Sprite.__init__(self)
        self.imagens = [py.image.load('assets/sprites/chao2.png'),
                        py.image.load('assets/sprites/chao3.png'),
                        py.image.load('assets/sprites/chao4.png'),
                        py.image.load('assets/sprites/chao5.png')]
        self.index = choice(img)
        self.image = self.imagens[self.index]
        self.rect = self.image.get_rect()
        self.rect[0] = x
        self.rect[1] = 425
        self.speedX = Velocity
    def update(self):
        self.rect.right -= self.speedX
        
        if self.rect.right < 0:
            self.rect[0] = 800


ground_group = py.sprite.Group()

def InitializeGround():
    for i in range(15):
        ground = Ground(60 * i)
        ground_group.add(ground)
      
InitializeGround()



class Cloud(py.sprite.Sprite):
    def __init__(self,x,y):
        py.sprite.Sprite.__init__(self,self.containers)
        self.image = py.image.load('assets/sprites/nuvem.png')
        self.rect = self.image.get_rect()
        self.rect[0] = x
        self.rect[1] = y
    def update(self):
        self.rect.right -= 1
        
        if self.rect.right < 0:
            self.rect[0] = 700

        

cloud_group = py.sprite.Group()  
Cloud.containers = cloud_group

def renderCloud():
    if len(cloud_group) < 5 and randrange(0,300) == 10:
        Cloud(width,randrange(heigth/5,heigth/2))
        




