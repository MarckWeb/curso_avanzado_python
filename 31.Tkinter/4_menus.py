import tkinter as tk
from tkinter import filedialog as FileDialog
import os
import platform
import subprocess


def opcion():
    print('algo')


def abrir():
    fichero = FileDialog.askopenfilename(title='abrir fichero')
    print(fichero)
    ruta_fichero = os.getcwd()
    if platform.system() == "Windows":
        print('estoy dentro del if')
        # Usar os.startfile para abrir el archivo en Windows
        os.startfile(os.path.join(ruta_fichero, fichero))


def salir():
    ventana.quit()


def copiar(e):
    print('seleccionado copiado')


# crear una nueva ventana
ventana = tk.Tk()
ventana.title('Ejemplo menus de la ventana')

# Creamos la barra de menu
barra_menu = tk.Menu(ventana)
ventana.config(menu=barra_menu)

menu_file = tk.Menu(barra_menu, tearoff=0)  # tearoff quita lineas ----
barra_menu.add_cascade(label='File', menu=menu_file)


menu_edit = tk.Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label='Edit', menu=menu_edit)

# OPCIONES DE MENU
menu_file.add_command(label='ejecutar fichero', command=opcion)
menu_file.add_command(label='Open', command=abrir)
menu_file.add_command(label='Close', command=salir)
# menu_file.add_separator() # separa en linea
# menu_file.add_command(label="Salir", command=ventana.quit)

menu_edit.add_command(label='Copy', accelerator=('Ctrol+c'), command=copiar)
# ventana.bind('<Control-c>', lambda e: copiar()) #1ra forma
ventana.bind('<Control-c>', copiar)  # 2da forma
menu_edit.add_command(label='Paste', command=opcion)

menu_export = tk.Menu(menu_file, tearoff=0)
menu_file.add_cascade(label='Export', menu=menu_export)
menu_export.add_command(label='.py')
menu_export.add_command(label='.pdf')

ventana.mainloop()
