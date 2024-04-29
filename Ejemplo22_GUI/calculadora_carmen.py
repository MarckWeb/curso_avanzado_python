import tkinter as tk

def calcular():
    try:
        expresion = entrada.get()
        resultado = eval(expresion)
        resultado_var.set(resultado)
    except Exception as e:
        resultado_var.set("Error")

def agregar_igual():
    entrada.insert(tk.END, "=")
    calcular()

ventana = tk.Tk()
ventana.title("Calculadora")

resultado_var = tk.StringVar()
resultado_var.set("")

entrada = tk.Entry(ventana, textvariable=resultado_var, font=('Arial', 14))
entrada.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="ew")

estilo_botones = {'font': ('Arial', 12), 'width': 5, 'height': 2}

botones_numericos = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2),
    ('0', 4, 0), ('.', 4, 1)
]

for texto, fila, columna in botones_numericos:
    tk.Button(ventana, text=texto, bg="lightblue", **estilo_botones, command=lambda t=texto: entrada.insert(tk.END, t)).grid(row=fila, column=columna)

botones_operaciones = [
    ('/', 1, 3), ('*', 2, 3), ('-', 3, 3), ('+', 4, 3)
]

for texto, fila, columna in botones_operaciones:
    tk.Button(ventana, text=texto, bg="lightgreen", **estilo_botones, command=lambda t=texto: entrada.insert(tk.END, t)).grid(row=fila, column=columna)

tk.Button(ventana, text="C", bg="red", **estilo_botones, command=lambda: entrada.delete(0, tk.END)).grid(row=4, column=2)

tk.Button(ventana, text="=", bg="orange", **estilo_botones, command=calcular).grid(row=4, column=1)

ventana.mainloop()
