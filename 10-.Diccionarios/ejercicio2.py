# Ejercicios Diccionarios

# • Crea un diccionario con los siguientes key-values: "Name":
# "Testing", "Age": 0

developer = {
    "name" :"Marck",
    'Testing': True,
    'Age': 25
}

print(developer)
# • Inserta en el diccionario que has creado el key-value:
# "Debug": False

developer['Debug'] = False

print(developer)

# • Muestra por pantalla el valor asociado al key "Debug"

print(developer['Debug'])

# • Inserta en el diccionario que has creado el key-value:
# "Lista": [[1, 2, 3], 100]
developer['lista'] = [[1, 2, 3], 100]
print(developer)

# • Accede al último elemento del key "Lista"
print(developer['lista'][-1])

# • Borra el key-value "Debug": False

# print(developer.pop('Debug'))
del developer['Debug']
print(developer)

# • Borra el key-value "Age": 0 y guarda el valor en una variable
# llamada valor
developer['Age'] = {'Valor':0}
print(developer)

valor = developer.pop('Age')

print(developer)
print(valor)
# • Añade dentro de la lista, dentro de la lista del key "Lista",
# el elemento -300

developer['lista'].append(-300)
print(developer)