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

'''loc = accedemos por le nombre del indicede la fila'''

# loc = acceso por posicion [nombre_indice_fila]
print(df_desde_dict1.loc[2])


# Mostrar la fila 2 y la fila 4
print(df_desde_dict1.loc[[2, 4]])

# Mostrar desde el indice de la fila 2 a la fila 4
print(df_desde_dict1.loc[2:4])

# Solo la nota de pedro
print(df_desde_dict1.loc[2, ['Notas']])
print(df_desde_dict1.loc[[2, 4], ['Notas']])
print(df_desde_dict1['Notas'].loc[2])


print('.-----------------------------.')
# con rangos
print(df_desde_dict1.loc[2:4]['Notas'])

# Nonmber y apellido de ana
# print(df_desde_dict1.loc[3][['nombre', 'Apellido']])
