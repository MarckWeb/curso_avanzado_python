
print("Bienvenido a ... ")
print("""

.-..-.       _ .---.          .-.
: :: :      :_;: .; :         : :
: :: :,-.,-..-.:   .' .--.  .-' :
: :; :: ,. :: :: :.`.' '_.'' .; :
`.__.':_;:_;:_;:_;:_;`.__.'`.__.'
                                                            
""")

# Solicitamos al usuario que ingrese su nombre,
# y lo guardamos en una variable de tipo str
nombre = input("Para empezar, dime como te llamas. ")
print()
print("Hola ", nombre, ", bienvenido a unired")
print()

# Solicitamos el ingreso del año, y utilizamos este
# dato para estimar la edad de la persona. ¿Por que decimos que solo estamos "estimando" su edad?
anio = int(input("Para preparar tu perfil, dime en qe año naciste. "))
edad = 2024-anio
print()

# Solicitamos la estatura, medida en metros.
# Utilizamos la conversiÃ³n a 'int', y una expresiÃ³n para convertir esto
# a una medida en metros y centÃ­metros
estatura = float(input(
    "Cuentame mas de ti, para agregarlo a tu perfil. ¿Cuanto mides? Dimelo en metros. "))
estatura_m = int(estatura)
estatura_cm = int((estatura - estatura_m)*100)

# Consultamos cuantos amigos tiene el usuario.
num_amigos = int(
    input("Muy bien. Finalmente, cuèntame cuantos amigos tienes. "))

# Consultamos por el genero

genero = ''

respuest = int(input(
    'Cual es tu genero. \n 1- Masculino \n 2- Femenino. \n Selecciona la opcion: '))
if respuest == 1:
    genero == 'Masculino'
elif respuest == 2:
    genero == 'Femenino'
else:
    print('escoge solo entre uno y dos')

# Consultamos por el telefono
num_telefono = (input(
    'Introduce tu numero de telefonon para que podamos conectarte con amigos. '))

# Consultamos por la direccion
direccion = input('Indica el pais, ciudad, y direccion donde vives. ')


# Con los datos recolectados escribimos en pantalla un texto que resuma los datos que hemos obtenido
print()
print("Muy bien,", nombre, ". Entonces podemos crear un perfil con estos datos.")
print("--------------------------------------------------")
print("Nombre:  ", nombre)
print("Edad:    ", edad, "años")
print("Estatura:", estatura_m, "metros y", estatura_cm, "centimetros")
print("Amigos:  ", num_amigos)
print("Genero:  ", genero)
print("Telefono:  ", num_telefono)
print("Ciudad:  ", direccion)
print("--------------------------------------------------")
print("Gracias por la informaciòn. Esperamos que disfrutes con unired")
print()

# Finalmente, solicitamos un mensaje de prueba que sirva para publicar un estado del usuario.
# mensaje = input(
#     "Ahora vamos a publicar tu primer mensaje. ¿Que estas pensando hoy? ")
# print()
# print("--------------------------------------------------")
# print(nombre, "dice:", mensaje)
# print("--------------------------------------------------")

# MENU
print('Elige uan de las opciones en nuestro menu')
print("1-. Deseo modificar mi nombre de perfil")
print("2-. Deseo escribir un mensaje")

menu = int(input("Agreaga el numero de la opcion seleccioanda: "))

if menu == 1:
    nombre = input("Ingresa el nuevo nombre de tu perfil ")
    print('Tu nuevo nombre de perfil es: ', nombre)
elif menu == 2:
    continuar = True
    # Este ciclo se mantiene en ejecuciòn hasta que el usuario desee salir
    while continuar:

        # Solicitamos opciòn al usuario
        escribir_mensaje = str(input("Â¿Deseas escribir un mensaje? (S/N) "))

    # Vamos a aceptar que el usuario ingrese un mensaje cuando escriban "S", "s", o nada
        if escribir_mensaje == "N" or escribir_mensaje == "n":
            continuar = False
    # En caso que sea otra respuesta, vamos a decidir salir.
    # Asi­, en la siguiente iteración el ciclo terminará¡
        else:
            mensaje = input("Vamos a publicar un mensaje. ¿Qué piensas hoy? ")
            print()
            print("--------------------------------------------------")
            print(nombre, "dice:", mensaje)
            print("--------------------------------------------------")

# Mensaje de salida, una vez que el ciclo ha terminado.
    print("Gracias por usar UniRed. ¡Hasta pronto!")
