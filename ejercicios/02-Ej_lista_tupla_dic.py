# Crea una lista llamada platos que contenga los siguientes platos (strings): Paella, Risotto, Sushi, Tacos y Pizza.
platos = ['Paella', 'Risotto', 'Sushi', 'Tacos', 'Pizza']


# Crea una tupla llamada precios con los precios correspondientes a cada plato de la lista platos. Asegúrate de que el orden de los precios coincida con el de los platos. Los precios son los siguientes: 

precios = (15, 12, 20, 10, 8)

# Utiliza slicing para crear una lista platos_seleccionados que contenga los nombres del segundo al cuarto plato de la lista platos.

platos_seleccionados = platos[1:4]

# Crea un diccionario menu donde cada clave sea un nombre de plato y su valor correspondiente sea el precio.
menu = {
    platos[0]: precios[0],
    platos[1]: precios[1],
    platos[2]: precios[2],
    platos[3]: precios[3],
    platos[4]: precios[4]
}

print('Bienvenidos a nuestro menú especial:')
# Imprime el menú completo por pantalla.

descripcion_menu = (
    f"Bienvenidos a nuestro menú especial: "
    f"\n - Paella:{menu['Paella']} euros"
    f"\n - Risotto: {menu['Risotto']} euros"
    f"\n - Sushi: {menu['Sushi']} euros"
    f"\n - Tacos: {menu['Tacos']} euros"
    f"\n - Pizza: {menu['Pizza']} euros"
)
print(descripcion_menu)


# Utiliza indexing para imprimir el nombre y el precio del tercer plato del menú.
tercer_plato = platos[2]
precio_tercer_plato = menu[tercer_plato]
print(f"El tercer plato es {tercer_plato} y su precio es {precio_tercer_plato}.")

# Utiliza stride en la lista platos para crear una nueva lista platos_pares que contenga solo los platos en posiciones pares e imprímelos.

platos_pares = platos[::2]
print("Los platos pares son:", platos_pares)

