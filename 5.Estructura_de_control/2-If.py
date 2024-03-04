edad = 70
if edad > 17:
    print('puede ver la pelicula')
else:
    print('No puedes entrar')
print('listo')

# NOTA-. es importante que se respete el espacio el codigo dentro del if, no debe estar al mismo nivel


# las evaluaciones se hacen de arriba hacia abajo

# el orden en el que se escribe las condiciones son importantes
if edad > 65:
    print('Puedes ver la pelicula con super desceunto')
elif edad > 54:
    print('puedes ver la pelicula con descuento')

elif edad > 17:
    print('puedes ver la pelicula')
# else:
#     print('ve a otro lado')
