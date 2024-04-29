import tkinter as tk
import random
import time

# Dimensiones de la cuadrícula
NUM_FILAS = 70
NUM_COLUMNAS = 70
ANCHO_CELDA = 8
ALTO_CELDA = 8

# Colores
COLOR_NORMAL = "white"
COLOR_RANDOM = lambda: "#{:06x}".format(0xFFFFF - int(n_global))


def celda_en_blanco(celda_seleccionada):
    #obtener el color del objeto
    color_actual = canvas.itemcget(celda_seleccionada, "fill")
    # Verificar si el color es blanco
    return color_actual == COLOR_NORMAL


def pintar_celda(fila, columna):
    
    celda_seleccionada = celdas[fila][columna]
    if celda_en_blanco(celda_seleccionada):
        global flag
        global n_global
        
        #setear el color del objeto 
        if n_global > 254:
            flag = False
        elif n_global < 1:
            flag = True
        if flag:
            n_global += 1
        else:
            n_global -= 1
            
        canvas.itemconfig(celda_seleccionada, fill=COLOR_RANDOM())


def drch(fila, columna):
    #cae abajo, izquierda si esta blanco
    if not celda_en_blanco(celdas[fila][columna]) and celda_en_blanco(celdas[fila + 1][columna - 1]):
        #mueve el renderizado del objeto
        canvas.move(celdas[fila][columna], -ALTO_CELDA, ALTO_CELDA)
        canvas.move(celdas[fila +1][columna - 1], ALTO_CELDA, -ALTO_CELDA)
        # Actualizar la matriz de celdas, swap
        celdas[fila][columna], celdas[fila + 1][columna - 1] = celdas[fila + 1][columna - 1], celdas[fila][columna]


def izq(fila, columna):
    #cae a abajo, derecha si esta blanco
    if not celda_en_blanco(celdas[fila][columna]) and celda_en_blanco(celdas[fila + 1][columna + 1]):
        #mueve el renderizado del objeto
        canvas.move(celdas[fila][columna], ALTO_CELDA, ALTO_CELDA)
        canvas.move(celdas[fila +1][columna + 1], -ALTO_CELDA, -ALTO_CELDA)
        # Actualizar la matriz de celdas, swap
        celdas[fila][columna], celdas[fila + 1][columna + 1] = celdas[fila + 1][columna + 1], celdas[fila][columna]


def caer(fila, columna):
    #mueve el renderizado del objeto
    canvas.move(celdas[fila][columna], 0, ALTO_CELDA)
    canvas.move(celdas[fila +1][columna], 0, -ALTO_CELDA)
    # Actualizar la matriz de celdas, swap 
    celdas[fila][columna], celdas[fila + 1][columna] = celdas[fila + 1][columna], celdas[fila][columna]


def volcar(fila, columna):
    #Incertidumbre derecha o izquierda
    if random.randint(0, 10) > 5.0:
        drch(fila, columna)
    else:
        izq(fila, columna)


def gravedad():
    #Recorrer la matriz de referencias de los objetos de abajo a arriba
    for fila in reversed(range(NUM_FILAS -1)):
        for columna in range(NUM_COLUMNAS -1):
            #caer si no esta blanco abajo
            if not celda_en_blanco(celdas[fila][columna]) and celda_en_blanco(celdas[fila + 1][columna]):
                caer(fila, columna)
            else:
                volcar(fila, columna)                                    


def paso_raton():
    #obtener coordenadas del raton
    x, y = coordenadas[0], coordenadas[1]
    #obtenemos cuadricula correspondiente
    fila_seleccionada = y // ALTO_CELDA
    columna_seleccionada = x // ANCHO_CELDA

    if columna_seleccionada < NUM_COLUMNAS and fila_seleccionada < NUM_FILAS:
        pintar_celda(fila_seleccionada, columna_seleccionada)
    gravedad()
    

#generamos los objetos rectangulo y lo resgistramos sus referencias en la matriz de listas celdas
def generar_rectangulos():
    global canvas
    global celdas

    for fila in range(NUM_FILAS):
        for columna in range(NUM_COLUMNAS):
            x1 = columna * ANCHO_CELDA
            y1 = fila * ALTO_CELDA
            x2 = x1 + ANCHO_CELDA
            y2 = y1 + ALTO_CELDA 
            rectangulo = canvas.create_rectangle(x1, y1, x2, y2, outline="white", fill=COLOR_NORMAL)
            #registramos el objeto en la matriz
            celdas[fila][columna] = rectangulo


#loop infinito para obtener x, y del raton y llamar a funcion paso_raton
def looop():
    global coordenadas 

    while True:
        ventana_ordenador = ventana.winfo_pointerxy()
        x_ventana_juego = ventana.winfo_rootx()
        y_ventana_juego = ventana.winfo_rooty()
        coordenadas[0] = ventana_ordenador[0] - x_ventana_juego
        coordenadas[1] = ventana_ordenador[1] - y_ventana_juego
        #evitar overIndex
        if (coordenadas[0] >= 0 or coordenadas[0] < NUM_FILAS) and (coordenadas[1] >= 0 or coordenadas[1] < NUM_COLUMNAS):
            paso_raton()

        ventana.update()        

#refencias globales
celdas = [[None] * NUM_COLUMNAS for _ in range(NUM_FILAS)]
coordenadas = [0, 0]
n_global = 0.0
flag = True

# Crear ventana
ventana = tk.Tk()
ventana.title("Jugando con arena")

# Crear Canvas imitando MACROS de C
canvas = tk.Canvas(ventana, width=NUM_COLUMNAS * ANCHO_CELDA, height=NUM_FILAS * ALTO_CELDA, bg="white")
canvas.pack()

#Generamos una matriz de objetos NONE que se asignaran despues las referencias de los objetos rectangulo

generar_rectangulos()
looop()

ventana.mainloop()
