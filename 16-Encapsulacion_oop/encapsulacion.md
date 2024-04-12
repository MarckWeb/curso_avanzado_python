# Encapsulacion

La encapsulación es un concepto fundamental de la programación orientada a objetos (OOP). En esencia, la encapsulación se refiere a la práctica de esconder los detalles internos de cómo se implementa un objeto, exponiendo solo lo que es seguro y necesario. Esta estrategia ayuda a evitar manipulaciones no deseadas o inesperadas de los datos, proporcionando una forma de controlar el acceso a los atributos y métodos de un objeto.

Aunque Python no tiene encapsulación en el sentido estricto como otros lenguajes de programación como Java o C++, Python ofrece una forma de "simular" la encapsulación utilizando convenciones y métodos especiales. En Python, la encapsulación se logra utilizando dos niveles de acceso a los atributos y métodos: público y privado.

1. **Público**: Todos los atributos y métodos de una clase son públicos por defecto en Python.

2. **Privado**: Los atributos y métodos privados son aquellos que no pueden ser accedidos o alterados directamente desde fuera de la clase.

Se crean al añadir dos guiones bajos \_\_ antes del nombre del atributo o método.

## Atributos privados

Aquí hay un ejemplo de cómo se puede usar la encapsulación en Python:

```py
class Coche:
    def __init__(self):
        self.__marca = "Toyota" # Atributo privado

    # Método para obtener el valor del atributo privado
    def get_marca(self):
        return self.__marca

    # Método para cambiar el valor del atributo privado
    def set_marca(self, marca):
        self.__marca = marca

# Crear una instancia de la clase Coche
mi_coche = Coche()

# Acceso permitido a través de los métodos de la clase
print(mi_coche.get_marca()) # Imprime: Toyota
mi_coche.set_marca("Ford")
print(mi_coche.get_marca()) # Imprime: Ford

# Acceso no permitido directamente al atributo privado
print(mi_coche.__marca) # Lanza un error: AttributeError
```

En el ejemplo, **marca es un atributo privado. No se puede acceder directamente fuera de la clase Coche, como se intenta en la última línea. Esto lanzará un error AttributeError: 'Coche' object has no attribute '**marca'.

Para acceder o modificar el valor de \_\_marca, es necesario utilizar los métodos get_marca() y set_marca(marca) que son públicos. Este control del acceso a los detalles internos de la clase es el núcleo de la encapsulación.

Es importante notar que el "encapsulamiento" en Python es más una convención que una regla estricta. Pythonistas experimentados pueden conocer formas de acceder a estos "atributos privados" a pesar de la convención. Sin embargo, es considerado una mala práctica hacerlo fuera de ciertas situaciones excepcionales.

## Métodos privados

Los métodos privados son una parte importante del concepto de encapsulación en la programación orientada a objetos (OOP). Al igual que los atributos privados, los métodos privados en una clase están destinados a ser utilizados solo dentro de la clase en la que se definen y no deben ser accesibles directamente desde fuera de la clase.

En Python, un método privado se define utilizando un doble guión bajo \_\_ antes del nombre del método. Esta convención indica que el método no debe ser accesado directamente desde fuera de la clase. En su lugar, generalmente se proporcionan métodos públicos para interactuar con los métodos y atributos privados de manera controlada.

Aquí hay un ejemplo de cómo se pueden utilizar los métodos privados en Python:

```py
class Ejemplo:
    def __init__(self):
        self.__dato_privado = 10

    # Método privado
    def __metodo_privado(self):
        return self.__dato_privado * 2

    # Método público que utiliza el método privado
    def metodo_publico(self):
        return self.__metodo_privado()

ejemplo = Ejemplo()

print(ejemplo.metodo_publico()) # Imprime: 20
print(ejemplo.__metodo_privado()) # Lanza un error: AttributeError
```

En el ejemplo anterior, el método **\_\_metodo_privado()** es un método privado.

Intentar llamarlo directamente desde una instancia de la clase Ejemplo, como en la última línea, resultará en un error AttributeError. En lugar de eso, se proporciona un método público, metodo_publico(), que utiliza el método privado de manera segura y controlada.

Aunque los métodos privados pueden parecer restrictivos, en realidad proporcionan una gran cantidad de flexibilidad y control. Permiten a los diseñadores de clases controlar exactamente cómo se utilizan sus clases y ayudan a evitar errores al restringir el acceso a los detalles internos de la implementación de la clase.
