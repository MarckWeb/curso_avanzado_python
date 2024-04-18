import pandas as pd

'''
         TIPOS DE MERGE
- inner => solo coge lso datos en comun
- left => todo lso de la izq + lso en comun
- right => todo lso de la derch + lso en comun
- outer => todos
'''


# Preparamos las dos tablas con DataFrames con un campo en comun
dict1 = [
    {'Id': 1, 'Nombre': 'Pantalla', 'Precio': 129.50},
    {'Id': 2, 'Nombre': 'Teclado', 'Precio': 49.95},
    {'Id': 3, 'Nombre': 'Mouse', 'Precio': 19.75},
    {'Id': 4, 'Nombre': 'Escaner', 'Precio': 300}
]
df1 = pd.DataFrame(dict1)

dict2 = [
    {'Nombre': 'Pantalla', 'Proveedor': 'lenovo'},
    {'Nombre': 'Teclado', 'Proveedor': 'Logitech'},
    {'Nombre': 'Mouse', 'Proveedor': 'Mocrosoft'},
    {'Nombre': 'Impresora', 'Proveedor': 'HP'}
]
df2 = pd.DataFrame(dict2)

print('----TABLA_1------')
print(df1)
print('-' * 50)
print('----TABLA_2------')
print(df2)
print('-' * 50)


# Utilizamso merge inner

df_inner = pd.merge(df1, df2, how='inner', on=['Nombre'])
print('----TABLA_CON_INNER------')
print(df_inner)
print('-' * 50)


# Utilizamso merge left

df_left = pd.merge(df1, df2, how='left', on=['Nombre'])
print('----TABLA_CON_LEFT------')
print(df_left)
print('-' * 50)

# Utilizamso merge right

df_right = pd.merge(df1, df2, how='right', on=['Nombre'])
print('----TABLA_CON_RIGHT df1 y df2------')
print(df_right)
print('-' * 50)

# Utilizamso merge right-. pero cambiando la posicion de las tablas de dercha a izquierda

df_right = pd.merge(df2, df1, how='right', on=['Nombre'])
print('----TABLA_CON_RIGHT df2 y df1------')
print(df_right)
print('-' * 50)
'''
NOTA-. El 
'''

# Utilizamso merge outer
df_outer = pd.merge(df1, df2, how='outer', on=['Nombre'])
print('----TABLA_CON_OUTER df1 y df2------')
print(df_outer)
print('-' * 50)

# Ordenamos la tabla por preccio de forma descendiente
df_outer = pd.merge(
    df1,
    df2,
    how='outer',
    on=['Nombre']
).sort_values('Precio', ascending=False)

print('----TABLA_CON_OUTER_ORDENADO X PRECIO DESC------')
print(df_outer)
print('-' * 50)

# Filtrar por Proveedor HP
print('----TABLA_CON_OUTER_FILTRADO_X_HP------')
print(df_outer[df_outer['Proveedor'] == 'HP'])
print('-' * 50)

# Mostrar los productos con precio inferior a 100
print('----TABLA_FILTRADO_X_Precio < 100------')
print(df_outer[df_outer['Precio'] < 100])
print('-' * 50)

# Mostrar los productos con más de 5 caracteres en el nombre y precio inferior a 100
filtro = (df_outer['Nombre'].str.len() > 5) & (df_outer['Precio'] < 100)
print('----TABLA_FILTRADO_X_Precio < 100------')
print(df_outer[filtro])
print('-' * 50)

'''Utilizamos DROP Borrar'''
#
