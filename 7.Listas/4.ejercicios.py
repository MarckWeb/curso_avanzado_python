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
