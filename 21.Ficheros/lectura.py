# Abrir el fichero en modo lectura

# tienen ruta basoluta y ruta relativa

fichero = open('fichero.txt', 'rt', encoding='utf-8')

# leer todo el contenido del fichero

texto = fichero.read()
print(texto)
print(type(texto)) # <class 'str'>

# muestar una lista de las filas sin salto de linea
lineass = texto.splitlines()
print(lineass)

# mover el curso al inicio
fichero.seek(0)

# leer todo el contenido pero me lo devulve como una lista
lineas = fichero.readlines()
print(lineas)
print(type(lineas))

# crear una lista con el contenido leido
fichero.seek(0)
lista = list(fichero)
print(lista)

# Cerrar el fichero
fichero.close()

