"This game is a maze game where you have to find the hidden flag to win the game."

import os
import threading
import wave
from tkinter import Button, Canvas, Tk, messagebox, Label
import tkinter as tk

import pyaudio
from PIL import Image, ImageTk

p = pyaudio.PyAudio()
stream = None

# map stuff
playerx, playery = 0, 0
game_map = [
    [0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
    [0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1],
    [0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1],
    [0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1],
    [0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1],
    [0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1],
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
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]
x, y = 0, 0
# points stuff
points = [
    [13, 13],
    [8, 18],
    [11, 13],
    [16, 14],
    [16, 2],
    [2, 15],
    [8, 13],
    [4, 18],
    [12, 6],
    [16, 7],
    [16, 4],
    [18, 8],
    [14, 9],
    [3, 3],
    [5, 5],
    [18, 4],
    [13, 4],
    [16, 9],
    [2, 9],
    [18, 15],
    [9, 13],
    [17, 3],
    [17, 11],
    [15, 5],
    [2, 1],
    [17, 13],
    [15, 7],
    [12, 17],
    [10, 11],
    [16, 11]]
#points = [
#    [13, 13],
#    [8, 18],
#    [11, 13],
#    [16, 14],
#    [16, 2]] #overriding points for shorter game
POINT = 0

# TODO: Add return button to editor.


def tksleep(t):
    'emulating time.sleep(seconds)'
    ms = int(t*1000)
    var = tk.IntVar()
    root = tk._get_default_root('sleep')  # type: ignore
    root.after(ms, var.set, 1)
    root.wait_variable(var)

# Moves the background image around the character


def move_key(event):
    """This is the code to move the character in key mode

    Args:
        event (KeyPress): What button the player presses
    """
    global playerx, playery  # pylint: disable=C0103,W0603
    if event.keysym == "Up" and game_map[playery - 1][playerx] != 1:
        Game_Canvas.move(map_canvas, 0, 128)

        playery -= 1
    elif event.keysym == "Down" and game_map[playery + 1][playerx] != 1:
        Game_Canvas.move(map_canvas, 0, -128)
        playery += 1
    elif event.keysym == "Left" and game_map[playery][playerx - 1] != 1:
        Game_Canvas.move(map_canvas, 128, 0)
        playerx -= 1
    elif event.keysym == "Right" and game_map[playery][playerx + 1] != 1:
        Game_Canvas.move(map_canvas, -128, 0)
        playerx += 1
    pos_lable["text"] = f"Player Position: [{playerx},{playery}]"
    pos_lable.update("Code Creeps!", "You Just got a point!")
    poi_lable["text"] = f"Points: {points[POINT]}"
    poi_lable.update()
    flags()


def move_code(movement):  # pylint: disable=W0621
    """This is the code to move the character in code mode

    Args:
        movement (str): this is the movement that the player will take
    """
    global playerx, playery  # pylint: disable=C0103,W0603
    if movement == "up" and game_map[playery - 1][playerx] != 1:
        Game_Canvas.move(map_canvas, 0, 128)

        playery -= 1
    elif movement == "down" and game_map[playery + 1][playerx] != 1:
        Game_Canvas.move(map_canvas, 0, -128)
        playery += 1
    elif movement == "left" and game_map[playery][playerx - 1] != 1:
        Game_Canvas.move(map_canvas, 128, 0)
        playerx -= 1
    elif movement == "right" and game_map[playery][playerx + 1] != 1:
        Game_Canvas.move(map_canvas, -128, 0)
        playerx += 1
    flags()


def flags():
    global POINT
    """Checks if the player has reached a flag"""
    x = [playery, playerx]
    if all(item in points[POINT] for item in x):
        POINT = POINT + 1
        messagebox.showinfo()
    if POINT == len(points):
        game_end()
    pos_lable["text"] = f"Player Position: [{playerx},{playery}]"
    pos_lable.update()
    poi_lable["text"] = f"Points: {points[POINT]}"
    poi_lable.update()


def title():
    """This is the title screen for the game"""
    root.title("Code Creeps!")
    root.geometry("640x640")
    root.configure(background="black")
    canvas.create_image(0, 0, anchor="nw", image=img)
    canvas.pack()
    root.after(
        1000,
        lambda: start_button.place(
            x=root.winfo_width() / 5, y=root.winfo_height() / 1.75
        ),
    )
    root.after(
        1000,
        lambda: Editor.place(x=root.winfo_width() / 1.5,
                             y=root.winfo_height() / 1.75),
    )
    root.mainloop()


def code_editor():
    """This will be the code editor for the game if used"""
    root.destroy()
    # run a python file that will open the code editor cross platform
    os.system("python3 code_editor.py")


def play_wav(filepath):
    global stream
    # Open the WAV file
    with wave.open(filepath, "rb") as file:
        # Initialize PyAudio
        global p
        p = pyaudio.PyAudio()

        # Open a streaming module
        stream = p.open(format=p.get_format_from_width(file.getsampwidth()),
                        channels=file.getnchannels(),
                        rate=file.getframerate(),
                        output=True)

        # Read and play the WAV file in a loop
        while True:
            file.rewind()
            data = file.readframes(1024)
            while data:
                stream.write(data)
                data = file.readframes(1024)


def before_middle():
    """Asks the player if they want to play in key mode or code mode"""
    key_mode = messagebox.askquestion(
        title="Code Creeps!", message="Do you want to play in Key mode?"
    )
    audio_mode = messagebox.askquestion(
        title="Code Creeps!", message="Do you want to play with Audio?"
    )
    if key_mode == "yes":
        messagebox.showinfo(
            title="Code Creeps!", message="Use the arrow keys to move around"
        )
    messagebox.showinfo(
        title="Code Creeps!", message="Go to the hidden flags to win the game"
    )
    if audio_mode == "yes":
        thread = threading.Thread(target=play_wav, args=("audio.wav",))
        thread.start()
    middle(key_mode)


# game screen


def middle(key_mode):
    """This is the game screen, it is called middle because it is in the middle of the app

    Args:
        key_mode (bool): This is the mode that the player will play in
    """
    Editor.place_forget()
    start_button.place_forget()
    canvas.pack_forget()
    pos_lable.place(x=0, y=0)
    poi_lable.place(x=0, y=20)
    Game_Canvas.create_image(288, 288, image=player, anchor="nw")
    Game_Canvas.pack()
    if key_mode == "yes":
        Game_Canvas.bind_all("<Key>", move_key)
    else:
        done = []
        with open("code.creeps", encoding="utf-8") as data_of_file:
            for line in data_of_file:
                if line[0] != "#":
                    command = line.strip()
                    move_code(command)
                    tksleep(0.5)


def game_end():
    """This is the end screen for the game"""
    Game_Canvas.pack_forget()
    messagebox.showerror(title="Code Creeps!",
                         message="You have won the game!")
    on_closing()


def on_closing():
    global stream
    """Checks if the window is trying to close then asks the player if they want to quit"""
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()
        stream.stop_stream()  # type: ignore
        p.terminate()


root = Tk()
img = ImageTk.PhotoImage(
    Image.open("./Images/Map-title.png").resize((32 * 20, 32 * 20))
)
canvas = Canvas(root, width=32 * 20, height=32 * 20)
Game_Canvas = Canvas(root, width=640, height=640, bg="lime")
Map_image = ImageTk.PhotoImage(Image.open(
    "./Images/Map.png").resize((2560, 2560)))
map_canvas = Game_Canvas.create_image(256, 256, image=Map_image, anchor="nw")
start_button = Button(
    root, text="Start", width=40, height=5, command=lambda: before_middle()  # pylint: disable=W0108
)
Editor = Button(
    root, text="Editor", width=40, height=5, command=lambda: code_editor()  # pylint: disable=W0108
)

pos_lable = Label(
    root, text=f"Player position: [{playerx}, {playery}]", bg="black", fg="white",)
poi_lable = Label(
    root, text=f"Points: {points[POINT]}", bg="black", fg="white",)

root.protocol("WM_DELETE_WINDOW", on_closing)
player = ImageTk.PhotoImage(Image.open("./Images/Char.png").resize((64, 64)))
title()
