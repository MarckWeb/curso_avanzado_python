import tkinter as tk


def incrementar():

    # valor_contador.set(contador)

    # Ahora cojo el valor introducido
    global dato
    print(dato.get())
    global contador
    contador += dato.get() + 1
    valor_contador.set(contador)


def decrementar():
    global contador
    contador -= 1
    valor_contador.set(contador)


ventana = tk.Tk()
ventana.title('Ejemplos de diferentes cursores')
ventana.geometry('300x400+800+100')

contador = 0
# BooleanVar, IntVar, DoubleVar
valor_contador = tk.StringVar(value=contador)
etiqueta = tk.Label(ventana, textvariable=valor_contador)
etiqueta.pack()

dato = tk.IntVar()
caja = tk.Entry(ventana, textvariable=dato)
caja.pack()


boton_incrementar = tk.Button(ventana, text='Incrementar', command=incrementar)
boton_incrementar.pack()

boton_decrementar = tk.Button(ventana, text='Decrementar', command=decrementar)
boton_decrementar.pack()


ventana.mainloop()
