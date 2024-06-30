import pgzrun

WIDTH = 300
HEIGHT = 300


def draw():
    length = 280
    width = 100
    for i in range(7):
        rect = Rect((50,230), (length,width))
        rect.center = 150,150
        screen.draw.rect(rect, 'white')
        length = length-15
        width = width+15







def update():
    #functinality
    pass


pgzrun.go()