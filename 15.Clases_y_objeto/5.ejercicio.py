'''
Tu tarea es crear una clase en Python llamada "Book" (Libro en inglés). Esta clase debe tener cuatro atributos: title (título), author (autor), pages (número de páginas) y publisher (editorial). Además, debe tener métodos para obtener (getters) y modificar (setters) estos atributos.
'''
# La clase debe llamarse "Book".
# La clase debe tener cuatro atributos:
#     - title
#     - author
#     - pages
#     - publisher
# Debes crear métodos "getters" y "setters" para cada uno de los atributos.
# Debes crear un método __init__ que inicialice los cuatro atributos.


class Book:
    def __init__(self, title, author, pages, publisher):
        self.title = title
        self.author = author
        self.pages = pages
        self.publisher = publisher

    def get_title(self):
        return self.title

    def set_title(self, title):
        self.title = title

    def get_author(self):
        return self.author

    def set_author(self, author):
        self.author = author

    def get_pages(self):
        return self.pages

    def set_pages(self, pages):
        self.pages = pages

    def get_publisher(self):
        return self.publisher

    def set_publisher(self, publisher):
        self.publisher = publisher


mi_libro = Book("1984", "George Orwell", 328, "Secker & Warburg")
print(mi_libro.get_title())  # Debe imprimir "1984"
print(mi_libro.get_author())  # Debe imprimir "George Orwell"
print(mi_libro.get_pages())   # Debe imprimir 328
print(mi_libro.get_publisher())  # Debe imprimir "Secker & Warburg"

mi_libro.set_title("Animal Farm")
print(mi_libro.get_title())  # Debe imprimir "Animal Farm"
