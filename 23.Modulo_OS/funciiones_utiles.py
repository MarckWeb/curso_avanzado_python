import os
import platform

# Nombre del sistema operativo
print("Nombre del sistema operativo:", os.name)

# Información detallada del sistema
print("Información del sistema:", platform.uname())

# Nombre del host/máquina
print("Nombre del host:", platform.node())

# Arquitectura del procesador
print("Arquitectura del procesador:", platform.architecture())

# Versión del sistema operativo
print("Versión del sistema operativo:", platform.version())

# Variables de entorno
print("Variables de entorno:", os.environ)

# Directorio actual
print("Directorio actual:", os.getcwd())

# Lista de archivos y directorios en el directorio actual
print("Archivos y directorios en el directorio actual:", os.listdir())
