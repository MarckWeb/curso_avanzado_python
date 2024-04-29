import tkinter
from tkmacosx import Button
from tkinter import font

def hello(e):
    print("Single Click, Button-l")
    #boton.config(background="orange")
    e.widget.config(background="orange")

def quit(event):
    print("Double Click, so let's stop")
    import sys; sys.exit()

root = tkinter.Tk()
default_font = font.nametofont("TkDefaultFont")  # Obtener la fuente predeterminada en un objeto Font
print(f"La fuente predeterminada en Tkinter es: {default_font.actual()}")  # Mostrar detalles de la fuente
boton = Button(None, text='Mouse Clicks', bg="red")
boton.bind("<Enter>", func=lambda e: boton.config( background="yellow"))
boton.bind("<Leave>", func=lambda e: boton.config( background="green"))
#boton.bind("<Button-1>", func=lambda e: boton.config( background="orange"))

etiqueta = tkinter.Label(None, text="fuente Arial con tamaño 16", font=("Arial", "16", "underline"))
etiqueta.bind("<Button-1>", hello)  # presionar sobre la etiqueta
etiqueta.pack()


boton.pack()
boton.bind('<Button-1>', hello)
boton.bind('<Double-1>', quit)

root.mainloop()