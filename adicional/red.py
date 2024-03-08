# Hola, para empezar con nuestro proyecto de red social, vamos a utilizar
# las herramientas que conocemos para ejecutar algunas acciones.
#
# Primero, mostraremos un mensaje en pantalla dando la bienvenida al usuario
# y escribiendo el nombre de la red.

# A continuaciÃ³n preguntaremos algunos datos al usuario para poder construir su perfil,
# y guardaremos esta informaciÃ³n en variables.

# Finalmente, escribiremos en pantalla todos los datos que hemos recolectado, y permitiremos
# al usuario escribir un mensaje de estado.

# Te invito a examinar el cÃ³digo, leer los comentarios y comprender los tipos de datos
# que estamos utilizando en cada caso.


# Para conocer un poco mÃ¡s del usuario, vamos a preguntarle algunos datos.
# Por ejemplo, su aÃ±o de nacimiento, y aprovecharemos este dato descubrir la edad del usuario.
# Â¿CÃ³mo lo haremos?, usaremos una variable para guardar el resultado del cÃ¡lculo de
# la edad del usuario. Este es un dato de tipo entero.

# A continuaciÃ³n le preguntaremos al usuario su estatura en metros. Este es un dato de tipo float,
# y usaremos esta informaciÃ³n para calcular los centimetros

# Finalmente escribiremos en pantalla los datos que hemos recordado del usuario usando print y le solicitaremos
# que escriba un mensaje para desplegar en pantalla.

############################################################
# Lo primero que haremos serÃ¡ escribir un mensaje de bienvenida al usuario
# con el nombre de la red. Puedes modificar este mensajes para que represente el nombre de tu propia red
# Considera que al escribir """ tambiÃ©n estamos delimitado un string, pero al hacerlo de esta manera,
# cambios de lÃ­nea que ocurran en el cÃ³digo se considerarÃ¡n como parte del string.
# Si no estÃ¡s convencido, prueba el funcionamiento reemplazando los delimitadores por "

print("Bienvenido a ... ")
print("""

.-..-.       _ .---.          .-.
: :: :      :_;: .; :         : :
: :: :,-.,-..-.:   .' .--.  .-' :
: :; :: ,. :: :: :.`.' '_.'' .; :
`.__.':_;:_;:_;:_;:_;`.__.'`.__.'
                                                            
""")

# Primera interacciÃ³n. Solicitamos al usuario que ingrese su nombre,
# y lo guardamos en una variable de tipo str
nombre = input("Para empezar, dime como te llamas. ")
print()
print("Hola ", nombre, ", bienvenido a unired")
print()

# Segunda interacciÃ³n. Solicitamos el ingreso del aÃ±o, y utilizamos este
# dato para estimar la edad de la persona. Â¿Por quÃ© decimos que solo estamos "estimando" su edad?
# Â¿QuÃ© ocurre si eliminamos la conversiÃ³n a tipo de dato 'int' de la siguiente lÃ­nea?
anio = int(input("Para preparar tu perfil, dime en qe año naciste. "))
edad = 2024-anio
print()

# Tercera interacciÃ³n. Solicitamos la estatura, medida en metros.
# Utilizamos la conversiÃ³n a 'int', y una expresiÃ³n para convertir esto
# a una medida en metros y centÃ­metros
estatura = float(input(
    "Cuentame mas de ti, para agregarlo a tu perfil. ¿Cuanto mides? Dimelo en metros. "))
estatura_m = int(estatura)
estatura_cm = int((estatura - estatura_m)*100)

# Cuarta interacciÃ³n. Consultamos cuÃ¡ntos amigos tiene el usuario.
num_amigos = int(
    input("Muy bien. Finalmente, cuèntame cuantos amigos tienes. "))

# quinta

genero = input(
    'Vamos a ver con que genero te identicas, MASCULINO o FEMENINO. ')

# secta
num_telefono = int(input(
    'Introduce tu numero de telefonon para que podamos conectarte con amigos. '))

# septima
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


# Usaremos una variable bool para indicar si el usuario desea continuar
# utilizando el programa o no


# Ahora puedes escribir mensajes todas las veces que quieras.
# Observa que hemos utilizado un ciclo while que permite repetir la accin de preguntar por un mensajes
# hasta que el usuario escribe algo distino de "S".

# Pero las redes sociales pueden ejecutar mÃ¡s acciones que solamente enviar mensajes.

# Te proponemos los siguientes desafÃ­os:
# 1. Este programa termina cada vez que el valor de 'escribir_mensaje' es distinto a "S" o a "s".
#   Modifique el programa para que el programa termine UNICAMENTE cuando se ingresa "N" o "n".
#   En caso que se ingrese algo distinto, debe volver a solicitar una opciÃ³n al usuario.
#
# 2. Modifica este menÃº para que le permita el usuario realizar mÃ¡s de una acciÃ³n.
#   Por ejemplo, puedes agregar una acciÃ³n que permita al usuario modificar su nombre.
