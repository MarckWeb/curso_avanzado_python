# condicional mas simple
# si se cumple la condicion :
#   se ejecuta este bloque
hora = 10
if hora == 15 :
    print("La clase ha terminado")
    


# condicional con alternativa
# si se cumple la condicion :
#   se ejecuta este bloque
# si no se cumple :
#   se ejecuta este otro bloque
if hora == 15 :
    print("La clase ha terminado")
else :
    print("Lo siento, todavia estamos en clase")
    

# condicional anidado
# si se cumple la condicion :
#   se ejecuta este bloque
# si no se cumple probamos otra condicion y si se cumple :
#   se ejecuta este otro bloque
# si no se cumple ninguna de las anteriores :
#   se ejecuta el ultimo bloque
n1 = 20
n2 = 20
if n1 > n2 :
    print("el numero", n1, "es el mayor")
elif n2 > n1 :
    print("el numero", n2, "es el mayor")
else :
    print("los numeros", n1, "y", n2, "son iguales")