# Recordemos que en este mÃ³dulo estÃ¡n todos las funciones adicionales que hemos creado.
import s5Red as Red
# El mÃ³dulo 'os' nos permitirÃ¡ consultar si un archivo existe.
import os

Red.mostrar_bienvenida()
nombre = Red.obtener_nombre()
print("Hola ", nombre, ", bienvenido a Mi Red")

# Verificamos si el archivo existe
if os.path.isfile(nombre+".user"):
    # Esto lo hacemos si ya habÃ­a un usuario con ese nombre
    print("Leyendo datos de usuario", nombre, "desde archivo.")
    archivo_usuario = open(nombre+".user", "r")
    nombre = archivo_usuario.readline()
    edad = int(archivo_usuario.readline().strip())
    estatura = float(archivo_usuario.readline())
    estatura_m = int(estatura)
    estatura_cm = int((estatura - estatura_m)*100)
    sexo = archivo_usuario.readline()
    pais = archivo_usuario.readline()
    num_amigos = int(archivo_usuario.readline())
    estado = archivo_usuario.readline()
    # Una vez que hemos leido los datos del usuario no debemos olvidar cerrar el archivo
    archivo_usuario.close()

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
    elif opcion == 0:
        print("Has decidido salir. Guardando perfil en ", nombre+".user")
        archivo_usuario = open(nombre+".user", "w")
        # sino se coloca el saldo de letra se guarda los datso de manera corrido y no pro linea.  esto para leer con writeline
        archivo_usuario.write(nombre+"\n")
        archivo_usuario.write(str(edad)+"\n")
        archivo_usuario.write(str(estatura_m + estatura_cm/100)+"\n")
        archivo_usuario.write(sexo+"\n")
        archivo_usuario.write(pais+"\n")
        archivo_usuario.write(str(num_amigos)+"\n")
        archivo_usuario.write(estado+"\n")
        # Una vez que hemos escrito todos los datos del usuario en el archivo, no debemos olvidar cerrarlo
        archivo_usuario.close()
        print("Archivo", nombre+".user", "guardado")


print("Gracias por usar Mi Red. Â¡Hasta pronto!")

# EJERCICIO 1

# Al leer las líneas del archivo, siempre se leen como últimos caracteres algunos caracteres blancos, como espacios o el caracter cambio de línea ('\n'). Esto hace que los nombres de archivos creados incluyan estos caracteres adicionales. Utiliza los métodos de 'str' para elminar este tipo de caracteres que denominamos "no imprimibles". Es decir, "limpia" toda línea que leas, de manera que no tengan caracteres adicionales a lo esperado (ya sean saltos de línea y/o espacios en blanco).

# EJERCICIO 2

# Utiliza tu conocimiento de funciones para crear funciones que lean desde un archivo, y retornen el conjunto de datos leídos, de manera de encapsular el proceso de lectura y escritura, y reducir el tamaño de tu código.
