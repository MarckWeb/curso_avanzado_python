# crear un conjunto con las letras de la palabra y la palabra es 'abracadabra'
# que no sean a ni b ni c


# codigo completo
# 1ra solucion:
def filtrar():
    resultado = set()
    for letra in 'abracadabra':
        if letra not in 'abc':
            resultado.add(letra)
    return resultado


print(filtrar())

# 2da solucion:
palabra = {'a', 'b', 'r', 'a', 'c', 'a', 'd', 'a', 'b', 'r', 'a'}
quitar = {'a', 'b', 'c'}

print(palabra.difference(quitar))

# 3ra solucion
print(set('abracadabra') - {'a', 'b', 'c'})

# compresion
conjunto_letras = {
    letra for letra in 'abracadabra' if letra not in {'a', 'b', 'c'}}

print(conjunto_letras)
