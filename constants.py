import pygame as py
from background import ground_group
from generator import cactus_group, ptera_group, spike_group
from player import Dino

from config import currentDistance, recordDistance, color, Velocity, width, heigth, reference, spriteSwap
   
            
def colisionEnemies():
    isGround = py.sprite.spritecollide(Dino, ground_group, False, collided = None)
    if isGround:
        Dino.state = 1
    

        if Dino.JUMP_DURING_TIME == 0:
            Dino.JUMP_DURING_TIME = 14
            Dino.state = 0

    collidedCactus = py.sprite.spritecollide(Dino, cactus_group, False, collided = None)
    collidedPtera = py.sprite.spritecollide(Dino, ptera_group, False, collided = None)
    collidedSpike = py.sprite.spritecollide(Dino, spike_group, False, collided = None)
    
    if collidedCactus or collidedPtera or collidedSpike:
        Dino.isDead = True


py.font.init()
font = py.font.get_default_font()
msg1 = py.font.SysFont(font, 20) 

text1 = msg1.render("Current Distance: " + str(currentDistance), 1,(color["White"]))
text2 = msg1.render("Record Distance: " + str(recordDistance), 1,(color["White"]))


def updateMessage(screen):
    global Velocity
    global recordDistance
    global text1
    global text2
    global currentDistance

    if not Dino.isDead:
        currentDistance += Velocity
        text1 = msg1.render("Current Distance " + str(f"{currentDistance:.0f}"), 1,(color["White"]))
    
    if currentDistance > recordDistance:
        recordDistance = currentDistance
        text2 = msg1.render("Record Distance: " + str(f"{recordDistance:.0f}"), 1,(color["White"]))

    if Velocity < 10 and not Dino.isDead:
        Velocity = Velocity + 0.0005

    screen.blit(text1,(10, 320))
    screen.blit(text2,(10, 340))

    if currentDistance > 1200 and currentDistance < 2000:
        screen.blit(py.image.load(reference), (-120, 300))


class Restart(py.sprite.Sprite):
    def __init__(self):
        py.sprite.Sprite.__init__(self)
        self.images = [py.image.load('assets/sprites/Replay2.png'),
                py.image.load('assets/sprites/Replay3.png'),
                py.image.load('assets/sprites/Replay4.png'),
                py.image.load('assets/sprites/Replay1.png')]

        self.image = py.image.load('assets/sprites/Replay2.png')
        self.game_over = 'assets/sprites/game_over.png'
        self.rect = self.image.get_rect()
        self.rect[0] = 350
        self.rect[1] = heigth/2
        self.index = 0
        self.time = 15

    def update(self, screen):
        if Dino.isDead: 
            self.time -= 1
            restart_group.draw(screen)
            screen.blit(py.image.load(self.game_over), (220, 250))
            if self.time == 0:
                self.image = spriteSwap(self.images, self.index)
                self.index += 1
                if self.index >= len(self.images):
                    self.index = 0
                self.time = 15

            if insideRestart():
                if py.mouse.get_pressed()[0]:
                    InitializeNewMatch()
    def draw(self):
        print(1)

restart_group = py.sprite.Group()
res = Restart()
restart_group.add(res)    

# if the mouse is within the coordinates of the restant
def insideRestart():
    isTrue = 0
    if py.mouse.get_pos()[0] > 350 and py.mouse.get_pos()[0] < 440:
        isTrue += 1
    if py.mouse.get_pos()[1] > 300 and py.mouse.get_pos()[1] < 380:
         isTrue += 1
    
    return isTrue == 2    
        
# Initialize New Game
def InitializeNewMatch():
    global Velocity
    global currentDistance
    currentDistance = 0
    Dino.isDead = False
    Dino.rect[0] = 200
    Dino.rect[1] = 300
    Velocity = 4
    Dino.state = 0
    
    py.sprite.Group.empty(cactus_group) 
    py.sprite.Group.empty(spike_group) 
    py.sprite.Group.empty(ptera_group)
 