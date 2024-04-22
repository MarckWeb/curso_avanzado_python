# Pregunta 1
# Escribe un programa para ayudar a una empresa que desea asignar sueldos para los cargos de sus trabajadores. La lista es la siguiente:

# Ejecutivo: 90

# Jefe: 100

# Externo: 50

# La variable cargo contiene el nombre del cargo (por ejemplo, "Externo"). Recuerda entregar tu resultado modificando únicamente la variable dinero

def sueldo(cargo):
    dinero = 0
    if cargo == "Ejecutivo":
        dinero = 90
    elif cargo == "Jefe":
        dinero = 100
    elif cargo == "Externo":
        dinero = 50
    return dinero


# Pregunta 2
# Escribe un código que calcule el cuadrado de un número si este es impar, o el cubo de un número si este es par. Por ejemplo, para 4 tu programa debe entregar 64, y para 3 debe entregar 9.

def exponenciacion(numero):
    resultado = numero
    if resultado % 2 == 0:
        resultado = resultado ** 3
    else:
        resultado = resultado ** 2
    return resultado


print(exponenciacion(3))

# Pregunta 3
# Escriba un programa que verifique si un número es primo o no. Por ejemplo, para los número 3, 5, y 13, la variable primo debe ser True, y para 1, 10, y 33, False.


def es_primo(numero):
    primo = True
    n = 0
    while n < numero:
        if numero % 2 == 0:
            primo = False
        n += 1
    return primo


print(es_primo(1))

hora = 10
if hora == 15:
    print('La clase ha terminado')
else:
    print('Lo siento, todavia estamos en clase')
