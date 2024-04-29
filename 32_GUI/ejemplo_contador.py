import tkinter as tk

def incrementar():
    '''global contador
    contador += 1
    valor_contador.set(contador)'''

    # Ahora cojo el valor introducido
    global dato
    print(dato.get())
    valor_contador.set(dato.get() + 1)


def decrementar():
    global contador
    contador -= 1
    valor_contador.set(contador)

ventana = tk.Tk()
ventana.title("Ejemplode contador")
ventana.geometry("200x100+500+200")

contador = 0
valor_contador = tk.StringVar(value=contador)   # BooleanVar, IntVar y DoubleVar
etiqueta = tk.Label(ventana, textvariable=valor_contador)
etiqueta.pack()

dato = tk.IntVar()
caja = tk.Entry(ventana, textvariable=dato)
caja.pack()

boton_incrementar = tk.Button(ventana, text="Incrementar", command=incrementar)
boton_incrementar.pack()
boton_decrementar = tk.Button(ventana, text="Decrementar", command=decrementar)
boton_decrementar.pack()

ventana.mainloop()