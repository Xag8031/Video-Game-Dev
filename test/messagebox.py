from tkinter import messagebox, Tk, Label

root = Tk()

abcd = messagebox.askquestion(title="Code Creeps!", message="Do you want to play in Key mode?")
text = Label(root, text=abcd)
text.pack()
root.mainloop()