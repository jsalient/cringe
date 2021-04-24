from pygame import *

win_width = 1200
win_height = 600

img_back = "bg.png"

window = display.set_mode((win_width, win_height))
background = transform.scale(image.load(img_back), (win_width, win_height))

finish = False

run = True
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False

    if not finish:
        window.blit(background,(0,0))
        display.update()
    time.delay(50)
        

