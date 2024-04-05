# paramiko
# Scapy
# Scrapy
# Selenium
# BeautifulSoap


# Vamos a modificar el cÃ³digo que acabamos de ver para encapsular algunas partes de Ã©l
# en funciones.

# En particular haremos esto con:
# 1. El mensaje de bienvenida
# 2. El cÃ³digo para solicitar datos al usuario.
# 3. El cÃ³digo para mostrar el perfil del usuario
# 4. El cÃ³digo para mostrar un mensaje en pantalla

def mostrar_bienvenida():
    print("Bienvenido a ... ")
    print("""
                  _                  __
       ____ ___  (_)  ________  ____/ /
      / __ `__ \/ /  / ___/ _ \/ __  /
     / / / / / / /  / /  /  __/ /_/ /
    /_/ /_/ /_/_/  /_/   \___/\__,_/

    """)


def obtener_nombre():
    nombre = input("Para empezar, dime como te llamas. ")
    return nombre


def obtener_edad():
    agno = int(input("Para preparar tu perfil, dime en quÃ© aÃ±o naciste. "))
    return 2017-agno-1


def obtener_estatura():
    estatura = float(input(
        "CuÃ©ntame mÃ¡s de ti, para agregarlo a tu perfil. Â¿CuÃ¡nto mides? DÃ­melo en metros. "))
    metros = int(estatura)
    centimetros = int((estatura - metros)*100)
    return (metros, centimetros)


def obtener_num_amigos():
    amigos = int(
        input("cuÃ©ntame cuantos amigos tienes. "))
    return amigos


def obtener_genero():
    genero = input("cuentame con que genero te identificas. ")
    return genero


def obtener_pais_nacimiento():
    pais_nacimiento = input(
        "Muy bien. Finalmente, cuentame de que pais eres. ")
    return pais_nacimiento


def obtener_datos():
    edad = obtener_edad()
    (est_m, est_c) = obtener_estatura()
    num_amigos = obtener_num_amigos()
    genero = obtener_genero()
    pais_nacimiento = obtener_pais_nacimiento()
    return (edad, est_m, est_c, num_amigos, genero, pais_nacimiento)


def mostrar_perfil(nombre, datos):
    edad, estatura_m, estatura_cm, num_amigos, genero, pais_nacimiento = datos
    print("--------------------------------------------------")
    print("Nombre:   ", nombre)
    print("Edad:     ", edad, "aÃ±os")
    print("Estatura: ", estatura_m, "m y ", estatura_cm, "centÃ­metros")
    print("Amigos:   ", num_amigos)
    print("Genero:   ", genero)
    print("Pais Nac:   ", pais_nacimiento)
    print("--------------------------------------------------")


def opcion_menu():
    print("Acciones disponibles:")
    print("  1. Escribir un mensaje pÃºblico")
    print("  2. Escribir un mensaje solo a algunos amigos")
    print("  3. Mostrar los datos de perfil")
    print("  4. Actualizar el perfil de usuario")
    print("  0. Salir")
    opcion = int(input("Ingresa una opciÃ³n: "))
    while opcion < 0 or opcion > 4:
        print("No conozco la opciÃ³n que has ingresado. IntÃ©ntalo otra vez.")
        opcion = int(input("Ingresa una opciÃ³n: "))
    return opcion


def obtener_mensaje():
    mensaje = input("Ahora vamos a publicar un mensaje. Â¿QuÃ© piensas hoy? ")
    return mensaje


def mostrar_mensaje(origen, destinatario, mensaje):
    print("--------------------------------------------------")
    if destinatario == None:
        print(origen, "dice:", mensaje)
    else:
        print(origen, "dice:", "@"+destinatario, mensaje)
    print("--------------------------------------------------")

############################################################
# El cÃ³digo anterior era solamente definiciÃ³n de funciones que serÃ¡n usadas mÃ¡s adelante
# Ahora empieza el programa principal.


mostrar_bienvenida()
nombre = obtener_nombre()
print()
print("Hola ", nombre, ", bienvenido a Mi Red")
print()
datos = obtener_datos()

print("Muy bien,", nombre, ". Entonces podemos crear un perfil con estos datos.")
mostrar_perfil(datos)
print("Ya podemos preguntar, recordar y calcular datos. Esperamos que disfrutes con Mi Red")
print("--------------------------------------------------")

# Ingresamos al ciclo que permite ejecutar acciones
opcion = 1
while opcion != 0:
    # Mostramos el menu
    opcion = opcion_menu()

    # CÃ³digo para la opciÃ³n 1. Publicar un mensaje.
    if opcion == 1:
        mensaje = obtener_mensaje()
        mostrar_mensaje(nombre, None, mensaje)

    # CÃ³digo para la opciÃ³n 2. Publicar un mensaje a un grupo de personas.
    elif opcion == 2:
        mensaje = obtener_mensaje()
        for i in range(num_amigos):
            nombre_amigo = input("Ingresa el nombre de tu amigo o amiga: ")
            mostrar_mensaje(nombre, nombre_amigo, mensaje)

    # CÃ³digo para la opciÃ³n 3. Publicar los datos del perfil del usuario.
    elif opcion == 3:
        mostrar_perfil(nombre, edad, estatura_m, estatura_cm, num_amigos)

    # CÃ³digo para la opciÃ³n 4. Actualizar los datos del perfil del usuario.
    elif opcion == 4:
        nombre = obtener_nombre()
        edad = obtener_edad()
        (estatura_m, estatura_cm) = obtener_estatura()
        num_amigos = obtener_num_amigos()
        mostrar_perfil(nombre, edad, estatura_m, estatura_cm, num_amigos)
    elif opcion == 0:
        print("Has decidido salir.")

print("Gracias por usar Mi Red. Â¡Hasta pronto!")

# Como puedes ver, una vez que no hay mÃ¡s definiciones de funciones, el programa principal empieza.
# Si lo lees, podrÃ¡s ver que es mucho mÃ¡s corto, y que hay menos cÃ³digo repetido que en la versiÃ³n anterior.

# Te proponemos como desafÃ­o:
# 1. Agrega el atributos como "sexo" y "pais de nacimiento"
#   a los datos que se le piden al usuario, y permite que sean solicitados y leÃ­dos usando funciones.
#   TendrÃ¡s que identificar en quÃ© partes del cÃ³digo debes hacer esa modificaciÃ³n.
