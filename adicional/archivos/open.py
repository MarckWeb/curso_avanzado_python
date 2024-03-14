# open -. metodo que nos sirve para imprimirarchivo o leerlos

open = ("archivo.txt", "r")  # leer
open = ("archivo.txt", "w")  # escribir


# para leer el archivo se debe llamar al ,etodo  "read" sobre la varibale que guarda al objeto "open".

lectura = open("arch.txt", "r")
leer = lectura.read()

# si el archivo tiene un texto Hollaaaa, el valor imprimido sera

print(leer)  # Hollaaaa


# Lectura readline()

# enves de leer todo el archivo con .read(), se puede leer una linea con .readline()

# cada vex que se llama a la funcion, se lee la siguiente linea,linea por linea, es decir que si la funcion fue llamada por cuarta vez, el print mostrara la cuarta linea.

leer = lectura.readline()
print(leer)  # primera linea

leer2 = lectura.readline()
print(leer2)  # segunda linea

"""*******************************************"""
# Par escribir en un archivo, se tiene que haber abieto en modo "w" write

# si el archivo existe, se borrara para crear uno nuevo, tener cuidado!!!

# para escribri algo se ocupa el metodo write(), pasadno como para,etro el string que se quiere escribir

escritura = open("arch.txt", "w")
escritura.write("esto se escribe en el archivo")

# para escribir mas lineas, se deben indicar los "saltos de linea mediante el simbolo \n new line"

escritura.write("Uno \nDos \nTres")


# similar a la funcion "open", existe la funcion "close"

# esta debe llamarse una vez terminada lo que queriamos hacer

# Abrir un archivo en modo de escritura
archivo = open("ejemplo.txt", "w")

# Escribir datos en el archivo
archivo.write("Hola, mundo!\n")
archivo.write("Este es un ejemplo de archivo en Python.\n")

# Cerrar el archivo
archivo.close()
# archivo: Es el objeto de archivo que deseas cerrar, obtenido previamente al llamar a la función open().

# esto permite que el archivo de guarde correctamente, de no cerralo el archivo puede quedarse habierto mucho tiempo


"""La lengua de la
ballena azul pesa lo mismo
que un elefante"""

ejemplo = open("ejemplo.txt", "r")
a = ejemplo.readline()
b = ejemplo.readline()
c = ejemplo.readline()
d = a + c
print(d)  # la lengua de la que un elefante


"""MOOC 
significa
Massive
Open
Online
Course"""

a = open("mooc.txt")
linea = a.readline()
linea = a.readline()
linea = a.readline()
linea = a.readline()

print(linea)  # open


# Si tenemos el siguiente código, ¿cuál será el resultado, que quedará guardado en el archivo mooc.txt?
a = open("mooc.txt", "w")
a.write("1 2 3 4")
a.write("5 6 7 8")
a.close()
