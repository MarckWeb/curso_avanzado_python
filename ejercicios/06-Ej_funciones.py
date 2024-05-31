'''
El objetivo de este ejercicio es implementar el cifrado César utilizando el lenguaje de programación Python.

El cifrado César es un tipo de cifrado por sustitución en el que cada letra en el texto plano es 'desplazada' un cierto número de lugares hacia la derecha o hacia la izquierda en el alfabeto. Por ejemplo, con un desplazamiento de 3, la 'A' se convierte en 'D', la 'B' se convierte en 'E', y así sucesivamente. Este método de cifrado lleva el nombre de Julio César, quien, según se informa, lo usó para comunicarse con sus generales.

Resultado esperado

Proceso de cifrado:

- Texto plano: HOLA MUNDO.

- Texto cifrado: KROD PXQGR.

Proceso de descifrado:

- Texto cifrado: KROD PXQGR.

- Texto descifrado: HOLA MUNDO.

Prueba con texto en minúsculas:

- Todos los caracteres deben estar en mayúsculas y dentro del alfabeto.
'''

alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']



def cifrado_cesar(texto, desplazamiento):
    texto_cifrado = ''
    for letra in texto:
        
        if letra == ' ' or letra == ',' or letra == '.' or letra == ':':
            texto_cifrado += letra
        else:
            letra_sust = (alfabeto.index(letra) + desplazamiento)% len(alfabeto)
            texto_cifrado += alfabeto[letra_sust]
            
    return texto_cifrado


def descifrado_cesar(texto, desplazamiento):
    texto_descifrado = ''

    if texto.islower():
        return "Todos los caracteres deben estar en mayúsculas y dentro del alfabeto."
    
    else:
        for letra in texto:
        
            if letra == ' ' or letra == ',' or letra == '.' or letra == ':':
                texto_descifrado+= letra
            else:
                letra_sust = (alfabeto.index(letra) - desplazamiento)% len(alfabeto)
                texto_descifrado+= alfabeto[letra_sust]
            
        return texto_descifrado
    
texto_a_cifrar = 'hola mundo'

if texto_a_cifrar.islower():
    print ("Todos los caracteres deben estar en mayúsculas y dentro del alfabeto.")
else:
    resultado_texto_cifrado = cifrado_cesar(texto_a_cifrar, 3)
    print('Proceso de cifrado:')
    print(f'Texto plano: {texto_a_cifrar}')
    print(f'Texto cifrado: {resultado_texto_cifrado}')
    if resultado_texto_cifrado.isupper() :
        print('Proceso de descifrado:')
        print(f'Texto cifrado: {resultado_texto_cifrado}')
        print(f'Texto descifrado: {descifrado_cesar(resultado_texto_cifrado, 3)}')

print('''SEGUNDA OPCION''')

def cifrado_cesar_2(texto, desplazamiento):
    texto_cifrado = ""
    for letra in texto:
        if letra in alfabeto:
            # Calculamos el nuevo índice
            indice_nuevo = (alfabeto.index(letra) + desplazamiento) % len(alfabeto)
            # Añadimos la letra correspondiente al resultado
            texto_cifrado += alfabeto[indice_nuevo]
        elif letra in " ,.:":  # Si es un espacio, coma, punto o dos puntos, lo añadimos directamente
            texto_cifrado += letra
        else:  # Si no está en el alfabeto
            return "Todos los caracteres deben estar en mayúsculas y dentro del alfabeto."
    return texto_cifrado
 
def descifrado_cesar_2(texto_cifrado, desplazamiento):
    texto_descifrado = ""
    for letra in texto_cifrado:
        if letra in alfabeto:
            # Calculamos el índice original
            indice_original = (alfabeto.index(letra) - desplazamiento) % len(alfabeto)
            texto_descifrado += alfabeto[indice_original]
        elif letra in " ,.:":  # Si es un espacio, coma, punto o dos puntos, lo añadimos directamente
            texto_descifrado += letra
        else:  # Si no está en el alfabeto
            return "Todos los caracteres deben estar en mayúsculas y dentro del alfabeto."
    return texto_descifrado
 
# Prueba de la función de cifrado
texto_prueba = "HOLA MUNDO."
desplazamiento_prueba = 3
texto_cifrado = cifrado_cesar_2(texto_prueba, desplazamiento_prueba)
print("Proceso de cifrado:")
print("- Texto plano:", texto_prueba)
print("- Texto cifrado:", texto_cifrado)
 
# Prueba de la función de descifrado con el texto cifrado anterior
texto_descifrado = descifrado_cesar_2(texto_cifrado, desplazamiento_prueba)
print("Proceso de descifrado:")
print("- Texto cifrado:", texto_cifrado)
print("- Texto descifrado:", texto_descifrado)
 
# Prueba de la función de cifrado con un texto en minúsculas
texto_minusc = "hola mundo."
resultado_minusc = cifrado_cesar_2(texto_minusc, desplazamiento_prueba)
print("Prueba con texto en minúsculas:")
print("-", resultado_minusc)