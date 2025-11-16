import time
from tkinter import *

windows = Tk()

windows.geometry('500x500')
windows.title("rac-developer")
icono = PhotoImage(file='icon.png')
windows.iconphoto(True, icono)
windows.config(background='#f2f2f2')

def update ():
    # Obtener la hora actual %H es la hora en formato 24 horas, %I es en formato 12 horas
    # %M son los minutos, %S son los segundos, %p es AM o PM
    time_string = time.strftime('%H:%M:%S %p')
    time_label.config(text=time_string)
    
    time_label.after(1000, update)  # Actualizar cada 1000 ms (1 segundo)

    day_string = time.strftime('%A')
    day_label.config(text=day_string)
    
    date_string = time.strftime('%B %d, %Y')
    date_label.config(text=date_string)

    print(time_string)

time_label = Label(windows, text='', font=('Arial', 50, ),fg='white' , bg="#161616")
time_label.pack()

day_label = Label(windows, font=('Ink Free', 25, ),fg="#161616")
day_label.pack()

date_label = Label(windows, font=('Ink Free', 25, ),fg="#161616")
date_label.pack()

update()

windows.mainloop()