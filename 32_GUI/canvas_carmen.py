import tkinter as tk

ventana = tk.Tk()
ventana.title("ejemplo canvas")
ventana.geometry("500x400")

canvas = tk.Canvas(ventana, width=400, height=400, background= "lightblue")

#vemos una linea
canvas.create_line(10,10,300,10, arrow=tk.FIRST, width=5, fill="red")

#linea punteada
canvas.create_line(20,20,400,20, dash=(4, 2), dashoffset=20, width=5, fill="red")

#creamos un triangulo metiendole las coordenadas de los vertices
canvas.create_line(10,380,200,10,380,380,10,380, width=5, fill="blue")

# Ejemplo de otro tipo de objeto (rectángulo) con una línea punteada
canvas.create_rectangle(50, 100, 150, 200, dash=(4, 2), fill='green')

#circulo
canvas.create_oval(100, 100, 300, 300, width=2, outline='black', fill='orange')

# polígono 
canvas.create_polygon(250, 100, 387, 188, 325, 324, 175, 324, 113, 188, fill='red', outline='black', width=2)



canvas.pack()

ventana.mainloop() 