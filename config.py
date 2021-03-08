width = 800 
heigth = 600

Velocity = 6

FPS = 30

recordDistance = 0
currentDistance = 0

color = {"Black":(0,0,0),"White":(255,255,255)}

reference = 'assets/sprites/ok.png'


time = 1
def spriteSwap(group, interval=5, i=0):
    global time
    
    time -= 1
    image = group[0]
    if time == 0:
        time = interval
        image = group[i]
    return image

    
