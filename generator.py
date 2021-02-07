import pygame as py
from obstacles import Ptera, Cactus, Spike
from random import randrange
from player import Dino

cactus_group = py.sprite.Group()
ptera_group = py.sprite.Group()
spike_group = py.sprite.Group()

cont_ptera = 0
cont_cactus = 0
cont_spike = 0

cactusDistance = 0


def generatePtera():
    global cont_ptera
    y = (340, 400)
    
    cont_ptera += 2
    if cont_ptera > 400 and len(ptera_group) < 3:
        ptera = Ptera(y)
        ptera_group.add(ptera)
        cont_ptera = 0

def generateCactus():
    global cont_cactus
    global cactusDistance  
    
    cont_cactus += 3
    if cont_cactus > cactusDistance and len(cactus_group) < 3:
        cactusDistance  = randrange(130, 250)
        cactus = Cactus()
        cactus_group.add(cactus)
        cont_cactus = 0

spike = Spike()
def generatorObstacle():
    global cont_spike
    global cont_cactus
    global cont_ptera  

    if not Dino.isDead:
        cont_spike += 2
    
        if cont_spike > 1000 and not spike.isActive:
            spike_group.add(spike)
            cont_spike = 0
            spike.isActive = True

        else:
            if not spike.isActive:
                generatePtera()
                generateCactus()
    else:
        cont_cactus = 0
        cont_ptera = 0
        cont_spike = 0