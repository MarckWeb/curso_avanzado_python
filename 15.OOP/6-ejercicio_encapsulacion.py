'''
Ejercicio: Sistema de Gestión de Cuentas Bancarias
Crea una clase CuentaBancaria que tenga los siguientes atributos y métodos:

Atributos:

 - titular: el nombre del titular de la cuenta (debe ser privado).
 - saldo: el saldo de la cuenta (debe ser privado).

Métodos:

    1-. __init__(self, titular, saldo_inicial): constructor que recibe el nombre del titular y el saldo inicial.
    2-.depositar(self, cantidad): añade una cantidad al saldo de la cuenta.
    3-.retirar(self, cantidad): retira una cantidad del saldo de la cuenta. No debe ser posible retirar
    más dinero del que hay en la cuenta.
    4-.consultar_saldo(self): devuelve el saldo actual de la cuenta.
Implementa la clase CuentaBancaria con los atributos y métodos especificados, asegurándote de usar
encapsulación para los atributos privados.
'''

class CuentaBancaria:
    def __init__(self, titular, saldo_inicial):
        # Inicializar atributos privados
        pass

    def depositar(self, cantidad):
        # Añadir cantidad al saldo
        pass

    def retirar(self, cantidad):
        # Retirar cantidad del saldo si es posible
        pass

    def consultar_saldo(self):
        # Devolver saldo actual
        pass


# Prueba de la clase CuentaBancaria
cuenta = CuentaBancaria("Juan Pérez", 1000)

print("Saldo inicial:", cuenta.consultar_saldo())

cuenta.depositar(500)
print("Saldo después de depositar 500:", cuenta.consultar_saldo())

cuenta.retirar(200)
print("Saldo después de retirar 200:", cuenta.consultar_saldo())

cuenta.retirar(1500)  # Esto no debe ser posible
print("Saldo después de intentar retirar 1500:", cuenta.consultar_saldo())