from tkinter import *

windows = Tk()

windows.geometry('500x500')
windows.title("rac-developer")
icono = PhotoImage(file='icon.png')
windows.iconphoto(True, icono)
windows.config(background='#f2f2f2')

# 1era forma usando python nativo

def move_up(event):
    canvas.move(miImagen, 0, -10)

def move_down(event):
    canvas.move(miImagen, 0, +10)

def move_left(event):
    canvas.move(miImagen, -10, 0)
    
def move_right(event):
    canvas.move(miImagen, +10, 0)

windows.bind("<w>", move_up)
windows.bind("<s>", move_down)
windows.bind("<a>", move_left)
windows.bind("<d>", move_right)

windows.bind("<Up>", move_up)
windows.bind("<Down>", move_down)
windows.bind("<Left>", move_left)
windows.bind("<Right>", move_right)

canvas = Canvas(windows, width=500, height=500)
canvas.pack()

miImagen = canvas.create_image(0,0,image=icono, anchor=NW)

windows.mainloop()