from time import sleep
from tkinter import Tk, Canvas
from playsound import playsound
import multiprocessing
from PIL import Image, ImageTk

global p1, root
#map stuff
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

#Plays background audio
def game_audio():
    playsound('lady-of-the-80x27s-128379.mp3')


#Moves the background image around the character
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
#Title screen
#Need to add editor button
#Need to Create a custom close button
def start():
    root = Tk()
    img = Image.open('./Images/Map-title.png').resize((32*20, 32*20))
    img = ImageTk.PhotoImage(img)
    canvas = Canvas(root, width=32*20, height=32*20)
    canvas.create_image(0, 0, anchor='nw', image=img)
    Start = Button(root, text='Start', width=40, height=5, command=lambda: middle())
    Editor = button(root, text='Editor', width=40, height=5, command=lambda: editor())
    canvas.pack()
    root.after(1000, lambda: Start.place(x=root.winfo_width()/5, y=root.winfo_height()/1.75))
    root.after(1000, lambda: Editor.place(x=root.winfo_width()/1.5, y=root.winfo_height()/1.75))
    root.mainloop()

# game screen
def middle():
    global root, p1, canvas, map_canvas, player, play, game_map, playerx, playery
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
p2 = multiprocessing.Process(target=middle)
p2.start()
