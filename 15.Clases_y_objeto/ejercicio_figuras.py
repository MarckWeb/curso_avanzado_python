'''
    Crear una clase Figura con atributos: x,y
    metodo calcular_area
    metodo  ->  [x,y]

    Crear la clase Circulo, Triangulo, Cuadrado
    calcular el area
    veamos la informacion de la figura por pantalla
'''

class Figura:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def calcular_area(self):
        raise NotImplementedError("Please Implement this method")

    def __str__(self):
        return f"[{self.x},{self.y}]"   # [20, 6]

import math
class Circulo(Figura):
    def __init__(self, x, y, radio):
        # Tambien puedo invocar con el nombre de la clase
        Figura.__init__(self,x, y)
        #super().__init__(x,y)
        self.radio = radio

    def calcular_area(self):
        return math.pi *  math.pow(self.radio, 2)

    def __str__(self):
        return super().__str__() + f", Radio: {self.radio}"

class Triangulo(Figura):
    def __init__(self, x, y, base, altura):
        super().__init__(x, y)
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura / 2

    def __str__(self):
        return super().__str__() + f", Base: {self.base}, Altura: {self.altura}"

class Cuadrado(Figura):
    def __init__(self, x, y, lado):
        super().__init__(x, y)
        self.lado = lado

    def calcular_area(self):
        return self.lado ** 2

    def __str__(self):
        return super().__str__() + f", Lado: {self.lado}"

''' Crear objetos y devolver el area y sus datos '''
figura = Figura(20,6)
print("Area de la figura:",figura.calcular_area())  # None
print(figura)

circulo = Circulo(20,6, 50)
print("Area del circulo:", round(circulo.calcular_area(), 2) )
print(circulo)

triangulo = Triangulo(20,6, 40, 25)
print("Area del triangulo:", round(triangulo.calcular_area(), 2) )
print(triangulo)

cuadrado = Cuadrado(20,6, 12)
print("Area del cuadrado:", cuadrado.calcular_area())
print(cuadrado)