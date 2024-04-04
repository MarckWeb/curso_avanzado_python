# Funciones lambda

Las funciones lambda en Python son una forma de crear pequeñas funciones anónimas. Estas funciones se llaman "anónimas" porque no se declaran de la forma estándar utilizando la palabra clave _def_. Puede usarse la palabra clave _lambda_ para crear pequeñas funciones anónimas.

## Sintaxis de las funciones lambda

La sintaxis de las funciones lambda es más sencilla que la sintaxis tradicional de las funciones en Python definidas con def. La sintaxis general es la siguiente:

```py
lambda argumentos: expresion
```

_lambda_ es la palabra clave que indica que se está creando una función lambda. _argumentos_ es una lista de argumentos separados por comas, sin paréntesis. _expresion_ es una expresión que se evalúa y devuelve el resultado cuando se llama a la función.

Aquí hay un ejemplo de una función lambda simple que toma un argumento y devuelve ese argumento incrementado en 1:

```py
f = lambda x: x + 1
print(f(1)) # Devuelve: 2
```

## Características de las funciones lambda

Las funciones lambda son muy útiles cuando se necesita una pequeña función que se va a utilizar una sola vez. Algunas características son:

- Pueden tomar cualquier número de argumentos, pero sólo pueden tener una expresión.
- No se les puede asignar un nombre directamente.
- Se pueden usar en cualquier lugar donde se requieran objetos de función.
- Tienen su propio espacio de nombres y no pueden acceder a otras variables fuera de su lista de argumentos.

Por ejemplo, aquí se muestra cómo utilizar una función lambda para definir una función que calcula el cuadrado de un número:

```py
f = lambda x: x ** 2
print(f(4)) # Devuelve: 16
```

## Funciones lambda en combinación con funciones como filter(), map() y reduce()

Las funciones lambda son particularmente útiles en combinación con las funciones incorporadas en Python filter(), map(), y reduce().

La función _filter(función, secuencia)_ ofrece una forma elegante de filtrar todos los elementos de una lista. La función función necesita devolver un valor booleano (verdadero o falso). Esta función se aplicará a cada elemento de la lista secuencia. Solo si función devuelve True, el elemento del secuencia será incluido en el resultado.

Por ejemplo, aquí hay una forma de utilizar filter() y una función lambda para obtener una lista de todos los números pares en una lista:

```py
lista = [1, 2, 3, 4, 5, 6]
pares = filter(lambda x: x % 2 == 0, lista)
print(list(pares)) # Devuelve: [2, 4, 6]
```

La función _map(función, secuencia)_ trabaja de manera similar a filter(), pero en lugar de aplicar una condición a los elementos de secuencia, aplica función a todos los elementos de la secuencia.

Por ejemplo, aquí se muestra cómo se puede usar map() y una función lambda para calcular el cuadrado de todos los números en una lista:

```py
lista = [1, 2, 3, 4, 5, 6]
cuadrados = map(lambda x: x ** 2, lista)
print(list(cuadrados)) # Devuelve: [1, 4, 9, 16, 25, 36]
```

La función _reduce(función, secuencia)_ es un poco diferente a filter() y map() porque no devuelve una lista, sino un solo valor calculado a partir de los elementos de la secuencia. Para usar reduce() es necesario importar el módulo functools.

Por ejemplo, aquí se muestra cómo se puede usar reduce() y una función lambda para calcular el producto de todos los números en una lista:

```py
from functools import reduce

lista = [1, 2, 3, 4, 5, 6]
producto = reduce(lambda x, y: x * y, lista)
print(producto) # Devuelve: 720
```

Las funciones lambda son una herramienta potente que permite escribir código más limpio y eficiente en Python, y pueden resultar especialmente útiles en casos en los que solo se necesite una pequeña función por un corto periodo de tiempo.
