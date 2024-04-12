'''
Polimorfismo-. ver el objeto de multiples formas
- esto se da cuando la subclase modifica el comportamiento de la superclase
'''


class Animal:

    def onomatopeya(self):
        return f'Sonido de los animales'


class Perro(Animal):
    def onomatopeya(self):
        return 'Ladrar'


class Vaca(Animal):
    def onomatopeya(self):
        return 'Muge'


class Caballo(Animal):
    def onomatopeya(self):
        return 'Relincha'


print(Animal().onomatopeya())
print(Perro().onomatopeya())
print(Vaca().onomatopeya())
print(Caballo().onomatopeya())
