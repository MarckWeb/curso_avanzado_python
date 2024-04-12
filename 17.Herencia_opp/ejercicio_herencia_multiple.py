'''
    clase Animal  nombre y edad

    clase ProductoVenta codigo y precio

    clase Perro que hereda de Animal y ProductoVenta
        atributos: vacunado, sexo
'''

class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}"

class ProductoVenta:
    def __init__(self, codigo, precio):
        self.codigo = codigo
        self.precio = precio

    def __str__(self):
        return f" Codigo: {self.codigo}, precio: {self.precio}"

class Perro(Animal, ProductoVenta):
    def __init__(self, nombre, edad, codigo, precio, vacunado, sexo):
        # con herencia multiple no puedo llamar al constructor con super()
        # hay que poner el nombre de la clase y ademas pasar el puntero self
        Animal.__init__(self, nombre, edad)
        ProductoVenta.__init__(self, codigo, precio)
        self.vacunado = vacunado
        self.sexo = sexo

    def __str__(self):
        # Lo mismo, para invocar al metodo de la superclase tambien con el nombre y self
        return Animal.__str__(self) + ProductoVenta.__str__(self) + f" Vacunado: {self.vacunado}, Sexo: {self.sexo}"

# Crear perro
perro = Perro("Pulguitas", 1, "PE-001", 295.90, True, "M")
print(perro)

print("Codigo:", perro.codigo)
print("Precio:", perro.precio)