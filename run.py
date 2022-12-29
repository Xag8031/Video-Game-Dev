"This game is a maze game where you have to find the hidden flag to win the game."


import multiprocessing
import os
from tkinter import Button, Canvas, Tk, messagebox
from PIL import Image, ImageTk
from playsound import playsound
import subprocess



# map stuff
playerx, playery = 0, 0
game_map = [
    [0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
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
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]
points = []
with open("points.txt", encoding="utf-8") as file_data:
    points.append(file_data.read().split("\n"))
POINT = 0

# TODO: Add Look to code mode.
# TODO: Add Look to key mode.
# TODO: Add return button to editor.
# TODO: Add Audio to Middle.
# TODO: Add message box for Audio on or off.
# TODO: Add points to game finder?
# TODO: Add a way to gain points.
# TODO: Need to add editor to app.
# TODO: Need to Create a custom close button


# Plays background audio
def game_audio():
    """Plays the specified audio file in a separate process."""
    subprocess.run(['playsound', "lady-of-the-80x27s-128379.mp3"])


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
    else:
        print("Not a Moveable Space")
    flags(POINT)


def move_code(movement, playerx, playery): # pylint: disable=W0621
    """This is the code to move the character in code mode

    Args:
        movement (str): this is the movement that the player will take
    """
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
    else:
        print("Not a Moveable Space")
    flags(POINT)


def flags(point):
    """Checks if the player has reached a flag"""
    if points[point] == [playery, playerx]:
        point = point + 1


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
        lambda: Editor.place(x=root.winfo_width() / 1.5, y=root.winfo_height() / 1.75),
    )
    root.mainloop()


def code_editor():
    """This will be the code editor for the game if used"""
    root.destroy()
    # run a python file that will open the code editor cross platform
    os.system("python3 code_editor.py")


def before_middle():
    """Asks the player if they want to play in key mode or code mode"""
    key_mode = messagebox.askquestion(
        title="Code Creeps!", message="Do you want to play in Key mode?"
    )
    audio_mode = messagebox.askquestion(
        title="Code Creeps!", message="Do you want to play with Audio?"
    )
    if audio_mode == "yes":
        audio_file.start()
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
    if key_mode == "yes":
        Game_Canvas.bind_all("<Key>", move_key)
    else:
        done = []
        with open("code.creeps", encoding="utf-8") as data_of_file:
            for line in data_of_file:
                if line[0] != ";":
                    command = line.strip()
                    parts = command.split("(")
                    name = parts[0]
                    argument = parts[1][:-1]
                    done.append([name, argument])
        for i in done:
            if i[0] == "move":
                move_code(i[1], playerx, playery)
    Game_Canvas.create_image(288, 288, image=player, anchor="nw")
    Game_Canvas.pack()


def on_closing():
    """Checks if the window is trying to close then asks the player if they want to quit"""
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()
        audio_file.terminate()


root = Tk()
img = ImageTk.PhotoImage(
    Image.open("./Images/Map-title.png").resize((32 * 20, 32 * 20))
)
canvas = Canvas(root, width=32 * 20, height=32 * 20)
Game_Canvas = Canvas(root, width=640, height=640, bg="lime")
Map_image = ImageTk.PhotoImage(Image.open("./Images/Map.png").resize((2560, 2560)))
map_canvas = Game_Canvas.create_image(256, 256, image=Map_image, anchor="nw")
start_button = Button(
    root, text="Start", width=40, height=5, command=lambda: before_middle() # pylint: disable=W0108
)
Editor = Button(
    root, text="Editor", width=40, height=5, command=lambda: code_editor() # pylint: disable=W0108
)
root.protocol("WM_DELETE_WINDOW", on_closing)
player = ImageTk.PhotoImage(Image.open("./Images/Char.png").resize((64, 64)))
audio_file = multiprocessing.Process(target=game_audio)
title()
