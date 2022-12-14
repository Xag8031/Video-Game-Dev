from time import sleep
from tkinter import Tk, Canvas
from playsound import playsound
import multiprocessing
from PIL import Image, ImageTk

global p1, root

playerx, playery = 0, 0
game_map = [[0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
            [0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1],
            [0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1],
            [0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1],
            [0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1],
            [0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1],
            [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1],
            [1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1],
            [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
            [0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
            [0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1],
            [0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
            [0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1],
            [0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1],
            [1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]


def game_audio():
    playsound('lady-of-the-80x27s-128379.mp3')


# create a movement function that moves the map by 128 but only if the space is not a 1
def move(event):
    global playerx, playery
    if event.keysym == "Up" and game_map[playery - 1][playerx] != 1:
        canvas.move(map_canvas, 0, 128)
        playery -= 1
    if event.keysym == "Down" and game_map[playery + 1][playerx] != 1:
        canvas.move(map_canvas, 0, -128)
        playery += 1
    if event.keysym == "Left" and game_map[playery][playerx - 1] != 1:
        canvas.move(map_canvas, 128, 0)
        playerx -= 1
    if event.keysym == "Right" and game_map[playery][playerx + 1] != 1:
        canvas.move(map_canvas, -128, 0)
        playerx += 1


def main():
    global canvas, map_canvas
    root = Tk()
    root.title("Code Creeps!")
    root.geometry("640x640")
    root.configure(background="black")
    canvas = Canvas(root, width=640, height=640, bg="lime")
    canvas.bind_all('<Key>', move)
    map = ImageTk.PhotoImage(Image.open(
        "./Images/Map.png").resize((2560, 2560)))
    map_canvas = canvas.create_image(256, 256, image=map, anchor="nw")
    player = ImageTk.PhotoImage(Image.open(
        "./Images/Char.png").resize((64, 64)))
    play = canvas.create_image(288, 288, image=player, anchor="nw")
    canvas.pack()
    root.mainloop()
    p1.kill()


p1 = multiprocessing.Process(target=game_audio)
p1.start()
p2 = multiprocessing.Process(target=main)
p2.start()
