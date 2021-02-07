width = 800 
heigth = 600

Velocity = 6

FPS = 30

recordDistance = 0
currentDistance = 0

color = {"Black":(0,0,0),"White":(255,255,255)}

reference = 'assets/sprites/ok.png'


index = 0
time = 1
def spriteSwap(group, interval=5):
    global time    
    global index 
    
    time -= 1
    image = group[0]
    if time == 0:
        time = interval
        index += 1
        image = group[index]
        if index >= len(group):
            index = 0
    return image

    
