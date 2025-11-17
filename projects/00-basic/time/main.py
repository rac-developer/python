from tkinter import *
from time import *

def update():
    time_string = strftime("%I:%M:%S %p")
    time_label.config(text=time_string) 
    
    time_label.after(1000, update)  # Actualizar cada 1000 ms (1 segundo)
    
window = Tk()
window.title("RAC Developer - Reloj")

time_label = Label(window, font=("Arial", 50), fg="white", bg="#161616")
time_label.pack()

update()

window.mainloop()