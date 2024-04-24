import tkinter as tk
from tkinter import ttk


def button_click(number):
    current = pantalla.get()
    pantalla.delete(0, tk.END)
    pantalla.insert(0, str(current) + str(number))


def button_clear():
    pantalla.delete(0, tk.END)


def button_equal():
    second_number = pantalla.get()
    pantalla.delete(0, tk.END)

    if math_operation == 'suma':
        pantalla.insert(0, f_num + float(second_number))
    if math_operation == 'resta':
        pantalla.insert(0, f_num - float(second_number))
    if math_operation == 'multiplicar':
        pantalla.insert(0, f_num * float(second_number))
    if math_operation == 'dividir':
        try:
            pantalla.insert(0, f_num / float(second_number))
        except ZeroDivisionError:
            pantalla.insert(0, "Error")


def button_add():
    first_number = pantalla.get()
    global f_num
    global math_operation
    math_operation = 'suma'
    f_num = float(first_number)
    pantalla.delete(0, tk.END)


def button_subtract():
    first_number = pantalla.get()
    global f_num
    global math_operation
    math_operation = 'resta'
    f_num = float(first_number)
    pantalla.delete(0, tk.END)


def button_multiply():
    first_number = pantalla.get()
    global f_num
    global math_operation
    math_operation = 'multiplicar'
    f_num = float(first_number)
    pantalla.delete(0, tk.END)


def button_divide():
    first_number = pantalla.get()
    global f_num
    global math_operation
    math_operation = 'dividir'
    f_num = float(first_number)
    pantalla.delete(0, tk.END)


# Configuración de la ventana
ventana = tk.Tk()
ventana.title('Calculadora')
ventana.geometry('650x300')
ventana.configure(bg='#f5f5f5')

# Estilos para botones
style = ttk.Style()
style.configure('TButton', font=('Victo Mono', 10),
                padding=10, background='red')

# Pantalla
pantalla = tk.Entry(ventana, width=15, borderwidth=5,
                    font=('Victo Mono', 20), justify='right')
pantalla.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Botones numéricos
boton_1 = ttk.Button(ventana, text='1', command=lambda: button_click(1))
boton_2 = ttk.Button(ventana, text='2', command=lambda: button_click(2))
boton_3 = ttk.Button(ventana, text='3', command=lambda: button_click(3))
boton_4 = ttk.Button(ventana, text='4', command=lambda: button_click(4))
boton_5 = ttk.Button(ventana, text='5', command=lambda: button_click(5))
boton_6 = ttk.Button(ventana, text='6', command=lambda: button_click(6))
boton_7 = ttk.Button(ventana, text='7', command=lambda: button_click(7))
boton_8 = ttk.Button(ventana, text='8', command=lambda: button_click(8))
boton_9 = ttk.Button(ventana, text='9', command=lambda: button_click(9))
boton_0 = ttk.Button(ventana, text='0', command=lambda: button_click(0))

# Botones de operaciones
boton_suma = ttk.Button(ventana, text='+', command=button_add)
boton_resta = ttk.Button(ventana, text='-', command=button_subtract)
boton_multiplicar = ttk.Button(ventana, text='*', command=button_multiply)
boton_dividir = ttk.Button(ventana, text='/', command=button_divide)

boton_igual = ttk.Button(ventana, text='=', command=button_equal)
boton_limpiar = ttk.Button(ventana, text='C', command=button_clear)

# Colocar botones en la ventana
boton_1.grid(row=1, column=0, padx=2, pady=2)
boton_2.grid(row=1, column=1, padx=2, pady=2)
boton_3.grid(row=1, column=2, padx=2, pady=2)
boton_suma.grid(row=1, column=3, padx=2, pady=2)

boton_4.grid(row=2, column=0, padx=5, pady=5)
boton_5.grid(row=2, column=1, padx=5, pady=5)
boton_6.grid(row=2, column=2, padx=5, pady=5)
boton_resta.grid(row=2, column=3, padx=5, pady=5)

boton_7.grid(row=3, column=0, padx=5, pady=5)
boton_8.grid(row=3, column=1, padx=5, pady=5)
boton_9.grid(row=3, column=2, padx=5, pady=5)
boton_multiplicar.grid(row=3, column=3, padx=5, pady=5)

boton_0.grid(row=4, column=0, padx=5, pady=5)
boton_limpiar.grid(row=4, column=1, padx=5, pady=5)
boton_igual.grid(row=4, column=2, padx=5, pady=5)
boton_dividir.grid(row=4, column=3, padx=5, pady=5)

ventana.mainloop()
