from tkinter import Canvas, IntVar, Tk
from PIL import ImageTk, Image
import random
from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder


def move(char, item):
    print("start!")
    item = item.lower()
    # pathfind to all available item and move to the closest one
    if item == "power":
        item = "p"
    elif item == "base":
        item = "b"
    elif item == "enemy":
        item = "e"
    elif item == "player":
        item = "u"
    items = []
    for xq, j in enumerate(tiles):
        for yq, l in enumerate(j):
            if l == item:
                items.append([xq, yq])
    print(items)
    for i in items:
        grid = Grid(matrix=tile_movecost)
        start = grid.node(0, 0)
        end = grid.node(i[1], i[0])
        finder = AStarFinder(diagonal_movement=DiagonalMovement.never)
        path, runs = finder.find_path(start, end, grid)
        tries.append(path)
        print(grid.grid_str(path=path, start=start, end=end))
    for b in path:  # type: ignore
        x, y = b[0]*32, b[1]*32
        print(x, y)
        print(canvas.moveto(char, x, y))
        waithere(300)


tries = []


def waithere(time):
    var = IntVar()
    root.after(time, var.set, 1)
    root.wait_variable(var)


tile_movecost = [0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1,
                 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1,
                 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1,
                 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1,
                 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1,
                 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0,
                 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1,
                 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1,
                 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1,
                 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1,
                 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1,
                 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0,
                 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1,
                 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
                 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1,
                 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0,
                 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1,
                 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1,
                 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1,
                 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

def main():
    print("Press w, a, s, d to move the rectangle")
    root.after(1000)
    move(player, "bAse")


root = Tk()
root.title("My first GUI")
root.geometry("800x800")
canvas = Canvas(root, width=640, height=640, bg="red")

map = ImageTk.PhotoImage(Image.open("map.png").resize((640, 640)))
canvas.create_image(0, 0, image=map, anchor="nw")
base = canvas.create_rectangle(96, 512, 128, 544, fill="green")
player = canvas.create_rectangle(0, 0, 32, 32, fill="blue")
canvas.pack()
root.after(500, main)
root.mainloop()
