import tkinter as tk

ventana = tk.Tk()
ventana.title("Ejemplo de grid")
ventana.geometry("300x400")

etiqueta1 = tk.Label(ventana, text="label 1")
etiqueta2 = tk.Label(ventana, text="label 2")
etiqueta3 = tk.Label(ventana, text="label 3")
etiqueta4 = tk.Label(ventana, text="label 4")
etiqueta6 = tk.Label(ventana, text="label 6")
etiqueta7 = tk.Label(ventana, text="label 7")
etiqueta1.grid(row=0, column=0)
etiqueta2.grid(row=0, column=1, rowspan=2)
etiqueta3.grid(row=0, column=2)
etiqueta4.grid(row=1, column=0)
etiqueta6.grid(row=1, column=2)
etiqueta7.grid(row=2, column=0, columnspan=3)

ventana.mainloop()