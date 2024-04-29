import tkinter as tk

def poner_foco():
    # Ponemos el foco en el boton 1
    boton1.focus_set()

def mostrar_foco(e):
    # Mostrar un mensaje que boton tiene el foco
    if ventana.focus_get() is boton2:
        print("El boton 2 tiene el foco")
    else :
        print(e.widget.cget('text'))

ventana = tk.Tk()
ventana.title("Ejemplo de Foco")
ventana.geometry("300x300")

boton1 = tk.Button(ventana, text="Boton 1")
boton1.bind("<FocusIn>", mostrar_foco)  # envia el evento a la funcion
boton1.bind("<FocusOut>", func=lambda e: print("Pierdo el foco"))
boton1.pack()

boton2 = tk.Button(ventana, text="Boton 2")
boton2.pack()

# Cuando transcurra x milisegundos llame a una funcion
ventana.after(2000, poner_foco)  # llama a la funcion sin evento
ventana.mainloop()