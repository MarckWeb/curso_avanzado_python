edad = 15


if edad > 17:
    print('es mayor')
else:
    print('es menor')

# OPERADOR TERNARIO

mensaje = 'Es mayor' if edad > 17 else 'es menor'

print(mensaje)


# ENCADENADO DE OPERADORES DE COMPARACION-.

if edad >= 15 and edad <= 65:
    print('puedes entrar a la pisina')

# forma corta de hacer lo mismo
# Lo que hace es evaluar si la variable edad está en el rango de 15 a 65

if 15 <= edad <= 65:
    print('puedes entrar a la pisina en el metodo corto')

# Python evalúa 15 <= edad, si este resultado es verdadero (es decir, si edad es mayor o igual que 15), entonces continúa evaluando edad <= 65. Si ambos son verdaderos, la expresión completa se evalúa como verdadera y se ejecuta el bloque de código dentro del if.
