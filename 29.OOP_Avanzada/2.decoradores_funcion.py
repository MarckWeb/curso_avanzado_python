# @Decoradores

def info(funcion):
    print("Nombre:", funcion.__name__)  # Nombre: mi_funcion
    print('Tipo:', type(funcion))  # Tipo: <class 'function'>
    return funcion


# Normalmente los decoradores deben estar encima de las funciones que serviran como paramtero
@info
def mi_funcion():
    print('Estoy ejecutando mi funcion')


mi_funcion()


'''
Ejemplo de decoradores con argumentos
'''


def operacion(operador):
    def otra_funcion(funcion):
        print('La operacion es:', operador)
        return funcion
    return otra_funcion


@operacion('+')
def sumar(n1, n2):
    print("suma", n1 + n2)


@operacion('-')
def restar(n1, n2):
    print("resta", n1 - n2)


@operacion('*')
def multiplicar(n1, n2):
    print("multiplica", n1 * n2)


@operacion('//')
def dividir(n1, n2):
    print("dividi", n1 // n2)


sumar(7, 5)
restar(7, 5)
multiplicar(7, 5)
dividir(7, 5)
