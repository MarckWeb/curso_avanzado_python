import shutil
import os

# Crear la estructura de directorios
os.makedirs('dir1/dir2/dir3')

# Eliminar dir1 y todos sus contenidos
shutil.rmtree('dir1')

# Verificar que dir1 y sus contenidos se han eliminado
'''if not os.path.exists('dir1'):
    print('dir1 ha sido eliminado con éxito.')
else:
    print('Ha ocurrido un error al eliminar dir1.')
'''
