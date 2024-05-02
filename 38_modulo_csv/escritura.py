import csv

with open('contactos.csv', 'w', newline='') as contactoscsv:
    escribir = csv.writer(contactoscsv, delimiter=',')

    escribir.writerow(["Nombre", "Telefono"])
    escribir.writerow(["Juan", "222-222-555"])
    escribir.writerow(["David", "222-111-555"])
    escribir.writerow(["Alex", "222-000-555"])
    escribir.writerow(["Carlos", "222-333-555"])
    escribir.writerow(["Jokin", "222-444-555"])

# Mostrar datos del archivo contactos.csv
with open('contactos.csv', newline='') as empleadoscsv:
    datos = csv.reader(empleadoscsv, delimiter=",")
    for item in datos:
        print(item)
    print('-' * 50)
