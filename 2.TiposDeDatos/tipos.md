# Tipos de datos

Python, como lenguaje de programación, tiene varios tipos de datos incorporados que pueden ser usados para manejar diferentes tipos de información.

## Números

En Python, los números pueden ser de diferentes tipos. Aquí hay cuatro tipos distintos de números:

1. **Enteros (int):** Estos son todos los números enteros, sin una parte decimal, tanto positivos como negativos. Por ejemplo:

```py
   a = 10
   print(type(a)) # <class 'int'>
```

2. **Números de punto flotante (float):** Estos son los números que tienen tanto una parte entera como una parte decimal. Pueden ser positivos o negativos. Por ejemplo:

```py
b = 10.5
print(type(b)) # <class 'float'>
```

3. **Números complejos (complex):** Estos son números que tienen una parte real y una parte imaginaria. Por ejemplo:

```py
c = 3 + 4j
print(type(c)) # <class 'complex'>
```

4. **Números de tipo booleano (bool):** Este tipo de datos solo puede tener dos valores: True (verdadero) o False (falso). Por ejemplo:

```py
d = True
print(type(d)) # <class 'bool'>
```

## Cadenas de texto (Strings)

Las cadenas de texto son una secuencia de caracteres y se definen utilizando comillas simples o dobles. Por ejemplo:

```py
str1 = 'Hola, Mundo!'
print(type(str1)) # <class 'str'>
```

Las cadenas pueden ser indexadas y también se pueden realizar operaciones de segmentación (slicing).

## Listas

Las listas son colecciones ordenadas y mutables de elementos. Los elementos de una lista están encerrados entre corchetes [] y están separados por comas. Por ejemplo:

```py
lista = [1, 'Hola', 3.14, True]
print(type(lista)) # <class 'list'>
```

Las listas en Python pueden contener diferentes tipos de datos.

## Tuplas

Las tuplas son similares a las listas, pero a diferencia de las listas, las tuplas son inmutables. Esto significa que una vez que una tupla es creada, no puede ser modificada. Las tuplas están encerradas entre paréntesis (). Por ejemplo:

```py
tupla = (1, 'Hola', 3.14, True)
print(type(tupla)) # <class 'tuple'>
```

## Conjuntos (Sets)

Los conjuntos son una colección de elementos que no están ordenados y no contienen duplicados. Los elementos de un conjunto están encerrados entre llaves {} y están separados por comas. Por ejemplo:

```py
conjunto = {1, 'Hola', 3.14, True}
print(type(conjunto)) # <class 'set'>
```

## Diccionarios

Los diccionarios son una colección no ordenada de pares clave-valor. Se definen utilizando llaves {}. La clave y el valor están separados por dos puntos :. Por ejemplo:

```py
diccionario = {'nombre': 'Juan', 'edad': 30}
print(type(diccionario)) # <class 'dict'>
```

En el ejemplo anterior, _'nombre'_ y _'edad'_ son las claves, y _'Juan'_ y _30_ son los valores correspondientes.

Estos son los principales tipos de datos en Python. Cada uno de ellos tiene sus propios métodos y funcionalidades que permiten a los programadores manipular datos de manera efectiva.
