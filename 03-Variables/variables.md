# Variables

Una variable en Python es un espacio reservado en la memoria que almacena un valor. Este valor puede cambiar durante la ejecución de un programa y puede ser de varios tipos, como un número, una cadena de caracteres o una lista, entre otros. Las variables se crean mediante la asignación de un valor a un identificador.

## Declaración y asignación de variables

La declaración de variables en Python se realiza de manera dinámica, lo que significa que no es necesario definir explícitamente el tipo de dato que la variable va a almacenar, a diferencia de otros lenguajes de programación como C o Java.

```py
numero = 10
texto = "Hola mundo"
lista = [1, 2, 3]
```

## Tipos de datos

Python es un lenguaje de programación dinámico y fuertemente tipado. Esto significa que, aunque no es necesario declarar explícitamente el tipo de dato que una variable va a almacenar, cada variable tiene un tipo y Python realiza comprobaciones de tipo en tiempo de ejecución.

Los tipos de datos básicos en Python incluyen enteros, flotantes, cadenas y booleanos.

```py
entero = 1 # Tipo entero
flotante = 1.0 # Tipo flotante
cadena = "Hola" # Tipo cadena
booleano = True # Tipo booleano
```

## Nombres de variables

Los nombres de las variables en Python deben seguir algunas reglas. Estos nombres pueden contener letras (tanto minúsculas como mayúsculas), números y el carácter de subrayado (\_), pero no pueden empezar con un número. Además, Python distingue entre mayúsculas y minúsculas, por lo que _variable_, _Variable_ y _VARIABLE_ serían tres nombres de variables distintos.

Por convención, los nombres de las variables suelen empezar con una letra minúscula y, si están compuestos por varias palabras, se utilizan subrayados para separarlas (por ejemplo, _mi_variable_).

## Variables y memoria

Cuando se crea una variable, Python reserva un espacio en la memoria para almacenar su valor. Si a una variable se le asigna un nuevo valor, Python puede reservar un nuevo espacio en la memoria para este nuevo valor y hacer que la variable apunte a este nuevo espacio. Esto es importante porque significa que asignar un nuevo valor a una variable no cambia el valor original.

Por ejemplo:

```py
a = 1 # Python reserva un espacio en memoria para el valor 1 y hace que 'a' apunte a él
b = a # 'b' ahora apunta al mismo espacio en memoria que 'a'
a = 2 # Python reserva un nuevo espacio en memoria para el valor 2 y hace que 'a' apunte a él

# En este punto, 'b' sigue apuntando al espacio en memoria del valor 1
```

## Variables y mutabilidad

Las variables en Python pueden ser mutables o inmutables. Un objeto mutable es aquel que puede cambiar después de haber sido creado, mientras que un objeto inmutable es aquel que no puede cambiar después de haber sido creado.

Los tipos de datos básicos como enteros, flotantes, cadenas y booleanos son inmutables. Esto significa que, una vez que se ha creado una variable con uno de estos tipos de datos, su valor no puede cambiar. En cambio, lo que sucede cuando se asigna un nuevo valor a una de estas variables es que Python crea un nuevo objeto con el nuevo valor y hace que la variable apunte a este nuevo objeto.

Por otro lado, los tipos de datos como las listas y los diccionarios son mutables. Esto significa que se puede cambiar su contenido después de haber sido creados. Por ejemplo:

```py
lista = [1, 2, 3] # Se crea una lista
lista[0] = 10 # Se cambia el primer elemento de la lista

# Ahora 'lista' es [10, 2, 3]
```

## Variables locales y globales

Las variables en Python pueden ser locales o globales. Una variable local es una variable que se define dentro de una función y solo puede ser accedida dentro de esa función. Por otro lado, una variable global es una variable que se define fuera de todas las funciones y puede ser accedida tanto dentro como fuera de las funciones.

Por ejemplo:

```py
variable_global = "Soy global"

def mi_funcion():
   variable_local = "Soy local"
   print(variable_local)
   print(variable_global)

mi_funcion()

# Esto imprimirá:

# Soy local

# Soy global
```

En este caso, _variable_global_ es una variable global y puede ser accedida tanto dentro como fuera de mi*funcion(). Por otro lado, \_variable_local* es una variable local y solo puede ser accedida dentro de mi_funcion(). Si se intenta acceder a variable_local fuera de mi_funcion(), Python dará un error.

## Adicional

```py
x, y, z = 5, 10, 8
# Esto significa que x será igual a 5, y será igual a 10 y z será igual a 8.
x, y, z = z, y, x
# Luego, se realiza una reasignación utilizando la técnica de desempaquetado de tuplas:

# Entonces, después de esta asignación, x es 8, y es 10 y z es 5.

print(x > z)
print((y - 5) == x)

# True
# False
```

Cabe mencionar que si se define una variable con el mismo nombre tanto dentro como fuera de una función, la variable dentro de la función ocultará a la variable fuera de la función. Es decir, dentro de la función, el nombre de la variable se referirá a la variable local, mientras que fuera de la función, se referirá a la variable global.
