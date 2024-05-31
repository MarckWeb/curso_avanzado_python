# Definición del alfabeto
alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
 
def cifrado_cesar(texto, desplazamiento):
    """Cifra un texto utilizando el método del cifrado César.
 
    Args:
        texto (str): El texto a cifrar.
        desplazamiento (int): El número de posiciones que cada letra del texto
            será desplazada a lo largo del alfabeto.
 
    Returns:
        str: El texto cifrado si todos los caracteres son válidos (mayúsculas y dentro del alfabeto).
        str: Un mensaje de error si algún caracter no es válido.
 
    Ejemplo:
        >>> cifrado_cesar("HOLA MUNDO.", 3)
        'KROD PXQGR.'
    """
    texto_cifrado = ""
    for letra in texto:
        if letra in alfabeto:
            indice_nuevo = (alfabeto.index(letra) + desplazamiento) % len(alfabeto)
            texto_cifrado += alfabeto[indice_nuevo]
        elif letra in " ,.:":  
            texto_cifrado += letra
        else:  
            return "Todos los caracteres deben estar en mayúsculas y dentro del alfabeto."
    return texto_cifrado
 
def descifrado_cesar(texto_cifrado, desplazamiento):
    """Descifra un texto que ha sido cifrado con el método del cifrado César.
 
    Args:
        texto_cifrado (str): El texto cifrado a descifrar.
        desplazamiento (int): El número de posiciones que cada letra del texto cifrado
            será desplazada hacia atrás a lo largo del alfabeto.
 
    Returns:
        str: El texto descifrado si todos los caracteres son válidos.
        str: Un mensaje de error si algún caracter no es válido.
 
    Ejemplo:
        >>> descifrado_cesar("KROD PXQGR.", 3)
        'HOLA MUNDO.'
    """
    texto_descifrado = ""
    for letra in texto_cifrado:
        if letra in alfabeto:
            indice_original = (alfabeto.index(letra) - desplazamiento) % len(alfabeto)
            texto_descifrado += alfabeto[indice_original]
        elif letra in " ,.:":  
            texto_descifrado += letra
        else:  
            return "Todos los caracteres deben estar en mayúsculas y dentro del alfabeto."
    return texto_descifrado
 
# Mostramos la ayuda de la funcion cifrado_cesar
help(cifrado_cesar)