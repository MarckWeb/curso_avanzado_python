import tkinter as tk

ventana = tk.Tk()
ventana.title("Ejemplo de Canvas")
ventana.geometry("500x400")

canvas = tk.Canvas(ventana, width=400, height=400, background="pink")
# mostrar linea
# dash=(1, 5)
# dash=(6,2,9,18)
# dashoffset=20   en que posicion empieza a aplicar el patron
#canvas.create_line(10,10,300,10, dash=(6,2,9,18),dashoff=10, dashoffset=20, arrow=tk.FIRST, width=5, fill="blue")
# crear un triangulo
#canvas.create_line(10,380,200,10,380,380,10,380, width=5, fill="blue")
#canvas.create_line(10, 10, 400, 10, arrow=tk.LAST, width=5, fill="blue",  dash=(5, 10, 2, 10), dashoff = 150, dashoffset = 3)
#canvas.create_line(10, 50, 400, 50, arrow=tk.LAST, width=5, fill="blue",  dash=(5, 10, 2, 10), dashoff = 150)

# crear rectangulo
#canvas.create_rectangle(50,50,200,300, outline="yellow", width=5,  fill="green")

# crear ovalos
#canvas.create_oval(50,50,200,300)
#canvas.create_oval(300,50,400,150, dash=(8,10), outline="red", width=5)

# colocar texto en el canvas
# lo centra porque 200 es justo la mitad del canvas
#canvas.create_text(10,10, text="Ejemplo", font=("Arial","20","bold"), anchor=tk.NW, width=180, justify=tk.CENTER, fill="blue")

# crear imagenes
logo = tk.PhotoImage(file="img/logo.png")
#canvas.create_image(150,180, image=logo)

# crear arcos
#extent=359 son los grados a dibujar, por defecto esta a 90
canvas.create_arc(10,10,300,100, style="arc", extent=-90)
canvas.create_arc(10,120,300,180, style="chord")
canvas.create_arc(10,300,300,250, style="pieslice")

# crear poligono
points = [150, 100, 200, 120, 240, 180,
          210, 200, 150, 150, 100, 200]
gamba = canvas.create_polygon(points, outline="blue",
                           fill="orange", width=2)


canvas.pack()

ventana.mainloop()