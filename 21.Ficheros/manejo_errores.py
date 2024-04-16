import errno
from os import strerror

try:

    # esta variable al estar fuera de cualquier funcion, es una variable global
    stream = open('aaaa.txt', 'rt')
except IOError as ex:
    print(ex.errno)  # 2
    print('', strerror(ex.errno))
    '''if ex.errno == errno.EACCES:
        print('No tienes permiso para abrir ese fichero')
    elif ex.errno == errno.ENOENT:
        print('Ese archivo no existe')'''

    # A partir de python 3.7

    match ex.errno:
        case errno.EACCES:
            print('No tienes permiso para abrir ese fichero')
        case errno.ENOENT:
            print('Ese archivo no existe')
        case _:  # Default
            print('Otro error')

finally:
    # comprobar si la variable stream se ha creado como varaible global
    if 'stream' in globals():
        stream.close()
    '''try:
        stream.close()
    except:
        print('Error al cerrar ')'''
