import pandas as pd
# Creamos el datframe apartir del diccionario
diccionario = {
    "Id": [1, 2, 3, 4, 5],
    "Nombre": ['Juan', 'Pedro', 'Estefania', 'Ana', 'Esteban'],
    "Apellido": ['Garcia', 'Sanchez', 'Lopez', 'Garcia', 'Gonzalez'],
    "Nota": [4.5, 8.9, 1.4, 5.6, 7.8]
}

df_desde_dict1 = pd.DataFrame(diccionario)

dictNombreNotas2 = [
    {'Id': 6, 'Nombre': 'Silvia', 'Apellido': 'Salas', 'Nota': 5.5},
    {'Id': 7, 'Nombre': 'David', 'Apellido': 'Marck', 'Nota': 8.5},
]

df_desde_dict2 = pd.DataFrame(dictNombreNotas2)

resultado = ['Suspenso', 'Aprobado', 'Suspenso', 'Aprobado', 'Aprobado']
df_desde_dict1.insert(loc=3, column='Resultado', value=resultado)

# Concatenar los DataFrames utilizando pd.concat()
print('----Juntar tablas con .concat-----')
df_desde_dict3 = pd.concat([df_desde_dict1, df_desde_dict2], ignore_index=True)
print(df_desde_dict3)

# Mostrar cuantos aprobados o susènsos tenemos(tabla.group('nombre_fila)[Id].count())
print(df_desde_dict3.groupby('Resultado')['Id'].count())
print('')


print('Agrupar por apellido y resultado')
print(df_desde_dict3.groupby(['Apellido', 'Resultado'])['Id'].count())

'''
Con concat le agreamos mas lineas a las que ya habia, en la table df3 le agremos el df:nuevo
'''
data3 = [
    [8, 'Jorge', 'Garcia', 'Suspenso', 4.5],
    [9, 'Maria', 'Gonzales', 'Aprobado', 8.9]
]

df_nuevo = pd.DataFrame(data3, columns=df_desde_dict3.columns)
df_desde_dict3 = pd.concat([df_desde_dict3, df_nuevo]).reset_index(drop=True)
print('---Agregamso mas filas a la tabla3---\n', df_desde_dict3)

# print(df_desde_dict3.groupby(['Resultado']).mean())
print(df_desde_dict3.groupby('Resultado')['Nota'].mean())
print(df_desde_dict3.groupby("Resultado").mean(["Nota"]))
