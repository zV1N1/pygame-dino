import pygame as py
from background import ground_group
from player import Dino

def Gravity():
    isGround = py.sprite.spritecollide(Dino, ground_group, False, collided = None)
    for i in isGround:
       Dino.speedY = 0
        