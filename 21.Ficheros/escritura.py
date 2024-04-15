# Abrir un fichero en modo escritura
'''
Dos formas de trabajar
    - ruta absoluta

    - ruta relativa
'''
# ruta relativa
# fichero = open('/User/usuario/desktop/fichero.txt', 'wt', encoding='utf-8' )

# ruta absoluta
fichero = open('fichero.txt', 'wt', encoding='utf-8')
texto = 'Esto es una prueba'
fichero.write(texto)

# se escribira a continuacion de la linea
#fichero.write('mas cosas')

# Cerrar el fichero
fichero.close()

'''
try:
    fichero= open('fichero.txt', 'wt', encoding='utf-8')
except:
    print('Error al abrir fichero')
else:
    texto = 'Esto al abrir el fichero'
    fichero.write(texto)
finally:
    fichero.close()
'''