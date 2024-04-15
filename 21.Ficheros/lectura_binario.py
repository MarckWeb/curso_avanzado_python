import pickle
# Abrir el fichero binario en modo lectura
# fichero = open('binario.bin', 'rb')
fichero = open('binario.pckl', 'rb')


# Leemos el contenido
nombres = pickle.load(fichero)

# mostrar el contenido leido
print(nombres)

# mostrar el tipo de dato y vemos que sigue siendo una lista
print(type(nombres)) # <class 'list'>

# cerrar el fichero
fichero.close()