'''
Crear la clase calculadora con 4 metodos: sumar, restar, multiplicar, dividir
Solicitar 2 nuemros al usuario
  - Llamar a los cuatro metodos
'''

class Calculadora:
    '''def __init__(self, a =5, b=2):
        self.a = a
        self.b = b'''
    # sino pongo constructor, coge el constructor por defecto
    # Calculadora()

    def sumar( self,a, b):
        return a + b

    def restar(self,a, b):
        return a - b

    def multiplicar(self,a, b):
        return a * b

    def dividir(self,a, b):
        resultado = 0
        try:
            resultado = a / b
        except ZeroDivisionError as e:
            print('Error:', e)

a = float(input('Intriduce un numero: '))
b = float(input('Intriduce un numero: '))
resultado = Calculadora()
print(f'{a} + {b} = {resultado.sumar(a, b)}')
print(f'{a} - {b} = {resultado.restar(a, b)}')
print(f'{a} * {b} = {resultado.multiplicar(a, b)}')
print(f'{a} // {b} = {resultado.dividir(a, b)}')