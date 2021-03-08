import pygame as py

from config import Velocity, spriteSwap

class Dinossauro(py.sprite.Sprite):
    def __init__(self):
        py.sprite.Sprite.__init__(self)
        self.imagens = [py.image.load('assets/sprites/1.png'),
                        py.image.load('assets/sprites/2.png')]
        self.airplane = [py.image.load('./assets/sprites/airplane1.png'),
                             py.image.load('./assets/sprites/airplane2.png')]
        self.image = py.image.load('./assets/sprites/1.png')
        self.rect = self.image.get_rect()
        self.rect[0] = 200
        self.rect[1] = 300
        self.speedY = 4
        self.AirplaneTime = 0
        self.AirplaneCooldown = 0
        self.state = 0 # 1- Run/ 2- Jump/ 3-Down/ 4- Flying 
        self.JUMP_DURING_TIME = 14
        self.isDead = False
        self.index = 0
    def update(self):
        if not self.isDead:
            if self.state == 1:
                self.image = spriteSwap(self.imagens, 5, self.index)
                self.index += 1
                if self.index >= 2:
                    self.index = 0
                
                
            if py.key.get_pressed()[py.K_UP]:
                if self.state == 1:
                    self.state = 2
            if py.key.get_pressed()[py.K_SPACE]:
                if self.AirplaneCooldown < 1:
                    self.state = 4            
        else:      
            self.rect[0] -= Velocity
    
        dinoBehavior()

dino_group = py.sprite.Group()
Dino = Dinossauro()
dino_group.add(Dino)     
                    
JUMP_DURING_TIME = 0
def dinoBehavior():
    if Dino.state == 0:
        Dino.rect[1] += Dino.speedY

    if Dino.state == 2:
            Dino.image = Dino.imagens[0]
            if Dino.JUMP_DURING_TIME > 0:
                Dino.JUMP_DURING_TIME -= 1
                Dino.rect[1] -= 6
            else:
                Dino.state = 0
                if py.key.get_pressed()[py.K_DOWN]:
                    Dino.rect[1] += 3         

    if Dino.state == 4:
        Dino.image = spriteSwap(Dino.airplane)
        if Dino.AirplaneTime <= 820:
            Dino.AirplaneTime += Velocity
            if Dino.AirplaneTime <= 50:
                Dino.rect[1] -= 5      
        else:
            Dino.state = 0
            Dino.AirplaneTime = 0    
            Dino.Cooldown = 2000
    else:
        Dino.AirplaneCooldown -= Velocity 
