import csv

with open('item.txt', 'w', newline='') as productoscsv:
    escribir = csv.writer(productoscsv, delimiter=',')

    for n in range(10):
        escribir.writerow(f'y {n}')

    # escribir.writerow(["ID", "Descripcion", "Precio"])
    # escribir.writerow([1, "Pantalla", 129.85])
    # escribir.writerow([2, "Teclado", 49.95])
    # escribir.writerow([3, "Mouse", 18])
    # escribir.writerow([4, "Scanner", 450])
    # escribir.writerow([5, "Impresora", 89.90])

# Mostrar datos del archivo productos.csv
# with open('productos.csv', newline='') as empleadoscsv:
#     datos = csv.reader(empleadoscsv, delimiter=",")
#     for item in datos:
#         print(item)
#     print('-' * 50)

# # Ecribir datos en archivo productos2.csv como diccionarios
# with open('productos2.csv', 'w', newline='') as productos2csv:
#     cabeceras = ['ID', 'Descripcion', 'Precio']
#     escribir = csv.DictWriter(productos2csv, fieldnames=cabeceras)

#     escribir.writeheader()
#     escribir.writerow({'ID': 1, 'Descripcion': "Pantalla", 'Precio': 120.35})
#     escribir.writerow({'ID': 2, 'Descripcion': "Scanner", 'Precio': 350})
#     escribir.writerow({'ID': 3, 'Descripcion': "Impresora", 'Precio': 70.35})
#     escribir.writerow({'ID': 4, 'Descripcion': "Mouse", 'Precio': 20.35})

