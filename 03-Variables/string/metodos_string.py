# Metodos propios de string

animal = '   leOnEs grandeS   .'

# len (longitud)-. retorna el largo del string que pase com
print(len(animal))

# valor original
print(animal)

# upper() -. coloca valores en MAYUSCULA
print(animal.upper())

# lower() -. coloca valores en minuscula
print(animal.lower())

# capitalize() -. coloca en MAYUSCULA solo el primer caracter de la cadena, el resto deja en minuscula
print(animal.capitalize())

# si antes del caracter hay un espacio basio tomara el espacio y no la primera letra
print(animal.strip().capitalize())

# title()-. toma la primera letra de cada palabra que se encuntra dentro de la cadena y los convierte en mayuscula
print(animal.title())

# strip() -. elimina todos los espacion en blanco dentro de la cadena, o dependiento el tipo de caracter que le pasemos
print(animal.strip())
print(animal.strip("."))

# lstrip()-. quita el espacio de la izquierda de la letra
print(animal.lstrip())

# rstrip()-. quita el espacio de la izquierda de la letra
print(animal.rstrip())

# split()-. convierte un string en array, acepta dos parametros ("", 1)
print(animal.split())

# find('gr')-. devuleve el index de su ubicacion del carcater, si se pasa una letra, encuentra el primer caracter y se pasa una letra muestra su index
print(animal.find('gr'))
print(animal.find('r'))
print(animal.find(''))

# nos devuelve -1 por que no se encuentra ese carcater en la cadena
print(animal.find('t'))

# error edebe tener un parametro
# print(animal.find())

# replace()-. reemplaza la cadena o caracter que se pasa en el primer parametro por la palabra del segundo parametro
print(animal.replace('grandeS', 'pequeñoS'))

print(animal.replace('ee', 'pequeñoS'))

# in -.  responde son true o false y existe la palabra o caracter en la cadena

# busca si la cadena si se encuentra
print('grande' in animal)
print('g' in animal)
print('t' in animal)


# not in -. busca si la cadena que no el pasamos no se encuentra en animal
print('t' not in animal)
print('g' not in animal)
print('grande' not in animal)


a = "A"+"B"
print(a)

s = "Acaso hubo buhos aca"
t = s[2:9]+s[0:1]
print(t)

s = input("Ingresa una palabra: ")
resultado = ""
i = 0
while i < len(s):
    resultado = resultado + s[len(s)-i-1]
    i = i+1
print(resultado)
