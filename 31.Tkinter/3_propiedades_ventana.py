import tkinter as tk

# crear una nueva ventana
ventana = tk.Tk()
ventana.title('Ejemplo de widgets')
ventana.geometry('400x400+800+100')

# Cambiar el logo de la ventana
try:
    ventana.tk.call('wm', 'iconphoto', ventana,
                    tk.PhotoImage(file='img/logo.png'))
except tk.TclError:
    print("No se pudo encontrar la imagen del logo")

# Tamaño minimo
ventana.minsize(width='200', height='300')

# tamaño maximo
ventana.maxsize(width='500', height='500')

# Cerrar la ventana
boton = tk.Button(ventana, text='cerrar', command=ventana.destroy)
boton.pack()

ventana.mainloop()


# https://www.bing.com/chat?form=NTPCHB
