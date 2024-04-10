class Persona:
    # Constructor por defecto
    '''def __init__(self):
        pass'''
    # en python solo se permite un constructor por clase
    def __init__(self, nombre= '', edad=0):
        #print('En el constructor recibimos', nombre, edad)
    # crear las propiedades de la clase
        self.nombre = nombre
        self.edad = edad

    # Metodos: Son funciones declaradas dentro de la clase
    # se invoca a travez de objeto
    def mostrarInfo(self): # si no pongo el argumento self, no lo reconoce como metodo de la clase Persona
        print('Nombre', self.nombre, 'Edad:', self.edad)
        print('Hola me llamo {} y tengo {}'.format(self.nombre, self.edad))
        print(f"Hola me llamo {self.nombre} y tengo {self.edad} años")

      # Error por que solo verifica que nombre y edad estan en la funcion mostrarInfo
      #  print('Nombre', nombre, 'Edad:', edad)
    def nombre_mayusculas(self):
        return  self.nombre.upper()

# crear objetos o instancia de persona
p1 = Persona() # Invoco al constructor pro defecto
p2 = Persona('Juan', 37)
print(p2)
p3 = Persona('Pepito')
print(p3)
p4 = Persona(edad=29)
print(p4)

# Invocar al metodo mostrarinfo()
p2.mostrarInfo()
print(p2.nombre)
print(p2.edad)

# Invovcar al metodo nombre_ayuculas()
print(p3.nombre_mayusculas())

# tengo acceso a las propiedades, son publicas
p2.nombre = 'Nuevo Juan'
print('Nuevo nombre de Juan ...', p2.nombre)
p2.mostrarInfo()