import tkinter as tk

ventana = tk.Tk()
ventana.title('Ejemplos de grid')
ventana.geometry('300x400+800+100')

# Crear etiquetas
etiqueta1 = tk.Label(ventana, text='button_1',  borderwidth=2, relief="solid")
etiqueta2 = tk.Label(ventana, text='button_2', borderwidth=2, relief="solid")
etiqueta3 = tk.Label(ventana, text='button_3',  borderwidth=2, relief="solid")
etiqueta4 = tk.Label(ventana, text='button_4',  borderwidth=2, relief="solid")
etiqueta5 = tk.Label(ventana, text='button_5',  borderwidth=2, relief="solid")
etiqueta6 = tk.Label(ventana, text='button_6',  borderwidth=2, relief="solid")
etiqueta7 = tk.Label(ventana, text='button_7',  borderwidth=2, relief="solid")

# Usar grid para organizar las etiquetas
etiqueta1.grid(row=0, column=0)
etiqueta2.grid(row=0, column=1)
etiqueta3.grid(row=0, column=2)
etiqueta4.grid(row=1, column=0, columnspan=2, rowspan=3, sticky='nsew')
'''N o n: Norte (arriba)
S o s: Sur (abajo)
E o e: Este (derecha)
W o w: Oeste (izquierda)'''
etiqueta5.grid(row=1, column=2)
etiqueta6.grid(row=2, column=2)
etiqueta7.grid(row=3, column=0, columnspan=3, sticky='ew')

# Configurar el tamaño de la primera fila
# ventana.rowconfigure(0, weight=1)  # Peso 1 para la primera fila

ventana.mainloop()
