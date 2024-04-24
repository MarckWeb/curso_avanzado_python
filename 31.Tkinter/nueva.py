import tkinter as tk
from tkinter import filedialog as FileDialog
import os
import platform


def opcion():
    print('algo')


def abrir():
    # Filtrar solo archivos con extensión .pdf
    fichero = FileDialog.askopenfilename(title='Abrir archivo', filetypes=[
                                         ("Archivos PDF", "*.pdf")])
    print(fichero)
    ruta_fichero = os.getcwd()
    if platform.system() == "Windows":
        # Usar os.startfile para abrir el archivo en Windows
        os.startfile(os.path.join(ruta_fichero, fichero))


def cerrar():
    ventana.destroy()


# Crear una nueva ventana
ventana = tk.Tk()
ventana.title('Ejemplo de menús en la ventana')

# Creamos la barra de menú
barra_menu = tk.Menu(ventana)
ventana.config(menu=barra_menu)

menu_file = tk.Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label='File', menu=menu_file)

menu_edit = tk.Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label='Edit', menu=menu_edit)

# Opciones de menú
menu_file.add_command(label='Ejecutar archivo', command=opcion)
menu_file.add_command(label='Abrir', command=abrir, accelerator='Ctrl+O')
menu_file.add_command(label='Cerrar', command=cerrar, accelerator='Ctrl+W')

menu_edit.add_command(label='Copiar', command=opcion, accelerator='Ctrl+C')
menu_edit.add_command(label='Pegar', command=opcion)

menu_export = tk.Menu(menu_file, tearoff=0)
menu_file.add_cascade(label='Exportar', menu=menu_export)
menu_export.add_command(label='.py')
menu_export.add_command(label='.pdf')

# Asociar atajos de teclado
ventana.bind('<Control-o>', lambda e: abrir())
ventana.bind('<Control-w>', lambda e: cerrar())
ventana.bind('<Control-c>', lambda e: opcion())

ventana.mainloop()
