import  platform

# funcion platform
print(platform.platform())
print(platform.platform(aliased=True))
print(platform.platform(aliased=True, terse=True))
print(platform.platform(0, 0))

# funcion machine: nombre generico del procesador
print(platform.machine())

# funcion procesador: nombre real del procesador
print(platform.processor())

# funcion system: nombre del sistema operativo
print(platform.system())

# funcion version: version del sistema operativo
print(platform.version())

# Funcion python_implementacion
print(platform.python_implementation())
print(platform.python_version()) # 3.12.2
print(platform.python_version_tuple()) # ('3', '12', '2')