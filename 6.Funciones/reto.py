
# Definir una función: Crea una función llamada multiplicar que tome dos números como argumentos y devuelva su producto.

def multiplicar(a, b):
    return a * b

# Llamada a la función: Utiliza la función multiplicar para multiplicar los números 5 y 3, y guarda el resultado en una variable llamada resultado


resultado = multiplicar(5, 3)

# Argumentos y parámetros: Modifica la función multiplicar para que también pueda aceptar un tercer argumento opcional que determina si el resultado debe ser impreso en pantalla.


def multiplicar(a, b, imprimir=False):
    """Este es el docstring de la función"""
    resultado = a * b
    if imprimir:
        print("El resultado es:", resultado)
    return resultado


print(resultado)
# Valores predeterminados: Crea una función llamada saludar que tome un nombre como argumento y tenga un valor predeterminado de "Amigo". La función debe imprimir un saludo.


def saludar(nombre='Amigo'):
    """Este es el docstring de la función"""
    print('hola', nombre)


saludar()

# Retorno de valores: Crea una función llamada es_par que tome un número como argumento y devuelva True si el número es par y False si no lo es.


def es_par(num):
    """Este es el docstring de la función"""
    if num % 2 == 0:
        return True
    else:
        return False


print(es_par(4))
