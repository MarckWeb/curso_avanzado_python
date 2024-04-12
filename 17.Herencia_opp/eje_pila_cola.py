'''
   Crear una clase pila LIFO (Last In, First Out)
   motodo push, pop, size
'''


class Pila:
    def __init__(self):
        self.items = []

    def push(self, item):
        """Añade un elemento al tope de la pila."""
        self.items.append(item)

    def pop(self):
        """Elimina y devuelve el elemento del tope de la pila."""
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("La pila está vacía")

    def size(self):
        """Devuelve el número de elementos en la pila."""
        return len(self.items)

    def is_empty(self):
        """Devuelve True si la pila está vacía, False en caso contrario."""
        return len(self.items) == 0


# Crear una instancia de la clase Pila
mi_pila = Pila()

# Añadir elementos a la pila
mi_pila.push(1)
mi_pila.push(2)
mi_pila.push(3)

# Mostrar el contenido de la pila
print("Contenido de la pila después de añadir elementos:", mi_pila.items)

# Tamaño de la pila
print("Tamaño de la pila:", mi_pila.size())

# Eliminar elemento del tope de la pila
elemento_eliminado = mi_pila.pop()
print("Elemento eliminado de la pila:", elemento_eliminado)

# Mostrar el contenido de la pila después de eliminar un elemento
print("Contenido de la pila después de eliminar un elemento:", mi_pila.items)


'''
   Crear una clase cola FIFO (First In, First Out)
   motodo push, pop, size
'''


class Cola:
    def __init__(self):
        self.items = []

    def push(self, item):
        """Añade un elemento al final de la cola."""
        self.items.append(item)

    def pop(self):
        """Elimina y devuelve el elemento del frente de la cola."""
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("La cola está vacía")

    def size(self):
        """Devuelve el número de elementos en la cola."""
        return len(self.items)

    def is_empty(self):
        """Devuelve True si la cola está vacía, False en caso contrario."""
        return len(self.items) == 0


# Crear una instancia de la clase Cola
mi_cola = Cola()

# Añadir elementos a la cola
mi_cola.push('a')
mi_cola.push('b')
mi_cola.push('c')

# Mostrar el contenido de la cola
print("Contenido de la cola después de añadir elementos:", mi_cola.items)

# Tamaño de la cola
print("Tamaño de la cola:", mi_cola.size())

# Eliminar elemento del frente de la cola
elemento_eliminado_cola = mi_cola.pop()
print("Elemento eliminado de la cola:", elemento_eliminado_cola)

# Mostrar el contenido de la cola después de eliminar un elemento
print("Contenido de la cola después de eliminar un elemento:", mi_cola.items)
