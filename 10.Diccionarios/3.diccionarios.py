alumnos = {'Juan': 6.4, 'Maria': 8.3, 'Luis': 6.4, 'Adolfo': 7.1, 'Maria': 9.3}

# Recorrer un diccionario

for alumno in alumnos:  # solo me devuelve las claves
    print(alumno, alumnos[alumno])


for item in alumnos.items():
    print(item)  # Cada item es una tupla (clave, valor)

for clave, valor in alumnos.items():
    print(clave, ':', valor)


# Otras formas de crear diccionarios
alumnos = dict()
alumnos = {}
# alumnos = dict([('Juan', 6.4), ('Maria', 9.3), ('Luis', 6.4), ('Adolfo', 7.1)])
alumnos = dict(Juan=6.4, Maria=9.3, Luis=6.4, Adolfo=7.1)
print(alumnos)

# Eliminar todos los elemntos
alumnos.clear()
print(alumnos)
