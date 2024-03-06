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
mensaje = input(
    "Ahora vamos a publicar tu primer mensaje. ¿Que estas pensando hoy? ")
print()
print("--------------------------------------------------")
print(nombre, "dice:", mensaje)
print("--------------------------------------------------")

# Ahora puedes practicar solicitando mÃ¡s datos al usuario. Solo tienes que usar apropiadamente input() y print()
# 1. Escribe 3 solicitudes de datos al usuario, por ejemplo sexo, numero de telefono, ciudad donde vive,
#   pais de nacimiento, direccion, etc. Guarda esos datos en variables del tipo, y finalmente escrÃ­belos en pantalla
#   utilizando print. Puedes agregar todas las lÃ­neas que necesites.
