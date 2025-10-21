from tkinter import *
# Importamos la siguiente librería para usar temas
from tkinter.ttk import *
import time

windows = Tk()

windows.geometry('500x500')
windows.title("rac-developer")
icono = PhotoImage(file='icon.png')
windows.iconphoto(True, icono)
windows.config(background='#f2f2f2')

def start():
    GB = 10
    dowloaded = 0
    speed = 1  # GB por segundo
    while (dowloaded < GB):
        time.sleep(0.05)
        # bar['value']+=10
        # dowloaded+=1
        bar['value'] += (speed / GB) * 100
        dowloaded += speed
        porcentaje.set(str(int((dowloaded/GB)*100)) + "% descargado")
        texto.set(str(dowloaded) + "/" + str(GB) + " GB descargados")
        windows.update_idletasks()

porcentaje = StringVar()
porcentaje.set("0% descargado")

texto = StringVar()
texto.set("0/0 GB descargados")
        
bar = Progressbar(windows, orient=HORIZONTAL, length=300)
bar.pack(padx=10, pady=10)

textoLabel = Label(windows, textvariable=porcentaje).pack(padx=10, pady=10)
comLabel = Label(windows, textvariable=texto).pack(padx=10, pady=10)

boton = Button(windows, text="Descargar", command=start).pack()

windows.mainloop()
