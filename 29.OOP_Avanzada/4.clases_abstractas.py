import abc
import math


class Figura(abc.ABC):
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Marcar el metodo como abstracto
    @abc.abstractmethod
    def calcular_area(self):
        pass

    def __str__(self):
        return f"[{self.x},{self.y}]"


# @Figura.register
class Circulo(Figura):
    def __init__(self, x, y, radio):
        Figura.__init__(self, x, y)
        self.radio = radio

     # Sobre escribimos el metodo abstracto heredado
    def calcular_area(self):
        return math.pi * math.pow(self.radio, 2)

    def __str__(self):
        return super().__str__() + f", Radio: {self.radio}"


class Triangulo(Figura):
    def __init__(self, x, y, base, altura):
        super().__init__(x, y)
        self.base = base
        self.altura = altura

# No sobre escribo el metodo abstracto heredado
   #  def calcular_area(self):
   #      return self.base * self.altura / 2

    def __str__(self):
        return super().__str__() + f", Base: {self.base}, Altura: {self.altura}"


'''
class Cuadrado(Figura):
    def __init__(self, x, y, lado):
        super().__init__(x, y)
        self.lado = lado

    def calcular_area(self):
        return self.lado ** 2

    def __str__(self):
        return super().__str__() + f", Lado: {self.lado}"'''


''' 
Una clase que tiene un metodo abstracto, es una clase abstracta o inacabada, por lo tanto, nno puedo crear un objeto de una clase inacabada 
'''
# TypeError: Can't instantiate abstract class Figura without an implementation for abstract method 'calcular_area'
'''figura = Figura(20, 6)
print("Area de la figura:", figura.calcular_area())  # None
print(figura)'''

circulo = Circulo(20, 6, 50)
print("Area del circulo:", round(circulo.calcular_area(), 2))
print(circulo)

triangulo = Triangulo(20, 6, 40, 25)
print("Area del triangulo:", round(triangulo.calcular_area(), 2))
print(triangulo)
'''
cuadrado = Cuadrado(20, 6, 12)
print("Area del cuadrado:", cuadrado.calcular_area())
print(cuadrado)
'''
