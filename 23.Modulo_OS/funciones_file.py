import os

# Eliminar el directorio
os.rmdir('mi_carpeta')

# crear directorio
os.mkdir('mi_carpeta')
# print(os.listdir())

# Borramos directorios con subdirectorios antes de crear para no tener errores
os.removedirs('dir1/dir2/dir3')

# crear directorio con subdirectorios
os.makedirs('dir1/dir2/dir3')

# Mover entre directorios
os.chdir('dir1/dir2/')
# os.chdir('dir2') # FileNotFoundError: [WinError 2] El sistema no puede encontrar el archivo especificado: 'dir2'

# En que directorio estoy
print('estoy en,', os.getcwd())

# ejecutar cnn la funcion system
os.system('mkdir otro_directorio')

# Mostrar la fecha y hora del sistema
print(os.system('date'))
