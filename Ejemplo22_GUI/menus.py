import tkinter as tk
from tkinter import filedialog as FileDialog
from tkinter import messagebox
import os
import platform
import subprocess

'''
Si se utiliza el método bind es necesario pasarle como argumento a 
  la función el evento.

En caso de que se utilice command no hace falta pasarle el evento
 como argumento a la función 
'''
def abrir_archivo():
    file = FileDialog.askopenfilename(title="Abrir fichero")
    '''file = FileDialog.askopenfilename(
        filetypes=(
            ("Ficheros ejecutables", "*.pyw"),
            ("Ficheros de texto", "*.txt"),
            ("Todos los ficheros","*.*")
        ),
        title="Busca ejecutable"
    )'''
    # Obtener la ruta del directorio actual
    ruta_actual = os.getcwd()

    # Nombre del archivo .pyw que quieres abrir
    #nombre_archivo = "prueba/ejemplos_messagebox.pyw"  # Reemplaza con el nombre de tu archivo.pyw
    nombre_archivo = file  # Reemplaza con el nombre de tu archivo.pyw
    # Comprobar el sistema operativo
    if platform.system() == "Windows":
        # Usar os.startfile para abrir el archivo en Windows
        os.startfile(os.path.join(ruta_actual, nombre_archivo))
    else:
        # Usar subprocess.run para abrir el archivo en sistemas UNIX (incluido macOS)
        try:
            # mac pythonw, en windows "open"
            subprocess.run(["pythonw", os.path.join(ruta_actual, nombre_archivo)], check=True)
        #except subprocess.CalledProcessError as e:
        except Exception as e:
            print(f"Error al abrir el archivo: {e}")


def opcion(event=None):
    print("Has pulsado opcion", event)

def abrir():
    #root = tk.Tk()
    #root.withdraw()  # Oculta la ventana principal de la aplicación

    fichero = FileDialog.askopenfilename(
        filetypes=(
            ("Archivos pdf", "*.pdf"), # mostrar pdf
            ("Todos los ficheros", "*.*")  # mostrar las carpetas
        ),
        title="Busca pdf"
    )
    print(fichero)

def salir():
    ventana.quit()

def copiar(e):
    print(e)
    print("Has seleccionado copiar")

ventana = tk.Tk()
ventana.title("Ejemplo menus")

# crear la barra de menu
barra_menu = tk.Menu(ventana)
ventana.config(menu=barra_menu)

# tearoff=0 quitar ---------
menu_file = tk.Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label="File",menu=menu_file)

menu_edit = tk.Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label="Edit",menu=menu_edit)

# Seleccionar un fichero.pyw y ejecutarlo
menu_file.add_command(label="Ejecutar Fichero", command=abrir_archivo)
# Seleccionar un fichero .pdf
menu_file.add_command(label="Open...", command=abrir)
menu_file.add_command(label="Close", command=opcion)

# crear opcion del menu con atajo de teclado
menu_edit.add_command(label="Copy", accelerator='Ctrl-C')
#ventana.bind_all("<Control-c>", lambda e: copiar())  # Control-c con c minuscula
ventana.bind_all("<Control-c>", copiar)  # Asi funciona siempre que copiar reciba el evento
menu_edit.add_command(label="Paste", command=opcion)

menu_file.add_separator()
menu_export = tk.Menu(menu_file)
menu_file.add_cascade(label="Export", menu=menu_export)
menu_export.add_command(label=".py")
menu_export.add_command(label=".pdf")

menu_file.add_command(label="Salir", command=salir)

ventana.mainloop()