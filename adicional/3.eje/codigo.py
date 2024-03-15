# Esta versiÃ³n utiliza archivos para almacenar y leer los datos de cada usuario de nuestra red social.

# AdemÃ¡s encapsula el proceso de lectura y escritura de archivos en el mÃ³dulo Red, de manera de hacer
# que el cÃ³digo sea mÃ¡s fÃ¡cil de comprender.

# Recordemos que en este mÃ³dulo estÃ¡n todos las funciones adicionales que hemos creado.
import funciones as Red

Red.mostrar_bienvenida()
nombre = Red.obtener_nombre()
print("Hola ", nombre, ", bienvenido a Mi Red")

# Verificamos si el archivo existe
if Red.existe_archivo(nombre+".user"):
    # Esto lo hacemos si ya habÃ­a un usuario con ese nombre
    print("Leyendo datos de usuario", nombre, "desde archivo.")
    (nombre, edad, estatura_m, estatura_cm, sexo, pais,
     num_amigos, estado) = Red.leer_usuario(nombre)

else:
    # En caso que el usuario no exista, consultamos por sus datos tal como lo hacÃ­amos antes
    print()
    edad = Red.obtener_edad()
    (estatura_m, estatura_cm) = Red.obtener_estatura()
    sexo = Red.obtener_sexo()
    pais = Red.obtener_pais()
    num_amigos = Red.obtener_num_amigos()
    estado = ""

# En ambos casos, al llegar aquÃ­ ya conocemos los datos del usuario
print("Muy bien. Estos son los datos de tu perfil.")
Red.mostrar_perfil(nombre, edad, estatura_m,
                   estatura_cm, sexo, pais, num_amigos)
Red.mostrar_mensaje(nombre, None, estado)

# Ahora podemos mostrar el menu y consultar las opciones
opcion = 1
while opcion != 0:
    opcion = Red.opcion_menu()
    if opcion == 1:
        estado = Red.obtener_mensaje()
        Red.mostrar_mensaje(nombre, None, estado)

    elif opcion == 2:
        estado = Red.obtener_mensaje()
        for i in range(num_amigos):
            nombre_amigo = input("Ingresa el nombre de tu amigo o amiga: ")
            Red.mostrar_mensaje(nombre, nombre_amigo, estado)

    elif opcion == 3:
        Red.mostrar_perfil(nombre, edad, estatura_m,
                           estatura_cm, sexo, pais, num_amigos)

    elif opcion == 4:
        edad = Red.obtener_edad()
        (estatura_m, estatura_cm) = Red.obtener_estatura()
        sexo = Red.obtener_sexo()
        pais = Red.obtener_pais()
        num_amigos = Red.obtener_num_amigos()
        Red.mostrar_perfil(nombre, edad, estatura_m,
                           estatura_cm, sexo, pais, num_amigos)
    elif opcion == 5:
        nuevo_nombre = input("¿A qué perfil quieres cambiar?")
        datos_usuario = Red.cambiar_usuario(nuevo_nombre)
        if datos_usuario is not None:
            (nombre, edad, estatura_m, estatura_cm, sexo,
             pais, num_amigos, estado) = datos_usuario
            Red.mostrar_perfil(nombre, edad, estatura_m,
                               estatura_cm, sexo, pais, num_amigos)

    elif opcion == 0:
        print("Has decidido salir. Guardando perfil en ", nombre+".user")
        Red.escribir_usuario(nombre, edad, estatura_m,
                             estatura_cm, sexo, pais, num_amigos, estado)
        print("Archivo", nombre+".user", "guardado")

print("Gracias por usar Mi Red. Â¡Hasta pronto!")
