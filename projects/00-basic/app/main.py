from tkinter import *

def enviar():
  user = entrada.get()
  print('Hola ' + user + ' bienvenido')
  # Esto bloquea el input despues de haber enviardo el mensaje
  entrada.config(state=DISABLED)
  
def reset ():
  entrada.delete(0, END)
  
def borrar():
  entrada.delete( len(entrada.get()) - 1, END)


windows = Tk()

windows.geometry('500x500')
windows.title("rac-developer")
icono = PhotoImage(file='icon.png')
windows.iconphoto(True, icono)
windows.config(background='#f2f2f2')

entrada = Entry(windows, font=('Arial', 18), fg='red', bg='black',
                # Esto lo que hace es que cada vez que escribas cualquier caracter se va a ver el que pongas en show
                show='*')
entrada.insert(0, 'Escribe tu nombre')
entrada.pack(side=LEFT)

boton_enviar = Button(windows, text='Enviar', command=enviar)
boton_enviar.pack(side=RIGHT)

boton_resetear = Button(windows, text='Resetear', command=reset)
boton_resetear.pack(side=RIGHT)

boton_borrar = Button(windows, text='Borrar', command=borrar)
boton_borrar.pack(side=RIGHT)


windows.mainloop()
