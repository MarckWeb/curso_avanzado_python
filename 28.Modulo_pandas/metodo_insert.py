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


'''insert=> agrga columnas'''
print('-----Agregando insert el df-----')
resultado = ['Suspenso', 'Aprobado', 'Suspenso', 'Aprobado', 'Aprobado']
df_desde_dict1.insert(loc=3, column='Resultado', value=resultado)
print(df_desde_dict1)
print()

# Agergar datos del  f_desde_dict2 al f_desde_dict1
print('         concatenar tablas con _append')
df_desde_dict3 = df_desde_dict1._append(df_desde_dict2)
# df_desde_dict3 = pd.concat([df_desde_dict1, df_desde_dict2], ignore_index=True)
print(df_desde_dict3)
print()

# Concatenar los DataFrames utilizando pd.concat()
print('          Juntar tablas con .concat')
df_desde_dict3 = pd.concat([df_desde_dict1, df_desde_dict2], ignore_index=True)
print(df_desde_dict3)
