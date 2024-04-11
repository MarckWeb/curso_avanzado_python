
'''
            Operaciones con cadenas
Las cadenas en Python pueden ser comparadas usando el mismo conjunto de operadores que se
emplean con los números.
- Observa estos operadores: también sirven para comparar cadenas:

        • cadena == número es siempre False (falso).
        • cadena != número es siempre True (verdadero).
        • cadena >= número siempre genera una excepción.
'''

print('20' == 20) # False
print('20' != 20) # False
#print('20' >= 20) # TypeError: '>=' not supported between instances of 'str' and 'int'
#print('20' <= 20) # TypeError: '<=' not supported between instances of 'str' and 'int'
#print('20' > 20) # TypeError: '>' not supported between instances of 'str' and 'int'
#print('20' > 20) # TypeError: '>' not supported between instances of 'str' and 'int'
print('10' == 1)

#Operadores de pertenencia
'''
count()
ord()
chr()
sort()
sorted()
startwith()
endwith()
find()
rfind()
join()
isspace()
filter()
center()
'''
cadena = 'abracadabra'
print('m' in cadena) # False
print('b' in cadena) # True

print('m' not in cadena) # True
print('b' not in cadena) # False

# Repetir una cadena o caracter
print('Hola' * 3)
print('a' * 5)

# el orden no afecta al producto
print(5 * 'holas')

""" Estas comillas se llaman docstring, utilizamos a nivel comentario de bloque:
pero tambien se puede dar otras utilizadades ej: me permite crear cadenas en varias lineas"""
nombre_completo = '''  
        Pepito
        
        Perez

'''
print(nombre_completo)

# insert() => se utiliza para insertar un elemento en una lista en una posición específica.
# Este método modifica la lista original y no devuelve nada (o devuelve None).
# El método insert() toma dos argumentos:
# Índice: La posición en la que quieres insertar el elemento.
# Elemento: El elemento que quieres insertar en la lista

# Crear una lista
lista = [1, 2, 3, 4, 5]

# Insertar el número 10 en la posición 2 (índice 1)
lista.insert(1, 10)

print(lista)  # Esto imprimirá: [1, 10, 2, 3, 4, 5]