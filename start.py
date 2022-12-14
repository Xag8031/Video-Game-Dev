from tkinter import Tk, Canvas, Button
from PIL import Image, ImageTk

root = Tk()
img = Image.open('./Images/Map-title.png').resize((32*20, 32*20))
img = ImageTk.PhotoImage(img)
canvas = Canvas(root, width=32*20, height=32*20)
canvas.create_image(0, 0, anchor='nw', image=img)
Start = Button(root, text='Start', width=40, height=5, command=lambda: print("Start"))
Editor = Button(root, text='Editor', width=40, height=5, command=lambda: print("Editor"))
canvas.pack()
root.after(1000, lambda: Start.place(x=root.winfo_width()/5, y=root.winfo_height()/1.75))
root.after(1000, lambda: Editor.place(x=root.winfo_width()/1.5, y=root.winfo_height()/1.75))
root.mainloop()
