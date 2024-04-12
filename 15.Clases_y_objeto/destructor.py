# Ejemplo de destructor
# No es obligatorio
class Pelicula:
    # Constructor de la clase (al crear lainstancia)
    def __init__(self, titulo, duracion, lanzamiento):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento
        print('Se ha creadolapelicula', self.titulo)

    # Destructor de la clase (al borrar la instancia)
    def __del__(self):
        print('Se ha borrado la pelicula', self.titulo)

    def __str__(self):
        return f'{self.duracion}, {self.lanzamiento}, {self.titulo}'


p = Pelicula('Avatar 2', 140, 2023)
print(p)

# Otra forma de eliminar atributos
delattr(p, 'lanzamiento')
print(p.__dict__)  # {'titulo': 'Avatar 2', 'duracion': 140}

# eliminar un atributo del objeto
del p.titulo
# {'titulo': 'Avatar 2', 'duracion': 140, 'lanzamiento': 2023}
print('->>', p.__dict__)  # {'duracion': 140}


# Eliminar el objeto entero
print('llamando al objeto "p"', p)
del p
# print(p.__dict__)  # NameError: name 'p' is not defined
