'''modulo necesario para ficheros binarios
-es importante importar pickle'''
import pickle

nombres = ['Juan', 'Maria', 'Pedro', 'Pablo', 'Laura']

# Abrimos el fichero binario en modo escritura
fichero = open('binario.pckl', 'wb')

# Escribimos el contenido
pickle.dump(nombres, fichero)

# Para terminar cerrar el fichero
fichero.close()


