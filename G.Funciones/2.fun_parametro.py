
def detalle(nombre, apellido, edad, altura):
    print('Nombre Completo:', nombre, apellido)
    print('Edad:', edad)
    print('Altura:', altura)


# invocamos a la funcion pasando los valores en el mismo orden que los parametros
# pasar por funcion
detalle('Jokin', 'Joker', 37, 1.75)

# invocar a la funcion pasando los valores con el nombre del parametro
# pasar parametros con keywords
# util si le paso los parametros desordenados
detalle(nombre='David', edad=40, apellido='Marc', altura=1.75)

# si la funcion tiene declarados 4 parametros hay que invocar con 4 datos
# si le falta alguno de sus paramteros los resulatdos seran.......

# detalle('Jokin', 'Joker', 37) # TypeError: detalle() missing 1 required positional argument: 'altura'
# detalle(nombre='David', edad=40, altura=1.75) TypeError: detalle() missing 1 required positional argument: 'apellido'
