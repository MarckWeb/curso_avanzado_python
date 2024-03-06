# Operadores

Los operadores en Python son símbolos especiales que realizan operaciones aritméticas o lógicas. Python es rico en operadores y proporciona los siguientes tipos de operadores:

1. Operadores aritméticos
2. Operadores de comparación (relacionales)
3. Operadores de asignación
4. Operadores lógicos
5. Operadores de bit a bit
6. Operadores de identidad
7. Operadores de pertenencia

## Operadores aritméticos

Los operadores aritméticos se utilizan para realizar operaciones matemáticas como la suma, la resta, la multiplicación, etc.

```py
a = 10
b = 20

print(a + b) # Suma: 30
print(a - b) # Resta: -10
print(a * b) # Multiplicación: 200
print(a / b) # División: 0.5
print(a % b) # Módulo (resto de la división): 10
print(a \*\* b) # Exponenciación: 10^20
print(a // b) # División entera: 0
```

## Operadores de comparación (relacionales)

Estos operadores comparan los valores en ambos lados y deciden la relación entre ellos. También se conocen como operadores relacionales.

```py
a = 10
b = 20

print(a == b) # Igual a: False
print(a != b) # No igual a: True
print(a > b) # Mayor que: False
print(a < b) # Menor que: True
print(a >= b) # Mayor o igual que: False
print(a <= b) # Menor o igual que: True
```

## Operadores de asignación

Los operadores de asignación se utilizan para asignar valores a las variables.

```py
a = 10 # Asigna 10 a la variable 'a'
a += 10 # Equivalente a 'a = a + 10'
a -= 10 # Equivalente a 'a = a - 10'
a _= 10 # Equivalente a 'a = a _ 10'
a /= 10 # Equivalente a 'a = a / 10'
a %= 10 # Equivalente a 'a = a % 10'
a **= 10 # Equivalente a 'a = a ** 10'
a //= 10 # Equivalente a 'a = a // 10'
```

## Operadores lógicos

Los operadores lógicos se utilizan para combinar declaraciones condicionales.

cuando se usan todos los operadores para realizar condiciones primero se evalua el not luego el and y despues el or

```py
a = True
b = False

// AND: True si todas las condiciones son True
print(a and b) # Logical AND: False
// OR: True si al menos una condición es True
print(a or b) # Logical OR: True
// NOT: Invierte la condición
print(not a) # Logical NOT: False
```

## Operadores de bit a bit

Estos operadores trabajan con bits y realizan operaciones bit a bit. Son: &, |, ^, ~, <<, >>.

```py
a = 60 # 60 = 0011 1100
b = 13 # 13 = 0000 1101

print(a & b) # Bitwise AND: 12 (0000 1100)
print(a | b) # Bitwise OR: 61 (0011 1101)
print(a ^ b) # Bitwise XOR: 49 (0011 0001)
print(~a) # Bitwise NOT: -61 (1100 0011)
print(a << 2) # Left Shift: 240 (1111 0000)
print(a >> 2) # Right Shift: 15 (0000 1111)
```

## Operadores de identidad

Los operadores de identidad comparan las ubicaciones de memoria de dos objetos.

```py
a = 20
b = 20

print(a is b) # 'is' verifica si ambas variables apuntan al mismo objeto: True
print(a is not b) # 'is not' verifica si ambas variables NO apuntan al mismo objeto: False

c = [1, 2, 3]
d = [1, 2, 3]
print(c is d) # False (están en distintas ubicaciones de memoria)
print(c is not d) # True
```

## Operadores de pertenencia

Los operadores de pertenencia se utilizan para probar si una secuencia contiene un ítem.

```py
lista = [1, 2, 3, 4, 5]

print(1 in lista) # 'in' verifica si un elemento está en la secuencia: True
print(6 not in lista) # 'not in' verifica si un elemento NO está en la secuencia: True
```
