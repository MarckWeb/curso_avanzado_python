# Estructura de Control

Las estructuras de control en Python son bloques de código que permiten controlar el flujo del programa. Esto significa que determinan cómo se ejecutan las instrucciones del código, dependiendo de ciertas condiciones o mientras una condición se mantenga. En Python, las estructuras de control principales son las condicionales _(if, elif, else)_ y las de bucle _(for, while)_.

## Estructuras de control condicionales

Las estructuras de control condicionales permiten ejecutar bloques de código según se cumplan ciertas condiciones.

### if

La sentencia if es la más simple y básica. Permite ejecutar un bloque de código si se cumple una condición.

```py
numero = 10
if numero > 5:
    print("El número es mayor a 5")
```

En este ejemplo, Python evaluará si la condición _numero > 5_ es verdadera. Si lo es, ejecutará el bloque de código indentado que sigue al if, en este caso, _print("El número es mayor a 5")_.

### else

La sentencia else se utiliza en combinación con if. El bloque de código después de else se ejecutará si ninguna de las condiciones anteriores se cumple.

```py
numero = 4
if numero > 5:
print("El número es mayor a 5")
else:
print("El número es 5 o menor")
```

### elif

La sentencia elif es una contracción de "else if". Se utiliza para verificar múltiples condiciones después de la condición inicial verificada por if.

```py
numero = 12
if numero > 15:
print("El número es mayor a 15")
elif numero > 10:
print("El número es mayor a 10")
else:
print("El número es 10 o menor")
```

En este ejemplo, Python primero comprobará si _numero > 15_. Si no es verdadero, pasa a la siguiente condición, _numero > 10_. Si ninguna de las condiciones se cumple, ejecutará el bloque de código después del else.

## Estructuras de control de bucle

Las estructuras de control de bucle permiten ejecutar bloques de código varias veces, normalmente hasta que se cumple una determinada condición.

### for

La sentencia for en Python se utiliza para iterar sobre una secuencia (como una lista, tupla, diccionario, conjunto o cadena) o un generador.

```py
for i in range(5):
print(i)
```

En este ejemplo, i tomará cada valor de la secuencia generada por range(5), es decir, de 0 a 4. Para cada uno de estos valores, se ejecutará el bloque de código print(i).

### while

La sentencia while en Python permite ejecutar un bloque de código mientras se cumple una condición.

```py
i = 0
while i < 5:
print(i)
i += 1
```

En este ejemplo, el bloque de código se ejecutará mientras la condición _i < 5_ sea verdadera. Para cada iteración del bucle, se incrementa el valor de i en uno.

### break, continue y pass

Estas son sentencias que se utilizan para cambiar el flujo de bucles.

- **break:** Termina el bucle y pasa el control a la siguiente línea después del bucle.

- **continue:** Salta el resto de la iteración actual y pasa a la siguiente iteración.

- **pass:** Es una operación nula, no hace nada y se usa cuando se requiere por la sintaxis pero no se desea ejecutar ningún código. Suele utilizarse como marcador de posición (placeholder) cuando aún no está preparado el código real.

```py
for i in range(5):
if i == 3:
break
print(i)

largest_number = -99999999
counter = 0

while True:
    number = int(input("Ingresa un número o escribe -1 para finalizar el programa: "))
    if number == -1:
        break
    counter += 1
    if number > largest_number:
        largest_number = number

if counter != 0:
    print("El número más grande es", largest_number)
else:
    print("No has ingresado ningún número.")
```

Este código imprimirá 0, 1 y 2. Cuando i sea igual a 3, la sentencia break terminará el bucle.

En conclusión, las estructuras de control son esenciales en cualquier programa Python, permitiendo crear lógica compleja y controlar cómo y cuándo se ejecutan determinadas partes del código.
