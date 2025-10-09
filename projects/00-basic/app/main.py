from tkinter import *
# Debemos importar el messagebox
from tkinter import messagebox

windows = Tk()

windows.geometry('500x500')
windows.title("rac-developer")
icono = PhotoImage(file='icon.png')
windows.iconphoto(True, icono)
windows.config(background='#f2f2f2')

def click():
    # Mostramos un mensaje de información
    messagebox.showinfo(title="Information", message="Button clicked!")

def warning():
    # Mostramos un mensaje de advertencia
    # messagebox.showwarning(title="Warning", message="This is a warning message!")
    
    # Bucle infinito de mensajes de advertencia
    while True:
        messagebox.showwarning(title="Warning", message="This is a warning message!")
        
def error():
    # Mostramos un mensaje de error
    messagebox.showerror(title="Error", message="This is an error message!")
    
def ask():
    # Preguntamos al usuario una pregunta
    # messagebox.askquestion(title="Question", message="Do you like Python?")
    
    # Vemos lo botones de cancelar o reintentar
    # if (messagebox.askretrycancel(title="Retry or Cancel", message="Do you want to retry?")):
    #     print("Retry")
    # else:
    #     print("Cancel")

    # Vemos los botones de si o no
    # preguntas = messagebox.askquestion(title="Yes or No", message="Do you like Python?")
    
    # if (preguntas == 'yes'):
    #     print("You like Python")
    # elif (preguntas == 'no'):
    #     print("You don't like Python")
    
    # Programa con 3 botones
    var = messagebox.askyesnocancel(title="Advertencia!", message="Estas seguro que quieres salir?", icon='warning')
    print(var)
    
    
infoButton = Button(windows, text="Show Info", command=click)
infoButton.pack(pady=20)

warningButton = Button(windows, text="Show Warning", command=warning)
warningButton.pack(pady=20)

errorButton = Button(windows, text='Show Error', command=error)
errorButton.pack(pady=20)

askButton = Button(windows, text='Ask Question', command=ask)
askButton.pack(pady=20)

windows.mainloop()
