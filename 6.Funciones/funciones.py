# Dada la siguiente función en Python, ¿qué imprimirá?

def mi_funcion(a, b):
    return a ** b


print(mi_funcion(3, 2))  # 9


# función para que devuelva el triple de un número.

def triple(numero):
    return numero * 3


print(triple(2))  # 6


# definir un valor predeterminado 1 para el argumento incremento de la función

def incrementar(numero, incremento=1):
    return numero + incremento


print(incrementar(3))  # 4

# la función debe devolver el resultado de la suma.


def suma(a, b):
    resultado = a + b
    return resultado


print(suma(10, 20))
