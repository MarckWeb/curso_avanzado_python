import tkinter as tk
from tkinter import messagebox

def pulsar(event=None):
    #print(event)
    #messagebox.showinfo("Detalle", "Has pulsado el boton")
    respuesta = messagebox.askquestion("Cerramos la ventana?")
    if respuesta == 'yes':
        print("Has elegido yes")
    else:
        print("Has elegido no")


ventana = tk.Tk()
ventana.title('Ejemplo de eventos')

boton = tk.Button(ventana, text='Pulsame', command=pulsar)
boton.place(x=10,y=20)

ventana.mainloop()