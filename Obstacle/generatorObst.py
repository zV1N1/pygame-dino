import pygame as py
from obstacles import Ptera, Cactus, Spike

cactus_group = py.sprite.Group()
ptera_group = py.sprite.Group()
spike_group = py.sprite.Group()

cont_ptera = 0
cont_cactus = 0
cont_spike = 0

def generatePtera():
    global cont_ptera
    
    cont_ptera += 2
    if cont_ptera > 400 and len(ptera_group) < 3:
        ptera = Ptera()
        ptera_group.add(ptera)
        cont_ptera = 0

def generateCactus():
    global cont_cactus
    
    cont_cactus += 2
    if cont_cactus > 250 and len(cactus_group) < 3:
        cactus = Cactus()
        cactus_group.add(cactus)
        cont_cactus = 0

def generatorObstacle():
    global cont_spike
    hasSpike = False
    
    if len(spike_group) > 0:
        hasSpike = True

    if not hasSpike:
        cont_spike += 2
        if cont_spike > 1000 :
            spike = Spike()
            spike_group.add(spike)
            cont_spike = 0
    else:
        generatePtera()
        generateCactus()


    


   
    
    
    
