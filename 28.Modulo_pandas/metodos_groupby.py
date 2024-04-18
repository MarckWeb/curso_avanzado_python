import pandas as pd
# Creamos el datframe apartir del diccionario
diccionario = {
    "Id": [1, 2, 3, 4, 5],
    "Nombre": ['Juan', 'Pedro', 'Estefania', 'Ana', 'Esteban'],
    "Apellido": ['Garcia', 'Sanchez', 'Lopez', 'Garcia', 'Gonzalez'],
    "Nota": [4.5, 8.9, 1.4, 5.6, 7.8]
}

df_desde_dict1 = pd.DataFrame(diccionario)
print(df_desde_dict1)

dictNombreNotas2 = [
    {'Id': 6, 'Nombre': 'Silvia', 'Apellido': 'Salas', 'Nota': 5.5},
    {'Id': 7, 'Nombre': 'David', 'Apellido': 'Marck', 'Nota': 8.5},
]

df_desde_dict2 = pd.DataFrame(dictNombreNotas2)
print(df_desde_dict2)
