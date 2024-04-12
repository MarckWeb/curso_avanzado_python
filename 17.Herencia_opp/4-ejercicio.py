'''
Tu tarea es crear una clase base en Python llamada "Animal" y una clase derivada llamada "Dog" (Perro en inglés). La clase base "Animal" debe tener tres atributos: species (especie), age (edad) y weight (peso). La clase "Dog" debe heredar estos atributos y añadir dos más: breed (raza) y name (nombre). Ambas clases deben tener métodos para obtener (getters) y modificar (setters) sus respectivos atributos.
'''

# La clase base debe llamarse "Animal" y debe tener tres atributos:
# species
# age
# weight
# La clase derivada debe llamarse "Dog" y debe heredar los atributos de "Animal" y añadir dos más:
# breed
# name
# Debes crear métodos "getters" y "setters" para cada uno de los atributos en ambas clases.


class Animal:
    def __init__(self, especies, edad, weight):
        self.especies = especies
        self.edad = edad
        self.peso = weight

    def get_especies(self):
        return self.especies

    def set_especies(self, especies):
        self.especies = especies

    def get_edad(self):
        return self.edad

    def set_edad(self, edad):
        self.edad = edad

    def get_peso(self):
        return self.peso

    def set_peso(self, peso):
        self.peso = peso


class Dog(Animal):
    def __init__(self, especies, edad, peso, raza, nombre):
        super().__init__(especies, edad, peso)
        self.raza = raza
        self.nombre = nombre

    def get_raza(self):
        return self.raza

    def set_raza(self, raza):
        self.raza = raza

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre


animal = Animal("Felino", 5, 20)
print(animal.get_especies())  # Debe imprimir "Felino"

dog = Dog("Canino", 3, 10, "Labrador", "Rex")
print(dog.get_nombre())  # Debe imprimir "Rex"
