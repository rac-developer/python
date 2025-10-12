from tkinter import *

windows = Tk()

windows.geometry('500x500')
windows.title("rac-developer")
icono = PhotoImage(file='icon.png')
windows.iconphoto(True, icono)
windows.config(background='#f2f2f2')

def abrirArchivo():
    print("Abrir archivo")

def guardarArchivo():
    print("Guardar archivo")

def recortar():
    print("Recortar")

def copiar():
    print("Copiar")

def pegar():
    print("Pegar")

openImage = PhotoImage(file='open.png')
saveImage = PhotoImage(file='save.png')
exitImage = PhotoImage(file='exit.png')

menubar = Menu(windows)
windows.config(menu=menubar)

fileMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="Open", command=abrirArchivo, image=openImage, compound='left')
fileMenu.add_command(label="Save", command=guardarArchivo, image=saveImage, compound='left')
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=windows.quit, image=exitImage, compound='left')

editMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Cut", command=recortar)
editMenu.add_command(label="Copy", command=copiar)
editMenu.add_command(label="Paste", command=pegar)

windows.mainloop()
