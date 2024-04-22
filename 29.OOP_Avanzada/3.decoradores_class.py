# Ejemplo de decorador con clase
class MiDecorador:
    def __init__(self, funcion):
        self.funcion = funcion
        print(self)  # <__main__.MiDecorador object at 0x000001C6C58E0590>

# call es el metodo que se ejecuta cuando llamamos a la funcion contar
    def __call__(self, *argumentos):  # argumentos pasados a la funcion
        print("Hemos recibido:", argumentos)
        self.funcion(*argumentos)  # ejecuta la funcion que recibe


@MiDecorador
def contar(*numeros):
    print("Numeros de datos:", len(numeros))


contar()
contar(1)
contar(1, 7)
contar(1, 7, 5, 2, 8, 6)
print(type(contar))  # <class '__main__.MiDecorador'>
