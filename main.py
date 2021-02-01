import pygame as py
from player import dino_group
from background import ground_group, cloud_group, renderCloud
from other import Gravity 

import Obstacle.generatorObst as ob



py.init()

width = 800
heigth = 600
FPS = 30

Cor = {"Preto":(0,0,0),"Branco":(255,255,255)}

screen = py.display.set_mode((width, heigth))




clock = py.time.Clock()
while True:
    clock.tick(FPS)
    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()

    renderCloud()
    Gravity()
    
    ob.generatorObstacle()
    

    screen.fill(Cor["Preto"])

    ob.cactus_group.update()
    ob.ptera_group.update()
    dino_group.update()
    ground_group.update()
    cloud_group.update()
    ob.spike_group.update()
    
    ob.spike_group.draw(screen)
    ob.cactus_group.draw(screen)
    ob.ptera_group.draw(screen)
    ground_group.draw(screen)
    dino_group.draw(screen)
    cloud_group.draw(screen)
    

    py.display.update()