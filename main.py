import pygame as py
from player import dino_group
from background import ground_group, cloud_group, renderCloud
from constants import updateMessage, colisionEnemies, restart

from config import (width, heigth, color, FPS)

from generator import (generatorObstacle, cactus_group, 
ptera_group, spike_group)


py.init()

screen = py.display.set_mode((width, heigth))

    




clock = py.time.Clock()
while True:
    clock.tick(FPS)
    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()

    screen.fill(color["Black"])
    
    renderCloud()  
    generatorObstacle()
    updateMessage(screen)
    colisionEnemies()
    restart(screen)

    cactus_group.update()
    ptera_group.update()
    dino_group.update()
    ground_group.update()
    cloud_group.update()
    spike_group.update()
    
    spike_group.draw(screen)
    cactus_group.draw(screen)
    ptera_group.draw(screen)
    ground_group.draw(screen)
    dino_group.draw(screen)
    cloud_group.draw(screen)
    

    py.display.update()