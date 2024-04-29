import tkinter as tk

def cerrar_ventana():
    # cerrar la ventana
    ventana.destroy()

ventana = tk.Tk()
ventana.title("Ejemplo propiedades de la ventana")
ventana.geometry('400x600+500+200')  # anchoxalto+desp_x+desp_y

# cambiar el logo de la ventana
ventana.tk.call('wm','iconphoto',ventana, tk.PhotoImage(file='img/logo.png'))

# tamaño minimo
ventana.minsize(width="200", height="300")

# tamaño maximo
ventana.maxsize(width="800", height="700")

# tamaño fijo:  resizable
ventana.resizable(width=False, height=False)

#boton = tk.Button(ventana, text='cerrar', command=cerrar_ventana)
#boton = tk.Button(ventana, text='cerrar', command=ventana.destroy)
boton = tk.Button(ventana, text='cerrar')
boton.bind("<Button-1>",lambda e: ventana.destroy())
boton.pack()

ventana.mainloop()