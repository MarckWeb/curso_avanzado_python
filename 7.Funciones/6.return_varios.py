"""
   Crear una funcion que recibe un texto y retornar:
      - El texto en mayuscula
      - El texto en minuscula
      - Longitud del texto
"""


def procesar_texto(texto):
    mayuscula = texto.upper()
    minuscula = texto.lower()
    longitud = len(texto)
    return mayuscula, minuscula, longitud


# recuperar con multiples variables
"""
 - el primer valor que devuleve se guarda en la primera variable
 - el segundo valor que devuleve se guarda en la segunda variable
 - el tercer valor que devuleve se guarda en la tercera variable
"""
mayuscula, minuscula, logitud = procesar_texto('David')
print(mayuscula)
print(minuscula)
print(logitud)


'''
   SI devuelve tres elementos se debe recoger los tres elementos si o si,
   caso contrario si solo se recura dos de los muchos, esto da error : 
   ValueError: too many values to unpack (expected 2) 
   
   mayuscula, minuscula = procesar_texto('David')
   print(mayuscula)
   print(minuscula)
'''


# Recuperar con una tupla
tupla = procesar_texto('Por fin es viernes')
print(tupla)
for item in tupla:
    print(item)
