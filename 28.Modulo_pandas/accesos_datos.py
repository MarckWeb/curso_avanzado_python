import pandas as pd
# Creamos el datframe apartir del diccionario
diccionario = {
    "Id": [1, 2, 3, 4, 5],
    "Nombre": ['Juan', 'Pedro', 'Estefania', 'Ana', 'Esteban'],
    "Apellido": ['Garcia', 'Sanchez', 'Lopez', 'Garcia', 'Gonzalez'],
    "Notas": [4.5, 8.9, 1.4, 5.6, 7.8]
}

df_desde_dict1 = pd.DataFrame(diccionario)
print(df_desde_dict1)

'''
para accede a las posicones se colocan los indices que empiezan de cero tanto en filas y columnas 
'''
print('-----.iloc[]----')
# metod iloc = accedemos a la posicion por [filas, columnas]-
print(df_desde_dict1.iloc[2, 3])

# Queremos obtener los datos desde la fila 1 a la 3
print(df_desde_dict1.iloc[1:3])  # solo la fila uno y dos
print(df_desde_dict1.iloc[1:3], )  # solo la fila uno y dos
# solo la fila uno y dos y al final fila
print(df_desde_dict1.iloc[1:3], 'fila')
print(df_desde_dict1.iloc[1:3, :])  # solo al fial 1 y 2 con todas las columnas

# Queremos obtener lso datos desde la fila 1 a la 3 solo conn las 3 primeras columnas
print(df_desde_dict1.iloc[1:3, :3])

print('------------ejercicios-------------')
# Mostrar todas las filas desde 0, solo 2 primeras columnas
print(df_desde_dict1.iloc[:, :2])
print(df_desde_dict1.iloc[:, 0:2])
