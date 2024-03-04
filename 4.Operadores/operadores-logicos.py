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


# OPERADOR DE CORTO CIRCUITO-. significa que si la primera condicion es falsa el resto de codigo no se ejecuta en condicion, el cual significa ahorro de computo para el servidor o computador


# para and basta que la primera condicion sea false para que no siga al resto de las condiciones
if not despejado and semaforo_verde and velocidad > 5:
    print('Puedes avanzar en and')


# para OR basta que la primera condicion sea true para que el resultado sea true
if not despejado or semaforo_verde or velocidad > 5:
    print('Puedes avanzar en or')

# todo esto hace que las operaciones en python sean de corto circuito
