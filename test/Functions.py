from run1 import *


def move(event):
    if event.char == "w":
        canvas.move(ALL, 0,  -20)
    elif event.char == "a":
        canvas.move(ALL,  -20, 0)
    elif event.char == "s":
        canvas.move(ALL, 0, 20)
    elif event.char == "d":
        canvas.move(ALL, 20, 0)