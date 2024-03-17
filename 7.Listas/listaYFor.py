no_olvidar = ['huevos', 'palta', 'lechuga', 'naranjas', 7000]

# mostrar elemento por cada iteracion de la lista
for elem in no_olvidar:
    print('No olvides', elem)


for elem in no_olvidar:
    if elem != 7000:
        print(elem)


# modificar elementos de la lista

no_olvidar[1] = 'queso'
no_olvidar[3] = 10000
# las listas de pueden modificar ya que son mutables a diferncia de los str que si lo son:
print(no_olvidar)

for e in no_olvidar:
    if e == 'queso':
        e = 'mango'
    print(e)


# INSERCION Y ELIMINACION DE ELEMENTOS

alumnos = ['juan', 'carlos', 'bob', 'jokin', 'ion', 'david']

alumnos2 = ['aitor', 'gorka']


# NINGUNA DE ESTAS SOLUCIONES CAMBIA  LA LISTA ORIGINAL SI NO QUE CREA UNA NUEVA
# contanacion con +
alumnos_total = alumnos + alumnos2
print(alumnos_total)

# multiplicar lista por x
print(alumnos2 * 2)
print(alumnos2 * 4)


# METODOS DE LAS LISTAS
# agregar un elemento a la lista
alumnos.append('new_alumno')
print(alumnos)

# agregar varios elemento a la lista, seria igual a la concatenacion
alumnos.extend(alumnos2)
print(alumnos)

# agregar elementos el cualquier posicion de la lista

alumnos.insert(2, 'Martha')
print(alumnos)
