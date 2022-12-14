from tkinter import Canvas, Tk
from PIL import ImageTk, Image
import random
root = Tk()
canvas = Canvas(root, width=512, height=512, bg="red")

grid1 = [20,20]
matrix = []
for i in range(grid1[0]):
            matrix.append([])
            for j in range(grid1[1]):
                rand = random.randint(1, 72)
                if rand-60 >0:
                    tyle= [2, rand-60]
                elif rand-30 >0:
                    tyle= [1, rand-30]
                else:
                    tyle= [0, rand]
                matrix[i].append(tyle)
tileset = Image.open("Tileset.jpg")
image_tile = []
for i in range(grid1[0]):
        image_tile.append([])
        print(image_tile)
        for j in range(grid1[1]):
                tiletop, tileleft = i*32, j*32
                top, left = matrix[i][j][0]*16, matrix[i][j][1]*16
                tile = tileset.crop((left, top, left+16, top+16)).resize((32, 32))
                image_tile[i].append(ImageTk.PhotoImage(tile))
                print(canvas.create_image(tiletop, tileleft, image=image_tile[i][j], anchor="nw"))
canvas.pack()
root.mainloop()