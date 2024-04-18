# DATA FRAMES
import pandas as pd

# crear un dataframe a partir de una lista
data2 = [
    ['Juan', 4.5],
    ['Pedro', 8.9],
    ['Estefania', 1.4],
    ['Ana', 5.6],
    ['Esteban', 7.9]
]

columnas_nombres = ['Nombre', 'Nota']
filas = list(range(len(data2)))  # [0,1,2,3,4]
df = pd.DataFrame(data2, columns=columnas_nombres, index=filas)
print(df)

# Obtener informacion
print('informacion', df.info)

# Mostrar la forma del dataframe
print('filas y columnas de df', df.shape)

# Tamaño del dataframe (num_filas * num_columnas)
print('Tamaño o numero de celdas', df.size)

# Mostrar los nombres de columnas
print('las columans son:', df.columns)

# Tipos de datos de las columnas
print('tipo de datos de df', df.dtypes)

# Mostrar los tres primeros filas
print('3 primeros', df.head(3))

# Mpstrar las 3 ultimas filas
print('3 ultimas', df.tail(3))


# Creamos el datframe apartir del diccionario
diccionario = {
    "Id": [1, 2, 3, 4, 5],
    "Nombre": ['Juan', 'Pedro', 'Estefania', 'Ana', 'Esteban'],
    "Apellido": ['Garcia', 'Sanchez', 'Lopez', 'Garcia', 'Gonzalez'],
    "Notas": [4.5, 8.9, 1.4, 5.6, 7.8]
}

dfDesdeDict1 = pd.DataFrame(diccionario)
print(dfDesdeDict1)


# Otra forma de crear el dataframe a apartir de un diccionario
print('------------Otra forma DATAFRAME--------')
dictNombreNotas2 = [
    {'Id': 6, 'Nombre': 'Silvia', 'Apellido': 'Salas', 'Nota': 5.5},
    {'Id': 7, 'Nombre': 'David', 'Apellido': 'Marck', 'Nota': 8.5},
]

df_desde_dict2 = pd.DataFrame(dictNombreNotas2)
print(df_desde_dict2)
