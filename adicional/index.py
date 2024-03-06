print("Bienvenido a ... ")
print("""

.-..-.       _ .---.          .-.
: :: :      :_;: .; :         : :
: :: :,-.,-..-.:   .' .--.  .-' :
: :; :: ,. :: :: :.`.' '_.'' .; :
`.__.':_;:_;:_;:_;:_;`.__.'`.__.'
                                 
                                 
""")


# http://www.network-science.de/ascii/
# https://www.coursera.org/learn/aprendiendo-programar-python/lecture/i9kQu/2-1-1-que-valores-puedo-usar-tipos-de-datos

"""Fin Módulo 2: Recolección de datos de usuario y publicación de mensajes de estado.

Fin Módulo 3: Integración de un menú que permita efectuar distintas acciones sobre la red.

Fin Módulo 4: Separación del código en módulos que agregan distintas funciones y hacen el código más fácil de entender y modificar.

Fin Módulo 5: Integración de uso de archivos para recordar y almacenar los datos de un usuario.

Fin Módulo 6: Incorporación de listas de amigos y transmisión de mensajes entre ellos."""

"""En Python, los operadores se evalúan siguiendo el orden de precedencia estándar de las operaciones aritméticas:

1-Paréntesis ()
2-Exponentes **
3-Multiplicación *, División /, División entera //, Módulo %
4-Suma +, Resta -
"""
# realizamos la operacion dentro de los parentesis, pero tambien vemos que dentro de los parentesis hay division entera que se realiza la operacion antes de las sumas y restas

operacion = (3+5//4-2)-2**4+3*(7-2)
desglose_parentesis = (3+1-2)-2**4+3*5
desglose_parentesis = 2-2**4+3*5
print(desglose_parentesis)
seguimos_exponente = 2-16+15
print(seguimos_exponente)
opracion_de_izquierda = -14+15
resultado = 1

print(75*75)

tiempo = 1000 * (1/3600)
print(tiempo)
0.2777777777777778

distancia = 0.01


def velocidad(distancia, tiempo):
    resultado = ""
    # desde aquí hacia abajo debes modificar el programa
    # modifica la variable resultado
    # recuerda que los datos están en las variables distancia y tiempo
    resultado = "la velocidad es " + \
        str(distancia / tiempo * 3600)+"km/h o " + \
        str(distancia * 1000 / tiempo)+"m/s"
    return resultado


print(velocidad(100, 1))

# 68/1.83^2 es 20.305174833527424 pero tu programa calculó 68.0.
# Prueba de nuevo!


def xor(a, b):
    xor = False
    # desde aquí hacia abajo debes modificar el programa
    # modifica la variable xor
    # recuerda que los datos están en las variables a y b
    xor = b != a
    return xor


print(xor(True, True))
print(xor(False, True))
print(xor(True, False))
print(xor(False, False))
