# 📌 OPERADORES ARITMATICOS(+, -, *, /, %, **, //)

# x = int(input('ingresa el primer número: '))
# y = int(input('ingresa el segundo número: '))
x = 7
y = 3

print('Suma', x + y)
print('Resta', x - y)
print("multiplicacon", x * y)
print("Divicion", x / y)
print("Modulo o resto de la divicion", x % y)
print("Potencia", x ** y)
print("Divicion entera", x // y)

# 📌 OPERADORES DE ASIGNACION(+=, -=, *=, /=, %=, **=, //=)
x += 3
print(x)

x += 10  # Equivalente a 'x = x + 10'
x -= 10  # Equivalente a 'x = x - 10'
# a _= 10 # Equivalente a 'x = x _ 10'
x /= 10  # Equivalente a 'x = x / 10'
x %= 10  # Equivalente a 'x = x % 10'
x **= 10  # Equivalente a 'x = x ** 10'
x //= 10  # Equivalente a 'x = x // 10'

# 📌 En python no existe incremnet y decrement
# x ++
# x --
# ++x
# --x


# 📌 OPERADORES RELACIONALES
print('<-OPERADORES RELACIONALES->')

a = 10
b = 20

print(a == b)  # Igual a: False
print(a != b)  # No igual a: True
print(a > b)  # Mayor que: False
print(a < b)  # Menor que: True
print(a >= b)  # Mayor o igual que: False
print(a <= b)  # Menor o igual que: True


# 📌 OPERADORES DE IDENTIDAD (is, is not) -. una manera de comprobar si el objeto es igual a otro
print('OPERADORES DE IDENTIDAD (is, is not)')

frutas1 = ['manzana', 'pera']
frutas2 = ['manzana', 'pera']
frutas3 = frutas1

print(frutas3 is frutas1)  # true por que es una copia
# false por que se guardan en diferentes memorias o con referencias distintas #AAA is #BBB
print(frutas2 is frutas1)

# 📌 OPERADORES DE PERTENENCIA (in, not in) -. si un elemento esta en una determinada coleccion en este caso lista.

print('Luis' in frutas1)
print('Luis' not in frutas1)
print('pera' in frutas1)
print('pera' not in frutas1)
