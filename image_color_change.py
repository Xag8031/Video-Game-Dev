import numpy as np
from PIL import Image, ImageTk
from tkinter import Tk, Canvas, NW

root = Tk()

im = Image.open('Untitled.png')
data = np.array(im)

r1, g1, b1 = 255, 255, 255  # Original value
r2, g2, b2 = 45, 34, 67  # Value that we want to replace it with

red, green, blue = data[:, :, 0], data[:, :, 1], data[:, :, 2]
mask = (red == r1) & (green == g1) & (blue == b1)
data[:, :, :3][mask] = [r2, g2, b2]

im = Image.fromarray(data)
im = ImageTk.PhotoImage(im)
canvas = Canvas(width="400")
canvas.create_image(0, 0, anchor=NW, image=im)

canvas.pack()
root.mainloop()
