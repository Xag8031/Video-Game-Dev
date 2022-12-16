#from time import sleep
from tkinter import Tk, Canvas, Button, messagebox
#from playsound import playsound
#import multiprocessing
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

#TODO: Add Code Mode.
#TODO: Add Editor To screen.
#TODO: Add Audio to Middle.
#TODO: Add message box for Audio on or off.

#Plays background audio
#def game_audio():
#    playsound('lady-of-the-80x27s-128379.mp3')


#Moves the background image around the character
def move_key(event):
    global playerx, playery, Game_Canvas, map_canvas
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
    else: print("Not a Moveable Space")
#Title screen
#Need to add editor to app
#Need to Create a custom close button
def Title():
    global root, canvas, Editor, start_button, code_editor
    root = Tk()
    root.title("Code Creeps!")
    root.geometry("640x640")
    root.configure(background="black")
    img = Image.open('./Images/Map-title.png').resize((32*20, 32*20))
    img = ImageTk.PhotoImage(img)
    canvas = Canvas(root, width=32*20, height=32*20)
    canvas.create_image(0, 0, anchor='nw', image=img)
    start_button = Button(root, text='Start', width=40, height=5, command=lambda: before_middle()) # type: ignore
    Editor = Button(root, text='Editor', width=40, height=5, command=lambda: code_editor()) # type: ignore
    canvas.pack()
    root.after(1000, lambda: start_button.place(x=root.winfo_width()/5, y=root.winfo_height()/1.75))
    
    root.after(1000, lambda: Editor.place(x=root.winfo_width()/1.5, y=root.winfo_height()/1.75))
    root.mainloop()
    #p1.kill()

def code_editor():
    pass
def before_middle():
    global key_mode
    key_mode = messagebox.askquestion(title="Code Creeps!", message="Do you want to play in Key mode?")
    middle(key_mode)
# game screen
def middle(key_mode):
    global root, Game_Canvas, map_canvas, canvas, Editor, start_button, player, map_image
    Editor.place_forget()
    start_button.place_forget()
    #p1.start()
    canvas.pack_forget()
    Game_Canvas = Canvas(root, width=640, height=640, bg="lime")
    if key_mode == "yes": 
        Game_Canvas.bind_all('<Key>', move_key)
    else: 
        print("Code Mode")
    map_image = ImageTk.PhotoImage(Image.open("./Images/Map.png").resize((2560, 2560)))
    map_canvas = Game_Canvas.create_image(256, 256, image=map_image, anchor="nw")
    player = ImageTk.PhotoImage(Image.open("./Images/Char.png").resize((64, 64)))
    Game_Canvas.create_image(288, 288, image=player, anchor="nw")
    Game_Canvas.pack()
  
#p1 = multiprocessing.Process(target=game_audio())   
Title()
