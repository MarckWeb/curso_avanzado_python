no_olvidar = ['huevos', 'palta', 'lechuga', 'naranjas', 7000]

no_olvidar.append('leche')

print('hay', len(no_olvidar), 'cosas por comprar')

# verificar si existe un elemnto indicado dentro de la lista

print('existe vino en la lista', ('vino' in no_olvidar))
print('existe pan en la lista', ('pan' in no_olvidar))
print('existe huevos en la lista', ('huevos' in no_olvidar))

# verificar en que posicion se encuentra un elemento

print('si palta esta en que posicion se encuentra?', no_olvidar.index('palta'))
print('si leche esta en que posicion se encuentra?', no_olvidar.index('leche'))
# print('si pulpo esta en que posicion se encuentra?', no_olvidar.index('pulpo')) # error no esta dentro de la lista


# CONVERTIR UN STRING EN UNA LISTA
