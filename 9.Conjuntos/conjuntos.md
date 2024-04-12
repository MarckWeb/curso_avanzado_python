# Conjuntos

En Python, un conjunto (set) es una colección no ordenada de elementos únicos, que admite operaciones de teoría de conjuntos como la unión, intersección y diferencia. Los sets en Python son muy útiles cuando se requiere eliminar duplicados de una lista o comparar diferentes colecciones.

La principal característica de los sets es que solo pueden contener elementos únicos y no admiten índices, por lo que no se puede acceder a elementos específicos mediante índices. Los sets también son mutables, lo cual permite agregar o eliminar elementos una vez creado el set.

## Creación de sets

Para crear un set en Python, se pueden utilizar dos métodos. El primero es colocar todos los elementos del set entre llaves {} y separados por comas:

```py
conjunto_a = {1, 2, 3, 4, 5}
```

Otra forma de crear sets es utilizando la función set(), que convierte una lista o tupla en un conjunto:

```py
conjunto_b = set([1, 2, 3, 4, 5])
```

Es importante destacar que, aunque se utilice la función set() y se pasen elementos duplicados, estos serán eliminados y el conjunto solo contendrá elementos únicos:

```py
lista_duplicada = [1, 1, 2, 2, 3, 4, 5]
conjunto_c = set(lista_duplicada)
print(conjunto_c)  # Salida: {1, 2, 3, 4, 5}
```

## Métodos de los conjuntos

Los conjuntos en Python ofrecen una serie de métodos para trabajar con ellos.

- add(elemento): Agrega un elemento al conjunto.

```py
conjunto = {1, 2, 3}
conjunto.add(4)
print(conjunto)  # Salida: {1, 2, 3, 4}
```

- remove(elemento): Elimina un elemento del conjunto. Si el elemento no existe en el conjunto, se lanza un error KeyError.

```py
conjunto = {1, 2, 3}
conjunto.remove(2)
print(conjunto)  # Salida: {1, 3}
```

- discard(elemento): Elimina un elemento del conjunto si este existe; en caso contrario, no hace nada. Al contrario que remove, este método no lanzará ningún error si el elemento no existe.

```py
conjunto = {1, 2, 3}
conjunto.discard(3)
print(conjunto)  # Salida: {1, 2}
```

- clear(): Elimina todos los elementos del conjunto.

```py
conjunto = {1, 2, 3, 4, 5}
conjunto.clear()
print(conjunto)  # Salida: set()
```

## Operaciones con sets

En Python, se pueden realizar las operaciones clásicas de teoría de conjuntos, como la unión, intersección y diferencia:

- **Unión:** Une todos los elementos en un único set. Se pueden utilizar dos formas, el método union() o el operador |.

```py
conjunto_a = {1, 2, 3}
conjunto_b = {3, 4, 5}

union = conjunto_a.union(conjunto_b)
print(union)  # Salida: {1, 2, 3, 4, 5}

# Otra forma:
union = conjunto_a | conjunto_b
print(union)  # Salida: {1, 2, 3, 4, 5}
```

- **Intersección:** Obtiene todos los elementos que aparecen en ambos sets. Se pueden utilizar dos formas, el método intersection() o el operador &.

```py
conjunto_a = {1, 2, 3}
conjunto_b = {3, 4, 5}

interseccion = conjunto_a.intersection(conjunto_b)
print(interseccion)  # Salida: {3}

# Otra forma:
interseccion = conjunto_a & conjunto_b
print(interseccion)  # Salida: {3}
```

- **Diferencia:** Elimina del primer set todos los elementos que aparecen en el segundo. Se pueden utilizar dos formas, el método difference() o el operador -.

```py
conjunto_a = {1, 2, 3}
conjunto_b = {3, 4, 5}

diferencia = conjunto_a.difference(conjunto_b)
print(diferencia)  # Salida: {1, 2}

# Otra forma:
diferencia = conjunto_a - conjunto_b
print(diferencia)  # Salida: {1, 2}
```

En resumen, los conjuntos en Python son una herramienta versátil y eficiente para trabajar con colecciones de elementos únicos y realizar operaciones de la teoría de conjuntos de forma sencilla y rápida.
