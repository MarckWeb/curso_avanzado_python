import tkinter as tk


def button_click(value):
    if value == '=':
        evaluate_expression()
    elif value == 'C':
        display_entry.delete(0, tk.END)
    else:
        display_entry.insert(tk.END, value)


def evaluate_expression():
    expression = display_entry.get()
    try:
        result = eval(expression)
        display_entry.delete(0, tk.END)
        display_entry.insert(tk.END, str(result))
    except Exception as e:
        display_entry.delete(0, tk.END)
        display_entry.insert(tk.END, "Error")


open_window = tk.Tk()
open_window.title('Calculator')
open_window.config(bg='#222')

# Dimensiones de la ventana de la calculadora
window_width = 600
window_height = 600

# Dimensiones de la pantalla
screen_width = open_window.winfo_screenwidth()
screen_height = open_window.winfo_screenheight()

# Coordenadas para centrar la ventana
x_coordinate = int((screen_width / 2) - (window_width / 2))
y_coordinate = int((screen_height / 2) - (window_height / 2))

# Configuración de la geometría de la ventana y límites de tamaño
open_window.geometry(f'{window_width}x{window_height}+{x_coordinate}+{y_coordinate}')
open_window.minsize(360, 360)
open_window.maxsize(720, 720)

# Crear el marco base
base_frame = tk.LabelFrame(open_window, background='darkgray', borderwidth=3, text='Calculadora')
base_frame.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.9)

# Crear el marco de visualización
display_frame = tk.LabelFrame(base_frame, background='lightgray', borderwidth=0, text='Display')
display_frame.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.2)

# Crear la entrada de texto para el display
display_entry = tk.Entry(display_frame, font=('Verdana', 22), justify='right')
display_entry.pack(fill='both', expand=True)

# Crear el marco del teclado
keyboard_frame = tk.LabelFrame(base_frame, bg='black', borderwidth=0, text='Keyboard', fg='gray')
keyboard_frame.place(relx=0.05, rely=0.3, relwidth=0.9, relheight=0.65)

# Lista de botones para la calculadora
buttons = [
    '7', '8', '9', '+',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '/',
    '.', '%'
]

# Configurar botones en el marco de teclado utilizando grid
for i, button_text in enumerate(buttons):
    row = i // 4
    col = i % 4
    # Ajustar el rowspan para el botón de igual y el rowspan y sticky para el botón de módulo
    if button_text == '=':
        button = tk.Button(keyboard_frame, font=('Verdana', 20), text=button_text,
                           command=lambda value=button_text: button_click(value))
        button.grid(row=row, column=col, rowspan=2, padx=5, pady=5, sticky='nsew')
        button.config(fg='white', bg='green')
    elif button_text == '%':
        button = tk.Button(keyboard_frame, font=('Verdana', 20), text=button_text,
                           command=lambda value=button_text: button_click(value))
        button.grid(row=row, column=3, padx=5, pady=5, sticky='nsew')
    elif button_text == 'C':
        button = tk.Button(keyboard_frame, font=('Verdana', 20), text=button_text,
                           command=lambda value=button_text: button_click(value))
        button.grid(row=row, column=0, rowspan=2, padx=5, pady=5, sticky='nsew')
        button.config(bg='red', fg='white')
    elif button_text == '.':
        button = tk.Button(keyboard_frame, font=('Verdana', 20), text=button_text,
                           command=lambda value=button_text: button_click(value))
        button.grid(row=row, column=1, padx=5, pady=5, sticky='nsew')
    else:
        button = tk.Button(keyboard_frame, font=('Verdana', 20), text=button_text,
                           command=lambda value=button_text: button_click(value))
        button.grid(row=row, column=col, padx=5, pady=5, sticky='nsew')  # Alineación vertical y horizontal centrada

    if button_text in ['/', '*', '-', '+', '%']:
        button.config(bg='orange')

# Configurar el tamaño de las celdas en el marco del teclado
for i in range(4):
    keyboard_frame.grid_rowconfigure(i, weight=1)  # Columnas expandibles
for j in range(4):
    keyboard_frame.grid_columnconfigure(j, weight=1)  # Filas expandibles

open_window.mainloop()
print(tk.TkVersion)
