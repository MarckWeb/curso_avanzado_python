'''operaciones segun la prioridad de los signos'''
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
