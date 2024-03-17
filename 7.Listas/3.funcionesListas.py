no_olvidar = ['huevos', 'palta', 'lechuga', 'naranjas']

no_olvidar.append('leche')

print('hay', len(no_olvidar), 'cosas por comprar')

# verificar si existe un elemnto indicado dentro de la lista

print('existe vino en la lista', ('vino' in no_olvidar))
print('existe pan en la lista', ('pan' in no_olvidar))
print('existe huevos en la lista', ('huevos' in no_olvidar))

# verificar en que posicion se encuentra un elemento

print('si palta esta en que posicion se encuentra?', no_olvidar.index('palta'))
print('si leche esta en que posicion se encuentra?', no_olvidar.index('leche'))
# print('si pulpo esta en que posicion se encuentra?', no_olvidar.index('pulpo')) # error no esta dentro de la lista


# CONVERTIR UN STRING EN UNA LISTA

texto = "Pérez, García, Martínez, Borja"
print('Primero: ', texto[0])
print('No lista: ', texto)

nueva_lista = []
inicio = 0
for i in range(0, len(texto)):
    if texto[i] == ",":
        nueva_lista.append(texto[inicio:i])
        inicio = i + 1
nueva_lista.append(texto[inicio:])

print(nueva_lista)

# cada vez que veamos una coma (',') dividimos esa parte el string desde que se inicio hasta el final, en la separacion podria ir cualquier caracter
lista_alumnos = "Pérez, García, Martínez, Borja"
alumnos = lista_alumnos.split(',')

print(alumnos)

# Ordenar las listas  de manera alfabetica

print('lista original: ', no_olvidar)
# para utilizar el metodo sort se debe teneer un listado de un solo typo ya sea string o number
no_olvidar.sort()
print('lista ordenado: ', no_olvidar)

# sort ordena de mayor a menor

precios = [10, 5, 4, 2, 1]
precios.sort()
print(precios)

# ordenado de listas, de acuerdo al precio menor de cada elemento

comprar = [[1800, 'huevos'], [2300, 'palta'],
           [450, 'naranjas'], [610, 'queso']]

print('original:', comprar)
comprar.sort()
print('Ordenado: ', comprar)

print(comprar[0])


lista_compras = ["pan", "huevo", "queso", "arroz", "jamon"]
lista_compras.append("maní")
lista_compras.remove("arroz")
lista_compras.insert(2, "leche")
print(lista_compras)

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
