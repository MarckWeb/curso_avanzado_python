#Ejercicios Listas

# • Crea una variable que contenga una lista con los
# siguientes elementos: "Cherry", "Berry", "Mango".

frutas = ["Cherry", "Berry", "Mango"]

# • Printa por pantalla la lista que has creado.

print(frutas)

# • Añade a la lista que has creado en el punto 1 de este
# ejercicio, el entero 99 al final de la misma.

frutas.append(99)

# • Printa por pantalla el segundo elemento de esta lista.
print(frutas)

# • Cambia el primer elemento de esta lista por otra lista
# vacía.

# frutas[0] = ["lista1", "lista2", "lista3"]
frutas.insert(0, [])
print(frutas)

# • Accede al primer elemento de esta lista (el cual es una lista) y añade dentro de esta lista el valor -100.
frutas[0].insert(0,-100) 
print(frutas)


# • Borra el último elemento de la lista.
del frutas[-1]
print(frutas)

# • Inserta en la posición cero de la lista el valor decimal
# 3.141516.

frutas[0].insert(0,3.141516) 
print(frutas)

# • Print a la lista dada la vuelta, desde atrás hacia adelante.
# print(frutas[::-1])
frutas.reverse()
print(frutas)
# • Borra el elemento "Berry" de la lista.


del frutas[1]
print(frutas)