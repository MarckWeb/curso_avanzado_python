# Funciones en Python

En Python, una función es un bloque de código reutilizable que realiza una acción específica. Las funciones brindan una forma de estructurar el código de manera que permita su reutilización, lo que puede hacer que los programas sean más fáciles de leer y de mantener.

## Definición de funciones

La definición de una función comienza con la palabra clave _def_ seguida del nombre de la función y paréntesis _()_. Cualquier entrada o argumento debe colocarse dentro de estos paréntesis. Además, se puede definir una documentación de la función, llamada docstring, al comienzo de la función. Finalmente, el bloque de código dentro de cada función comienza con dos puntos : y está indentado.

Aquí hay un ejemplo de una función simple:

´´´py
def saludo(nombre):
"""
Esta función saluda a la persona pasada como parámetro
"""
print("Hola, " + nombre + ". ¡Buen día!")
´´´

## Llamada a funciones

Después de definir una función, puedes "llamarla" o "usarla" escribiendo simplemente el nombre de la función seguido de paréntesis () y los argumentos dentro de los paréntesis, si los hay.

´´´py
saludo('Pedro')
´´´
Cuando se ejecuta este código, se imprimirá _"Hola, Pedro. ¡Buen día!"_.

## Argumentos y parámetros

Las funciones en Python pueden tener argumentos o parámetros, que son valores que se pasan a la función en el momento de la llamada. Estos argumentos se colocan dentro de los paréntesis después del nombre de la función. Pueden agregarse tantos argumentos como se desee, separados por coma.

Por ejemplo, la siguiente función acepta dos parámetros, num1 y num2, y devuelve su suma:

´´´py
def sumar(num1, num2):
"""
Esta función suma los dos números pasados como parámetros
"""
return num1 + num2

resultado = sumar(5, 3) # 8
´´´

## Funciones con valores predeterminados

Python permite definir valores predeterminados para los argumentos que no se pasan durante la llamada a la función. Para hacer esto, se debe asignar el valor predeterminado utilizando el signo igual = en la definición de la función.

Por ejemplo:
´´´py
def saludo(nombre='Amigo'):
"""
Esta función saluda a la persona pasada como parámetro, o a 'Amigo' si no se proporciona un nombre
"""
print("Hola, " + nombre + ". ¡Buen día!")

saludo('Ana') # Output: Hola, Ana. ¡Buen día!
saludo() # Output: Hola, Amigo. ¡Buen día!
´´´

## Retorno de valores

La declaración return se utiliza para que la función devuelva un resultado que puede ser almacenado en una variable o usado de cualquier otra manera. Una vez que la función llega a una declaración de retorno, deja de ejecutar el código restante en la función y "devuelve" al lugar del programa donde fue llamada.

´´´py
def cuadrado(numero):
"""
Esta función retorna el cuadrado del número pasado como parámetro
"""
return numero \*\* 2

resultado = cuadrado(4)
print(resultado) # 16
´´´

Las funciones son una herramienta esencial en Python y en cualquier otro lenguaje de programación, ya que permiten crear código reutilizable y organizado.

## Importacion y llamado de modulos

- Existen muchas librerias o modulos ya programados.

- Realizan de todo tipo de tareas simples o complejas

- **ramdon** permite generar numeros pseudoaleatorios.
- **math** permite realizar calculos complejos y acceder a constantes conocidas.
- Permiten realizar acciones u simple llamado de una funcion

Existen varios metodos:
Primer metodo

```py
#
import <nombre modulo>
ejemplo
import math
```

Segundo metodo -. elemnetos que vamos a ocupar dentro de nuestro programa

```py
from <monbre modulo> import <elem1>, <elem2>

ejemplo
from math import pow, sqrt
```

Tercer metodo -. consiste en darles nombre especiales, para evitar duplicidad de nombre

```py
from <monbre modulo> import <elem1> as <alias>

ejemplo
from math import e as euler
```
