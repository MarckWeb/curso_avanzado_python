'''
Se te proporciona un diccionario inicial llamado mi_diccionario que tiene algunos pares clave-valor. También se te proporciona otro diccionario llamado diccionario_para_fusionar. Realiza las siguientes tareas:
'''

mi_diccionario = {
    "clave1": "valor1",
    "clave2": "valor2",
    "clave3": "valor3"
}

diccionario_para_fusionar = {
    "clave3": "valor_fusionado",
    "clave4": "valor4"
}

# Acceso: Accede al valor asociado con la clave "clave1" y guárdalo en una variable llamada valor_obtenido.
valor_obtenido = mi_diccionario["clave1"]
print(valor_obtenido)
# Modificación: Cambia el valor asociado con la clave "clave1" a "valor_modificado".
mi_diccionario["clave1"] = "valor_modificado"
print(mi_diccionario)
# Adición: Añade un nuevo par clave-valor al diccionario: la clave será "clave_nueva" y el valor será "valor_nuevo".
mi_diccionario["clave_nueva"] = "valor_nuevo"
print(mi_diccionario)
# Eliminación: Elimina el par clave-valor con la clave "clave2".
del mi_diccionario["clave2"]
print(mi_diccionario)
# Iteración: Itera sobre el diccionario y muestra todas las claves.

for clave in mi_diccionario.keys():
    print(clave)
# Fusión: Fusiona mi_diccionario con diccionario_para_fusionar utilizando el método update.

mi_diccionario.update(diccionario_para_fusionar)
print(mi_diccionario)
