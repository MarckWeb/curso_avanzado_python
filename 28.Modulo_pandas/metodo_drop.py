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


# Concatenar los DataFrames utilizando pd.concat()
df_desde_dict3 = pd.concat([df_desde_dict1, df_desde_dict2], ignore_index=True)
print('-----TABLA_ORIGINAL------')
print(df_desde_dict3)
print('_'*50)


# Si borro un acolumna, para qu el datframe se actualice hay que hacer una asignacion
df_desde_dict3 = df_desde_dict3.drop(4, axis=0)
print('-----TABLA_ELIMINAR_ESTEBAN------')
print(df_desde_dict3)
print('_'*50)

# Borrar 2 filas. las que tienen el indice 3 y 6 de indice
df_desde_dict3 = df_desde_dict3.drop([3, 6], axis=0)
print('-----TABLA_ELIMINAR_FILAS_3 Y 6------')
print(df_desde_dict3)
print('_'*50)

# Borrar por rango de fila desde 0 hasta el 2 -1
df_desde_dict3 = df_desde_dict3.drop(range(0, 2), axis=0)
print('-----TABLA_ELIMINAR_RANGO_0Y 2------')
print(df_desde_dict3)
print('_'*50)

# Datos Unicos
print(df_desde_dict3['Apellido'].unique())
print(df_desde_dict3['Apellido'].unique().tolist())

# Aplicar
