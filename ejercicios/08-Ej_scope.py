'''Explorar el concepto de scope de variables en Python a través de un sistema de registro de puntos en un juego.

El programa simulará un sistema de registro de puntos para jugadores en un juego. Este escenario permitirá entender la diferencia entre variables globales, locales a una función, y locales a una subfunción, y cómo cada una puede ser accedida y modificada.'''

# Definición de la variable global
puntos_globales = 0
 
# Definición de la función de registro de puntos
def registro_puntos(puntos_de_partida):
    # Variable local a la función
    puntos_partida = puntos_de_partida
    
    # Definición de la subfunción para aplicar bonus
    def bonus_puntos(bonus):
        # Para modificar la variable local de la función contenedora, se usa nonlocal
        nonlocal puntos_partida
        puntos_partida += bonus
        print(f"Bonus aplicado: {bonus}. Puntos de partida después del bonus: {puntos_partida}")
    
    # Aplicar un bonus de 10 puntos
    bonus_puntos(10)
    
    # Modificar la variable global dentro de la función
    global puntos_globales
    puntos_globales += puntos_partida
    print(f"Puntos de partida: {puntos_partida}, Puntos globales después de la partida: {puntos_globales}")
 
# Llamada a la función para simular el registro de puntos
registro_puntos(100)
 
# Imprimir el estado final de las variables
print(f"Estado final - Puntos globales: {puntos_globales}")