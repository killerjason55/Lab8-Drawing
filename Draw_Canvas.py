from tkinter import *

def point(event):
    canvas.create_oval(event.x,event.y,event.x + 1, event.y + 1,width=10)

def clear():
    canvas.delete("all")

root = Tk()

canvas = Canvas(root, width = 400,height=400)
canvas.pack()

label = Label(root,text="Drage mouse to draw")
label.pack()

button = Button(root,text="Clear",command=clear)
button.pack(fill = "both")

canvas.bind("<B1-Motion>",point)

root.mainloop()
