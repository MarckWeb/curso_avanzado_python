# and, or, not

# AND-. ambas condiciones deben ser verdadero para que el resultado sea verdadero. Si una condicion es falsa la condicion es falso.

carlos = True
# bob = True
bob = False

if carlos and bob:
    print('son personas en and')


# OR-. Al menos una condicion debe ser verdadero para que el resultado evalue en true, Si ambas condiciones son falsa el resultado de estos es falso.

if carlos or bob:
    print('son personas en or')


despejado = False
semaforo_verde = True
velocidad = 10

# primero evalua los parentessis
if not despejado and (semaforo_verde or velocidad > 5):
    print('Puedes avanzar')
