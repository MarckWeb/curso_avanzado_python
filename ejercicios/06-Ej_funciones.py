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
