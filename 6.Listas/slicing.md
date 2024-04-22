# SLICING

### Dirección de la Secuencia:

- Las listas en Python son secuencias ordenadas.
- Los índices positivos se cuentan desde el principio de la lista (izquierda a derecha).
- Los índices negativos se cuentan desde el final de la lista (derecha a izquierda).

### Índices Positivos:

- Si usas índices positivos en el "slicing", estás especificando la posición de inicio y fin de izquierda a derecha.

```py
  lista = [0, 1, 2, 3, 4]
  resultado = lista[1:3] # [1, 2]
```

### Índices Negativos:

Si usas índices negativos en el "slicing", estás especificando la posición de inicio y fin de derecha a izquierda.

```py
lista = [0, 1, 2, 3, 4]
resultado = lista[-3:-1] # [2, 3]
```

### Sin Índices:

Si omites el inicio o el fin, Python utiliza automáticamente el principio o el final de la lista, respectivamente.

```py
lista = [0, 1, 2, 3, 4]
resultado = lista[:3] # [0, 1, 2]
resultado = lista[2:] # [2, 3, 4]
```

### Uso de Pasos:

Puedes especificar un paso para seleccionar elementos de manera alternada.

```py
lista = [0, 1, 2, 3, 4, 5, 6]
resultado = lista[::2] # [0, 2, 4, 6]
```

Seleccionar Todos los Elementos en Orden Inverso:

```py
lista = [0, 1, 2, 3, 4, 5]
resultado = lista[::-1]  # [5, 4, 3, 2, 1, 0]
```

Seleccionar Cada Segundo Elemento en Orden Inverso:

```py
lista = [0, 1, 2, 3, 4, 5]
resultado = lista[::-2]  # [5, 3, 1]
```

Seleccionar un Rango de Elementos en Orden Inverso:

```py
lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
resultado = lista[-3:-8:-1]  # [7, 6, 5, 4, 3]
```

En el tercer ejemplo:

- -3: Selecciona el tercer elemento desde el final de la lista.
- -8: Selecciona el octavo elemento desde el final de la lista.
- -1: Indica que el paso es negativo, es decir, los elementos se seleccionarán en orden inverso.
