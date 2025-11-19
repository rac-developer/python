import os
from tkinter import *
from tkinter import filedialog, messagebox, colorchooser, font
from tkinter.messagebox import *
from tkinter.filedialog import *

# ----- Funciones -----

def change_color():
    color = colorchooser.askcolor(title="Selecciona un color")
    text_area.config(fg=color[1])

# args podemos pasarle varias variables si queremos

def change_font(*args):
    font_selected = (font_name.get(), font_size.get())
    text_area.config(font=font_selected)

def new_file():
    windows.title("Untitled")
    text_area.delete(1.0, END)

def open_file():
    file = askopenfilename(defaultextension=".txt", 
                           file=[("All Files", "*.*"), ("Text Documents", "*.txt")]
                           )
    try:
        windows.title(os.path.basename(file) + " - Notepad")
        text_area.delete(1.0, END)
        file = open(file, "r")
        text_area.insert(1.0, file.read())
    except Exception:
        print("No se pudo abrir el archivo")
    finally:
        file.close()

def save_file():
    file = filedialog.asksaveasfilename(initialfile='Untitled.txt', 
                                        defaultextension=".txt", 
                                        file=[("All Files", "*.*"), ("Text Documents", "*.txt")]
                                        )
    if file is None:
        return
    else:
        try:
            windows.title(os.path.basename(file) + " - Notepad")
            file = open(file, "w")
            file.write(text_area.get(1.0, END))
        except Exception:
            print("No se pudo guardar el archivo")
        finally:
            file.close()

def cut():
    text_area.event_generate("<<Cut>>")

def copy():
    text_area.event_generate("<<Copy>>")

def paste():
    text_area.event_generate("<<Paste>>")
     
def about():
    showinfo("About Notepad", 
    """Bloc de notas es un editor de texto incluido en los sistemas operativos. Su funcionalida es muy simple. Algunas caracteristicas propias son:
    - Insercion de hora y fecha actual pulsando F5, en formto "hh:mm dd/mm/aaaa".
    - Insercion de hora y fecha actual si el documento comienza por ".LOG".
    - Ajuste de lineas.
    - Posibilidad de exportar a cualquier formato de texto plano.
""")

def quit():
    windows.destroy()

# ----- Programa ----- 

windows = Tk()

icono = PhotoImage(file='icon.png')
windows.iconphoto(True, icono)

# Para centrar el programa al abrirse en la pantalla
window_width = 500
window_height = 500
screen_width = windows.winfo_screenwidth()
screen_height = windows.winfo_screenheight()
x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))
windows.geometry('{}x{}+{}+{}'.format(window_width, window_height, x, y))

windows.title("rac-developer - Notepad")
file = None

font_name = StringVar(windows)
font_name.set("Arial")
font_size = StringVar(windows)
font_size.set("25")

text_area = Text(windows, font=(font_name.get(), font_size.get()), bg="#f2f2f2")
text_area.grid(sticky=N + E + S + W)

scroll_bar = Scrollbar(text_area)
scroll_bar.pack(side=RIGHT, fill=Y)

text_area.config(yscrollcommand=scroll_bar.set)

# Barra de menú inferior
frame = Frame(windows)
frame.grid()

color_button = Button(frame, text="Color", command=change_color)
color_button.grid(row=0, column=0)

font_box = OptionMenu(frame, font_name, *font.families(), command=change_font)
font_box.grid(row=0, column=1)

size_box = Spinbox(frame,from_=1, to=100, textvariable=font_size, command=change_font)
size_box.grid(row=0, column=2)

# Barra de menú superior
menu_bar = Menu(windows, bg="#f1f1f1")
windows.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=quit)

edit_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=cut)
edit_menu.add_command(label="Copy", command=copy)
edit_menu.add_command(label="Paste", command=paste)

help_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About", command=about)

# Este grid es para que el text_area se expanda correctamente
windows.grid_rowconfigure(0, weight=1)
windows.grid_columnconfigure(0, weight=1)

windows.mainloop()

