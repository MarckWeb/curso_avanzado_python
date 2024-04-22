# Ejemplo de decorador con clase
class MiDecorador:
    def __init__(self, funcion):
        self.funcion = funcion

    def __call__(self, *argumentos):
        print("Hemos recibido:", argumentos)
        self.funcion(*argumentos)  # ejecuta la funcion que recibe


@MiDecorador
def contar(*numeros):
    print("Numeros de datos:", len(numeros))


contar()
contar(1)
contar(1, 7)
contar(1, 7, 5, 2, 8, 6)
