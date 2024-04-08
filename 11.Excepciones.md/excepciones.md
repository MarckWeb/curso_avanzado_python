# Excepciones

Las excepciones en Python son eventos que se producen durante la ejecución de un programa y que alteran el flujo normal del mismo. Cuando un error ocurre en Python, el intérprete lanza o emite una excepción, que si no es debidamente manejada, terminará el programa e imprimirá un mensaje de error.

Las excepciones se pueden manejar usando bloques de código _try, except, finally, y else_. Este manejo de excepciones permite controlar el flujo del programa y tomar decisiones en caso de errores.

## Uso básico de las excepciones

### Bloque try/except

El manejo de excepciones en Python se realiza mediante el uso de bloques try/except. Un bloque try contiene el código que podría lanzar una excepción. Si se produce una excepción en cualquier parte del bloque try, el flujo de ejecución se moverá inmediatamente a un bloque except correspondiente.

Aquí está el uso más básico de una declaración try/except:

```py
try: # código que podría lanzar una excepción
x = 1 / 0
except: # qué hacer si la excepción ocurre
print("Ha ocurrido una excepción")
```

Si se ejecuta este código, el programa no se detiene con un error. En cambio, se imprime "Ha ocurrido una excepción".

## Especificar el tipo de excepción

Es posible especificar qué tipo de excepción se quiere manejar en un bloque except. Por ejemplo, si se quiere manejar específicamente el error de división por cero, se podría hacer:

```py
try:
x = 1 / 0
except ZeroDivisionError:
print("¡No se puede dividir por cero!")
```

## Múltiples bloques except

Un solo bloque try puede tener varios bloques except para manejar diferentes tipos de excepciones. Python verifica los bloques except de arriba a abajo hasta que encuentra una coincidencia. Una vez que se maneja una excepción, el control pasa al código que sigue al bloque try/except.

```py
try:
x = 1 / 0
except ZeroDivisionError:
print("¡No se puede dividir por cero!")
except:
print("Ocurrió otro tipo de excepción")
```

## Uso avanzado de las excepciones

### Bloque else

El bloque else en Python se puede utilizar junto con la instrucción try/except. El código dentro del bloque else se ejecutará siempre y cuando no se produzca ninguna excepción en el bloque try.

```py
try:
x = 1 / 2
except ZeroDivisionError:
print("¡No se puede dividir por cero!")
else:
print("Todo salió bien")
```

### Bloque finally

El bloque finally se utiliza para especificar acciones que deben realizarse bajo todas las circunstancias, ya sea que se produzca una excepción o no.

```py
try:
x = 1 / 0
except ZeroDivisionError:
print("¡No se puede dividir por cero!")
finally:
print("Esto se ejecuta sin importar qué")
```

### Lanzar excepciones

Puede lanzarse una excepción deliberadamente utilizando la palabra clave raise.

```py
x = 10
if x > 5:
raise Exception('x no debería exceder 5. El valor de x es: {}'.format(x))
```

Las excepciones son una parte fundamental de la programación en Python y un buen manejo de las mismas es crucial para escribir programas robustos y mantenibles. Las excepciones ofrecen una forma de indicar que ha sucedido un problema, y luego permitir que el código que invocó el código problemático decida cómo manejar la situación.
