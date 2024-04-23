import tkinter as tk
from tkinter import messagebox


def pulsar(event=None):
    print(event)
    messagebox.showinfo('Detalle', 'haz pulsado el boton')


# crear una nueva ventana
ventana = tk.Tk()
ventana.title('Ejemplo de widgets')

boton = tk.Button(ventana, text='pulssame', command='pulsar')
boton.place(x=20, y=50)

ventana.mainloop()
