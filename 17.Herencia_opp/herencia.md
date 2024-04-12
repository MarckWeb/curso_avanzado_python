# Herencia

La herencia es un principio fundamental de la programación orientada a objetos. En Python, al igual que en muchos otros lenguajes de programación, la herencia permite que una clase adquiera los atributos y métodos de otra. Esto facilita la reutilización del código y proporciona una estructura lógica y fácil de entender para el código del programa.

## Clases en Python

Antes de hablar de herencia, primero hay que entender las clases en Python. Una clase es esencialmente un plan que define las variables y los métodos (funciones asociadas a una clase) que serán comunes a todos los objetos de esa clase.

Aquí hay un ejemplo de una clase en Python:

```py
class Persona:
   def __init__(self, nombre, edad):
      self.nombre = nombre
      self.edad = edad

   def presentarse(self):
      return f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años."
```

## Herencia simple

La herencia simple en Python se realiza al definir una nueva clase (llamada subclase) que hereda los atributos y métodos de una clase existente (llamada superclase). En el siguiente ejemplo, la clase Estudiante hereda de la clase Persona.

```py
class Estudiante(Persona):
   def __init__(self, nombre, edad, nota):
   super().__init__(nombre, edad)
      self.nota = nota

   def estudiar(self):
        return f"{self.nombre} está estudiando."
```

El método super().a**init**(nombre, edad) en la clase Estudiante invoca el constructor de la superclase Persona, lo que permite que Estudiante herede los atributos nombre y edad de Persona.

## Herencia múltiple

Python también admite herencia múltiple, donde una subclase puede heredar de varias superclases. Para esto, se enumeran las superclases entre paréntesis en la definición de la subclase.

```py
class Mamifero:
   def comer(self):
   print("Puede comer.")

class Alado:
def volar(self):
print("Puede volar.")

class Murcielago(Mamifero, Alado):
pass
```

En este ejemplo, la clase Murcielago puede usar los métodos comer() de la clase Mamifero y volar() de la clase Alado.

En resumen, la herencia es un mecanismo poderoso que facilita la reutilización del código y proporciona una estructura lógica para los programas en Python.
