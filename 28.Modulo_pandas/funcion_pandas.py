# importamos el modulo pandas
import pandas as pd

# Crear una serie apartir de una lista de nombres
lista = ['Juan', 'Pedro', 'Estefania', 'Ana', 'Esteban']
serie = pd.Series(lista, dtype='string')
print(serie)
'''
0         Juan
1        Pedro
2    Estefania
3          Ana
4      Esteban
dtype: string
'''

# Crear una serie a partir de un diccionario
# diccionario = dict(
#     [(0, "Juan"), (1, "Pedro"), (2, "Estefania"), (3, 'AnA'), (4, "Esteban")])
# print(diccionario)

diccionario = {0: "Juan", 1: "Pedro", 2: "Estefania", 3: 'AnA', 4: "Esteban"}
diccionario = {key: lista[key] for key in range(len(lista))}
# {0: 'Juan', 1: 'Pedro', 2: 'Estefania', 3: 'Ana', 4: 'Esteban'}
print(diccionario)

serie = pd.Series(diccionario)
print(serie)
'''
0         Juan
1        Pedro
2    Estefania
3          Ana
4      Esteban
dtype: object
'''
print('Longitud', serie.size)  # Longitud 5

# Index([0, 1, 2, 3, 4], dtype='int64')
print('Indices de la serie:', serie.index)

print('Tipo', serie.dtype)  # Tipo object

# Acceder a los elemetos por posicion
print('2 primeros', serie[:2])

print(serie[1:3])  # el 3 no esta incluido

# In[19]:
serie[2:]
# In[20]:

# Acceder a los elementos por indice
print(serie[0])

# In[22]:

print(serie[len(serie) - 1])


# In[24]:
print(serie[[0, 3]])

# In[26]:


# Ejecutar lambdas con apply
serie.apply(lambda nombre: nombre.upper())

# Ejercicio
# Crear una serie de numeros y retorna la serie multiplicados *2
# Con la serie de nombres creada anteriormente, retornar solo los que tienen mas de 4 caracteres


numeros = pd.Series(n*2 for n in range(11))
# numeros.apply(lambda num: num*2)
print(numeros)


# Craer filtro
filtro = serie.apply(lambda nombre: len(nombre) > 4)
print(serie[filtro])

# Crear un filtro para que solo me devuelva JUAN y ANA

filtro2 = serie.apply(lambda nombre: nombre in ['Juan', 'Ana'])
print(serie[filtro2])

# Otra forma de crear filtros
print(serie[(serie == 'Juan') | (serie == 'Ana')])
