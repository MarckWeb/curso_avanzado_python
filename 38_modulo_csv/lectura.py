import csv

# Mostrar datos como un alista por cada linea
with open('empleados.csv', newline='') as empleadoscsv:
    datos = csv.reader(empleadoscsv, delimiter=",")
    for item in datos:
        # como lista ['Id', 'Nombre', 'Apellido', 'Email', 'Sueldo']
        print(item)
    print('-' * 50)

# Mostrar lista en texto con separador
with open('empleados.csv', newline='') as empleadoscsv:
    datos = csv.reader(empleadoscsv, delimiter=",")
    for item in datos:
        print("-".join(item))  # como texto id-Nombre-Apellido-Email-Sueldo
    print('-' * 50)

# Mostrar datos como doccionario
with open('empleados.csv', newline='') as empleadoscsv:
    datos = csv.DictReader(empleadoscsv, delimiter=",")
    for item in datos:
        print('_'*40)
        print(item)
        print('_'*40)
        print("ID:", item['Id'])
        print("Nombre:", item['Nombre'])
        print("Apellido:", item['Apellido'])
        print("Email:", item['Email'])
        print("Sueldo:", item['Sueldo'])
    print('-' * 50)

# Mostrar datos como doccionario
with open('empleados.csv', newline='') as empleadoscsv:
    cabeceras = ['Id', 'Nombre', 'Apellido', 'Email', 'Sueldo']
    datos = csv.DictReader(empleadoscsv, delimiter=",", fieldnames=cabeceras)
    for item in datos:
        print('_'*40)
        print(item['Nombre'], item['Sueldo'])
        print('_'*40)
    print('-' * 50)
