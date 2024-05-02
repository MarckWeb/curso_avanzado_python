import csv

# Agregar más contenido al archivo CSV
with open('contactos.csv', 'a', newline='') as contactoscsv:
    escribir = csv.writer(contactoscsv, delimiter=',')
    # Escribir nuevas filas
    escribir.writerow([6, "Altavoces", 79.99])
    escribir.writerow([7, "Webcam", 39.50])

# Mostrar datos actualizados del archivo contactos.csv
with open('contactos.csv', newline='') as empleadoscsv:
    datos = csv.reader(empleadoscsv, delimiter=",")
    for item in datos:
        print(item)
    print('-' * 50)
