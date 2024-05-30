'''
abs(): Devuelve el valor absoluto de un número. Puede ser un entero, un número de punto flotante o un objeto que implemente __abs__()
'''
numero = -5
valor_absoluto = abs(numero)
print(f"El valor absoluto de {numero} es {valor_absoluto}")

'''
bin(): Convierte un número entero a una cadena binaria con el prefijo "0b"
'''
decimal = 10
binario = bin(decimal)
print(f"El número {decimal} en binario es {binario}")

'''
len(): Devuelve la longitud (cantidad de elementos) de un objeto iterable, como una lista o una cadena
'''
cadena = "Hola, mundo"
longitud = len(cadena)
print(f"La longitud de la cadena es {longitud}")

'''
max() y min(): Encuentra el valor máximo y mínimo en una secuencia de números
'''
numeros = [5, 10, 3, 8, 1]
maximo = max(numeros)
minimo = min(numeros)
print(f"El máximo es {maximo} y el mínimo es {minimo}")

'''
sum(): Calcula la suma de los elementos en una lista o tupla
'''
numeros = [1, 2, 3, 4, 5]
suma_total = sum(numeros)
print(f"La suma de los números es {suma_total}")

