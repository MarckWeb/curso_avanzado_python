# declarar funciones

def saludar():  # funcion sin paramero y no retornan ningun resultado
    print('Hola, que tal')


def despedir(nombre):  # fun que recibe el paramtero nombre y retorna un mensaje personalizado
    print(nombre + ', Hasta luego')


# invocar o llamar a una funcion
saludar()  # obligatorio poner los parentesis

"""si no llamo a la funcion sin parentesis, saludar no da error pero no muestra nada porque no lo reconoce como funcion"""

# si intentamos pasar parametros a una funcion que no los tiene declarados
# saludar('11') TypeError: saludar() takes 0 positional arguments but 1 was given

# Cuando invoco a una funcion que retorna un dato, ese dato hay que guardarlo, mostrarlo...
print(despedir('Pepito'))
resultado = despedir('Carlos')
print(resultado)


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
