import pygame as py


class Dinossauro(py.sprite.Sprite):
    def __init__(self):
        py.sprite.Sprite.__init__(self)
        self.imagens = [py.image.load('assets/sprites/1.png'),
                        py.image.load('assets/sprites/2.png')]
        self.imagensAviao = [py.image.load('./assets/sprites/aviao0.png'),
                             py.image.load('./assets/sprites/aviao1.png')]
        self.imagensAbaixa = [py.image.load('./assets/sprites/1ab.png'),
                              py.image.load('./assets/sprites/2ab.png')]
        self.image = py.image.load('./assets/sprites/1.png')
        self.rect = self.image.get_rect()
        self.rect[0] = 200
        self.rect[1] = 300
        self.index = 0
        self.speedY = 3
        self.AviaoDeslocamento = 0
        self. AviaoCooldown = 0
        self.Estado = 0
        self.Largura = 40
        self.Altura = 43
    def update(self):
        self.rect[1] += self.speedY
        self.index += 1
        if self.index >= len(self.imagens):
            self.index = 0
        if self.Estado == 0:
            self.image = self.imagens[self.index]
        
        if Dino.Estado == 1:
            self.image = self.imagensAbaixa[self.index]
            self.rect[1] = 615

        if Dino.Estado == 3:
            self.image = py.image.load('DinossauroSprites/3.png')

        if Dino.Estado == 4:
            self.image = self.imagensAviao[self.index]

dino_group = py.sprite.Group()
Dino = Dinossauro()
dino_group.add(Dino)


