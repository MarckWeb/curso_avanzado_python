import tkinter as tk

def operar(e):
    # La etiqueta del boton pulsado
    op = e.widget.cget('text')
    global resultado
    match op:
        case '+':
            resultado.set(num1.get() + num2.get())
        case '-':
            resultado.set(num1.get() - num2.get())
        case 'x':
            resultado.set(num1.get() * num2.get())
        case '/':
            resultado.set(num1.get() / num2.get())


ventana = tk.Tk()
ventana.title("Mi calculadora")
ventana.geometry("300x300")

num1 = tk.DoubleVar()   # IntVar()
label1 = tk.Label(ventana,text="Introduce numero:")
caja1 = tk.Entry(ventana, textvariable=num1)
label1.pack()
caja1.pack()

num2 = tk.DoubleVar()
label2 = tk.Label(ventana, text="Introduce numero:")
caja2 = tk.Entry(ventana, textvariable=num2)
label2.pack()
caja2.pack()

boton_suma = tk.Button(ventana, text="+")
boton_suma.bind("<Button-1>", operar)
boton_suma.pack()

boton_resta = tk.Button(ventana, text="-")
boton_resta.bind("<Button-1>", operar)
boton_resta.pack()

boton_multiplicacion = tk.Button(ventana, text="x")
boton_multiplicacion.bind("<Button-1>", operar)
boton_multiplicacion.pack()

boton_division = tk.Button(ventana, text="/")
boton_division.bind("<Button-1>", operar)
boton_division.pack()

resultado = tk.DoubleVar()
label_resultado = tk.Label(ventana, textvariable=resultado )
label_resultado.pack()

ventana.mainloop()