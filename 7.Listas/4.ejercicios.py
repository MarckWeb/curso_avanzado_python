# Pregunta 1
# Escriba una función de nombre promedio_std(). La función debe recibir una lista de números llamada lista, y debe retornar retornar el promedio de ellos, junto con su desviación estándar.

# Hint 1: La desviación estándar corresponde a la raíz de la suma de los cuadrados de las diferencias de cada elemento respecto al promedio, divididos por la cantidad de elementos.

# Hint 2: Recuerda que puedes retonar dos valores x e y utilizando la notación

import math


def promedio_std(lista):
    # Calcula el promedio de la lista
    promedio = sum(lista) / len(lista)

    # Calcula la suma de los cuadrados de las diferencias entre cada elemento y el promedio
    suma_cuadrados_diferencias = sum((x - promedio) ** 2 for x in lista)

    # Calcula la desviación estándar
    desviacion_estandar = math.sqrt(suma_cuadrados_diferencias / len(lista))

    return promedio, desviacion_estandar


# Ejemplo de uso
numeros = [1, 2, 3, 4, 5]
promedio, std_dev = promedio_std(numeros)
print("Promedio:", promedio)
print("Desviación estándar:", std_dev)

# Suponga que tiene una lista de colores repetidos y desordenados, estos pueden ser: azul, rojo, verde y amarillo. Desea saber cual de esos colores es el que más se repite. Escriba una función color_frecuente que reciba como argumento a una lista de strings llamada lista y retorne el string más repetido y el número de ocurrencias del mismo.

# Por ejemplo para la lista ['azul', 'rojo', 'verde', 'verde', 'verde', 'rojo', 'verde', 'verde', 'azul', 'amarillo', 'azul', 'azul', 'verde', 'verde', 'verde', 'amarillo', 'amarillo']

# Debe retornar: "verde", 8

# En caso de que haya varios colores con el máximo número, se retornará con la siguiente prioridad: azul, rojo, verde, amarillo. Es decir, por ejemplo si la lista es l = ['rojo', 'rojo', 'azul', azul'], la función debe retornar "azul", 2


def color_frecuente(lista):
    # Inicializamos listas para contar la frecuencia de cada color
    colores = ['azul', 'rojo', 'verde', 'amarillo']
    frecuencias = [0] * len(colores)

    # Contamos la frecuencia de cada color
    for color in lista:
        if color in colores:
            index = colores.index(color)
            frecuencias[index] += 1

    # Encontramos el color más frecuente
    max_frecuencia = max(frecuencias)
    color_mas_frecuente = colores[frecuencias.index(max_frecuencia)]

    # Retornamos el color más frecuente y su frecuencia
    return color_mas_frecuente, max_frecuencia


# Ejemplo de uso
lista = ['azul', 'rojo', 'verde', 'verde', 'verde', 'rojo', 'verde', 'verde', 'azul',
         'amarillo', 'azul', 'azul', 'verde', 'verde', 'verde', 'amarillo', 'amarillo']
resultado = color_frecuente(lista)
print("Color más frecuente:", resultado[0])
print("Número de ocurrencias:", resultado[1])

# Un uso muy común de las listas es el de representar tableros con ellas. Para eso se utilizan listas de listas, de este modo, se puede entender una lista de listas como una matriz. Así, para acceder a un elemento i,j de la matriz, se debe acceder a: matriz[i][j].

# Para ese ejercicio se dispone de un tablero de buscaminas especial, donde lo único que hay es bombas en las distintas posiciones. Este tablero es de la forma:

# caudrado de minas bidujo

# Donde las X representan las bombas. Ese tablero, en representación matricial de Python, donde se utilizan strings con un espacio: " " y "X" para representar espacios libres y bombas respectivamente, viene dado por:

# 1
# tablero = [[' ', 'X', ' ', 'X'],['X', ' ', ' ', ' '],[' ', 'X', 'X', ' '],['X', ' ', ' ', 'X']]
# El objetivo de este ejercicio, es que programes una función buscaminas que reciba como argumento a una matriz tablero y dos coordenadas i, j, y que entregue la cantidad de bombas que rodean a esa posición.

# Por ejemplo, si la el tablero dado es el representado en la tabla, y la posición viene dada por i=0 y j=0, tu función debe retornar el valor 2, ya que hay dos bombas rodeándola, en (0,1) y (1,0).

# Por otro lado, si el tablero es el mismo, y las coordenadas son i=1, j=1, tu función debe retornar 4, pues hay bombas rodeando la posición en (1,0), en (0,1), en (2,1) y en (2,2).

# Hint: recuerda que el tablero puede ser de un tamaño arbitrario y que al escribir posiciones más grandes que ese tamaño o menores que 0, tu programa arrojará error.


def buscaminas(tablero, i, j):
    # Definimos las direcciones adyacentes (arriba, abajo, izquierda, derecha y diagonales)
    direcciones = [(1, 0), (-1, 0), (0, 1), (0, -1),
                   (1, 1), (-1, 1), (1, -1), (-1, -1)]

    # Inicializamos el contador de bombas adyacentes
    bombas_adyacentes = 0

    # Recorremos todas las direcciones adyacentes
    for dx, dy in direcciones:
        # Calculamos las coordenadas de la celda adyacente
        x, y = i + dx, j + dy

        # Verificamos si las coordenadas están dentro del tablero
        if 0 <= x < len(tablero) and 0 <= y < len(tablero[0]):
            # Verificamos si la celda adyacente contiene una bomba
            if tablero[x][y] == 'X':
                bombas_adyacentes += 1

    return bombas_adyacentes


# Ejemplo de uso
tablero = [[' ', 'X', ' ', 'X'],
           ['X', ' ', ' ', ' '],
           [' ', 'X', 'X', ' '],
           ['X', ' ', ' ', 'X']]

print(buscaminas(tablero, 0, 0))  # Output: 2
print(buscaminas(tablero, 1, 1))  # Output: 4
# Pregunta 4
# ¿Cuál es el valor de la variable trozo después de ejecutar el siguiente código?


datos = [2, "Julio", 2017, "Final", 14.5, "Chile", 0, "Alemania", 1]
trozo = datos[2:6]
print(trozo)

# Pregunta 5
# ¿Cuál es el valor de la variable trozo después de ejecutar el siguiente código?
datos = ["semillas", 500, "cerveza", 2, "despacho",
         4100, "pago", "bitcoin", "confianza", 95.4]
trozo = datos[1:9:2]
print(trozo)


# En el siguiente código:
unidades = [40, 32, 49, 2, 20, 8, 55, 300, 10]
muestra = []
# De las siguientes expresiones, marque aquellas que permiten que el valor de la variable muestra sea [49, 2, 55, 300]

print(unidades[2:3] + unidades[3:7:3] + unidades[7:8])
print(unidades[2:4] + unidades[6:8])


# Pregunta 7
# Considere la lista votos, que contiene listas con los resultados de una votación
def ganador(votos):
    mayor = votos[0]
    for cand in votos:
        if cand[1] > mayor[1]:
            mayor = cand
    return mayor


resultados = [["Alfredo", 20], ["Marcela", 40],
              ["Ignacio", 30], ["Loreto", 10]]
mayoria = ganador(resultados)

print('mayoria', mayoria)

# Pregunta 10
# ¿Cuál es el valor de la variable splitted luego de ejecutar el siguiente código?

contactos = "Marcelo, Alvaro; Elena, Karen; Jaime; Carmen"
splitted = contactos.split(";")
print(splitted)


# Pregunta 9
# De las siguientes funciones, indique cuál o cuáles permiten obtener la cantidad de veces que un elemento elem se encuentra dentro de la lista conjunto.


def cuantas(elem, conjunto):
    for e in conjunto:
        if e == elem:
            return e


print(cuantas(1, [1, 2, 1, 3, 1]))

# Pregunta 8
# Considera un tablero de 3x3 posiciones, donde cada una de ella está numerada desde el número 1 al 9. El tablero está definido de la siguiente manera:

tablero = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for i in range(9):
    print(tablero[i % 3][i//3], end=" ")

print()
for i in range(3):
    for j in range(3):
        print(tablero[j][i], end=" ")

print()
for j in range(3):
    for i in range(3):
        print(tablero[i][j], end=" ")
