# metodos de string

mi_curso = 'curso de python'

# imprime la cantidad de la cadena
print(len(mi_curso))  # resultado 15

# ACCESO MEDIANTE INDICES
# el indice del ultimo caracter sera N-1 ultima letra, N-2 penultima letra
# muestra el primer caracter de la cadena por su indice 0
print(mi_curso[0])  # Resultado c
print(mi_curso[1])  # Resultado u
print(mi_curso[4])  # Resultado o

# muestra la cadena desde el indice 0 hasta el indice 4
print(mi_curso[0:5])  # Resultado curso
print(mi_curso[0:4+1])  # Resultado curso

#  muestra la cadena desde el indice 9 hasta el ultimo que tenga la cadena
print(mi_curso[9:])  # Resultado python

# muestra la cadena desde el indice 0 hasta el indice 4
print(mi_curso[:4])  # Resultado curso de

# muestra la cadena desde el indice 0 hasta el final
print(mi_curso[:])  # Resultado curso de python

# Repeticion de string
# mostrara 5 veces el mismo string
print(mi_curso * 5)


# FORMATEO DE STRING

# 1ra forma sin formato
nombre = 'David'
apellido = 'Marck'
nombre_completo = nombre + ' ' + apellido

print(nombre_completo)

# 2da forma con formateo de string
# se puede utilizar tanto con comillas dobles o simples

nombre_completo_con_formateo = f'{nombre} {apellido}'
nombre_completo_con_dobles = f"{nombre} {apellido}"

print(nombre_completo_con_formateo)
print(nombre_completo_con_dobles)


# Mostrar solo caractes
nombre_caracter = f'{nombre[0]} {'caracter inicial'}'
print(nombre_caracter)

# NOTA: dentro del formateo de string no solo se puede colocar un formateo sino tambien cualquier expresion que nosotros queramos, esto dentro de los corchetes
