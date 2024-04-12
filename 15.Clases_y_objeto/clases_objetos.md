# Clases y objetos

En Python, casi todo es un objeto, con sus propiedades y métodos. Una clase es como un constructor de objetos, o un "plano" para crear objetos.

## Definición de Clase

Para definir una clase en Python, se utiliza la palabra clave class. El nombre de la clase sigue la convención de que la primera letra debe ser mayúscula.

```py
class MiClase:
    x = 5
```

En el ejemplo anterior, MiClase es una clase simple con un solo atributo x. A los atributos de las clases se les puede acceder utilizando el operador . (punto).

## Objetos

Un objeto es una instancia de una clase. Cuando se define una clase, solo se describe el plano.

Para acceder a las funcionalidades de la clase se debe instanciar la clase, es decir, crear un objeto de la clase.

```py
p1 = MiClase()
print(p1.x) # 5
```

En el ejemplo anterior, p1 es un objeto de MiClase y al acceder al atributo x de p1 se imprime el valor 5.

## La función a**init**a :

La función **init** es una función especial que se llama automáticamente cuando se crea un objeto de una clase. Esta función se usa para asignar valores a las propiedades del objeto o para realizar otras operaciones que son necesarias cuando se crea el objeto.

```py
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

p1 = Persona("Juan", 30)

print(p1.nombre)
print(p1.edad)
```

En el ejemplo anterior, la función **init** se utiliza para asignar nombres y edades a las instancias de la clase Persona.

Cuando se crea un nuevo objeto p1, p1 se convierte en una instancia de Persona con nombre "Juan" y edad 30. self hace referencia a la propia instancia de la clase que se está creando.

## Métodos de objeto

Los métodos de los objetos son funciones que pertenecen a los objetos de la clase. Esto es útil para hacer operaciones con los atributos de los objetos.

```py
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludo(self):
        print("Hola, mi nombre es " + self.nombre)

p1 = Persona("Juan", 30)
p1.saludo() # Hola, mi nombre es Juan
```

En este ejemplo, saludo() es un método que pertenece al objeto p1 de la clase Persona. Este método imprime un mensaje que incluye el nombre del objeto.

## Modificación de propiedades

Pueden modificarse las propiedades de los objetos de la siguiente manera:

```py
p1.edad = 40
```

En este ejemplo, el valor de edad de p1 se cambia a 40.

## Eliminación de propiedades

Pueden eliminarse las propiedades de los objetos utilizando la palabra clave del:

```py
del p1.edad
```

Ahora, p1 ya no tiene la propiedad edad.

## Eliminación de objetos

También pueden eliminarse los objetos utilizando la palabra clave del:

```py
del p1
```

Ahora, p1 ya no existe. Si intenta acceder a p1, Python lanzará una excepción porque ya no existe el objeto p1.

En resumen, las clases en Python proporcionan un medio de empaquetar datos y funcionalidad juntos. Al crear una nueva clase, se crea un nuevo tipo de objeto, lo que permite crear nuevas instancias de ese tipo. Cada instancia de la clase puede tener sus propios atributos. Las instancias de una clase también pueden tener métodos (definidos por su clase) para modificar su estado.
