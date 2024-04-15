'''
    abrir el fichero en modo lectura
    leer el contenido y copiarlo en fichero.txt
    mostrar el contenido fichero.txt
'''
# abrir el fichero en modo lectura
fichero_lectura = open('fichero.txt', 'rt', encoding='utf-8')

# Abrir el fichero en modo escritura
fichero_escritura = open('fichero2.txt', 'w+t', encoding='utf-8')

# Leer el contenido del fichero.txt
contenido = list(fichero_lectura)
# contenido = fichero_lectura.readline()


# Recorrer la lista de lineas y por cada una la escribimso en fichero2.txt
for linea in contenido:
    fichero_escritura.write(linea)

# Leer el contenido creado en fichero2.txt
fichero_escritura.seek(0) # mover el cursor al principio
for linea in fichero_escritura.readlines():
    print(linea, end='')

# cerrar los ficheros
fichero_lectura.close()
fichero_escritura.close()