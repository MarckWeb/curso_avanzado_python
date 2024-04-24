import tkinter as tk
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


def abrir_archivo(e):
    print('entra')
    # Obtener la ruta del directorio actual
    ruta_actual = os.getcwd()
    print(ruta_actual)

    # Nombre del archivo .pyw que quieres abrir
    # Reemplaza con el nombre de tu archivo.pyw
    nombre_archivo = "31.Tkinter/2_eventros.py"
    # Comprobar el sistema operativo
    if platform.system() == "Windows":
        print('que hace qui')
        # Usar os.startfile para abrir el archivo en Windows
        os.startfile(os.path.join(ruta_actual, nombre_archivo))
    else:
        # Usar subprocess.run para abrir el archivo en sistemas UNIX (incluido macOS)
        try:
            subprocess.run(["open", os.path.join(
                ruta_actual, nombre_archivo)], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error al abrir el archivo: {e}")


ventana = tk.Tk()
ventana.title("Ejemplo de los métodos messagebox")
ventana.geometry("300x300")
boton_info = tk.Button(ventana, text="showinfo",)
boton_info.pack()

boton_info.bind("<Button-1>", abrir_archivo)


ventana.mainloop()
