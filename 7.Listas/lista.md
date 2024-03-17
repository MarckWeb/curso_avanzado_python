# Listas

Una lista en Python es una colección ordenada y modificable de elementos _(secuencia de elementos)_. Los elementos pueden ser de cualquier tipo: números, cadenas, booleanos, objetos, e incluso otras listas. Esto significa que las listas en Python son estructuras de datos heterogéneas, es decir, pueden contener diferentes tipos de datos en la misma lista.

Para crear una lista en Python, se utilizan corchetes [], y los elementos de la lista se separan por comas ,. A continuación, se presenta un ejemplo de cómo se define una lista:

```py
mi_lista = [1, 2, 3, "manzana", True, 3.14, ["otra", "lista"]]
```

En este ejemplo, mi_lista contiene varios tipos de datos: números enteros, una cadena de texto, un booleano, un número flotante y otra lista.

## Acceso a elementos de la lista

Para acceder a los elementos de la lista, se utiliza el índice del elemento. El índice es un número que representa la posición de un elemento en la lista. En Python, los índices comienzan en 0, lo que significa que el primer elemento de la lista tiene el índice 0. Para acceder a un elemento de la lista, se coloca el índice entre corchetes después del nombre de la lista:

```py
mi_lista = [1, 2, 3, "manzana", True, 3.14, ["otra", "lista"]]
primer_elemento = mi_lista[0] # 1
cuarto_elemento = mi_lista[3] # "manzana"
septimo_elemento = mi_lista[6] # ["otra", "lista"]
```

Además, Python permite el uso de índices negativos, que cuentan desde el final de la lista. Por ejemplo, el índice -1 se refiere al último elemento de la lista, -2 al penúltimo elemento, y así sucesivamente.

```py
mi_lista = [1, 2, 3, "manzana", True, 3.14, ["otra", "lista"]]
ultimo_elemento = mi_lista[-1] # ["otra", "lista"]
penultimo_elemento = mi_lista[-2] # 3.14
```

## Modificación de una lista

Las listas en Python son modificables, lo que significa que es posible cambiar, agregar o eliminar elementos después de que la lista haya sido creada.

Para cambiar el valor de un elemento específico, se puede acceder al índice y asignar un nuevo valor:

```py
mi_lista = [1, 2, 3, "manzana", True, 3.14, ["otra", "lista"]]
mi_lista[1] = "dos" # Cambia el segundo elemento a "dos"
print(mi_lista) # [1, 'dos', 3, 'manzana', True, 3.14, ['otra', 'lista']]
```

Para agregar un elemento a la lista, puedes usar el método append() que añade el elemento al final de la lista:

```py
mi_lista = [1, 2, 3, "manzana", True, 3.14, ["otra", "lista"]]
mi_lista.append("nuevo elemento") # Añade "nuevo elemento" al final de la lista
print(mi_lista) # [1, 2, 3, 'manzana', True, 3.14, ['otra', 'lista'], 'nuevo elemento']
```

Si se quiere insertar un elemento en una posición específica, puede usarse el método insert(indice, elemento):

```py
mi_lista = [1, 2, 3, "manzana", True, 3.14, ["otra", "lista"]]
mi_lista.insert(1, "insertado") # Inserta "insertado" en la segunda posición
print(mi_lista) # [1, 'insertado', 2, 3, 'manzana', True, 3.14, ['otra', 'lista']]
```

Para eliminar un elemento, pueden usarse los método remove() o pop(). remove(elemento) elimina la primera aparición del elemento especificado, y pop(indice) elimina el elemento en la posición especificada:

```py
mi_lista = [1, 2, 3, "manzana", True, 3.14, ["otra", "lista"]]
mi_lista.remove(1) # Elimina el 1 de la lista
print(mi_lista) # [2, 3, 'manzana', True, 3.14, ['otra', 'lista']]
mi_lista.pop(1) # Elimina el elemento en la segunda posición (3)
print(mi_lista) # [2, 'manzana', True, 3.14, ['otra', 'lista']]
```

## Recorrer una lista

En Python, es posible recorrer los elementos de una lista utilizando un bucle for. Este tipo de bucle repite una serie de instrucciones para cada elemento de la lista. Un ejemplo:

```py
mi_lista = [1, 2, 3, "manzana", True, 3.14, ["otra", "lista"]]

for elemento in mi_lista:
print(elemento)
```

Este código imprimirá cada elemento de la lista en una nueva línea.

## Métodos de lista

Los métodos de listas en Python son funciones incorporadas que realizan operaciones específicas en listas. Algunos de los métodos más utilizados son:

**_extend:_** Este método se utiliza para concatenar dos listas, extendiendo la primera lista con los elementos de la segunda.

```py
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista1.extend(lista2)

# Resultado: [1, 2, 3, 4, 5, 6]
```

**_index:_** Este método devuelve el índice del primer elemento con el valor especificado en la lista.

```py
lista = [1, 2, 3, 2]
indice = lista.index(2)

# Resultado: indice = 1
```

**_count:_** Este método devuelve el número de veces que el valor especificado aparece en la lista.

```py
lista = [1, 2, 3, 2]
numero_de_veces = lista.count(2)

# Resultado: numero_de_veces = 2
```

**_sort:_** Este método ordena los elementos de una lista en orden ascendente.

```py
lista = [3, 1, 4, 2]
lista.sort()

# Resultado: [1, 2, 3, 4]
```

**_reverse:_** Este método invierte el orden de los elementos de la lista.

```py
lista = [3, 1, 4, 2]
lista.reverse()

# Resultado: [2, 4, 1, 3]
```

**_insert:_** Este método inserta un nuevo elemento dentro de la lista y en el indice indicado.

```py
lista = [3, 1, 4, 2]
lista.insert(1, 100)

# Resultado: [3, 100, 1, 4, 2]
```

En resumen, las listas son una herramienta fundamental en Python que permiten almacenar y manipular colecciones de datos de manera eficiente. Permiten una gran flexibilidad, ya que los elementos de la lista pueden ser de cualquier tipo y se pueden modificar después de que la lista haya sido creada.
