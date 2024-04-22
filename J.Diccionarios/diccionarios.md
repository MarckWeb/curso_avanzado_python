# DICCIONARIOS

Los diccionarios en Python son una estructura de datos mutable y no ordenada que permite almacenar pares de _clave-valor_. Los diccionarios se pueden utilizar para almacenar información de una manera organizada y fácil de buscar. En Python, los diccionarios se crean utilizando llaves ({}) que rodean los pares _clave-valor_, donde cada clave está separada de su valor por dos puntos (:), y cada par clave-valor está separado por comas.

Un ejemplo básico de un diccionario en Python es el siguiente:

```py
mi_diccionario = {
"clave1": "valor1",
"clave2": "valor2",
"clave3": "valor3"
}
```

En este ejemplo, se crea un diccionario llamado mi*diccionario, que contiene tres pares clave-valor. Las claves en este caso son cadenas de texto *("clave1", "clave2" y "clave3")_, y los valores también son cadenas de texto _("valor1", "valor2" y "valor3")\_.

Es importante mencionar que las claves de un diccionario deben ser únicas y no se pueden repetir, ya que representan un identificador único para cada valor. Además, las claves deben ser inmutables, lo que significa que su contenido no puede cambiar después de ser asignado. Los tipos de datos comunes que se utilizan como claves en los diccionarios incluyen strings, números y tuplas (si no contienen elementos mutables).

_" Para acceder a un valor en un diccionario, se utiliza la clave correspondiente entre corchetes ([]): "_

```py
valor = mi_diccionario["clave1"]
print(valor) # Output: "valor1"
```

Si se intenta acceder a una clave que no existe en el diccionario, se generará un error KeyError. Para evitar esto, es posible utilizar el método get(), que devuelve None si la clave no se encuentra en el diccionario:

```py
valor = mi_diccionario.get("clave_inexistente")
print(valor) # Output: None
```

Los diccionarios se pueden modificar agregando, actualizando o eliminando pares clave-valor. Para agregar un nuevo par clave-valor, simplemente se asigna un valor a una clave que no existe previamente en el diccionario:

```py
mi_diccionario["clave_nueva"] = "valor_nuevo"
```

Para actualizar el valor de una clave existente, se asigna un nuevo valor a la clave:

```py
mi_diccionario["clave1"] = "valor_actualizado"
```

Para eliminar un par clave-valor del diccionario, se utiliza la palabra clave seguida de la clave a eliminar:

```py
del mi_diccionario["clave1"]
```

Es posible iterar sobre las claves, los valores o ambos (pares clave-valor) de un diccionario utilizando diferentes métodos:

```py
# Iterar sobre las claves del diccionario

for clave in mi_diccionario.keys():
print(clave)

# Iterar sobre los valores del diccionario

for valor in mi_diccionario.values():
print(valor)

# Iterar sobre los pares clave-valor del diccionario

for clave, valor in mi_diccionario.items():
print(clave, valor)
```

El método update se usa para fusionar dos diccionarios en Python. Este método toma un diccionario como argumento y actualiza el diccionario original con los pares clave-valor del diccionario proporcionado como argumento. Si una clave en el diccionario original también está presente en el diccionario suministrado, el método actualizará el valor de la clave con el valor del diccionario suministrado. Si hay claves nuevas en el diccionario suministrado que no están en el diccionario original, estas claves y sus valores serán agregados al diccionario original.

```py
diccionario1 = {"a": 1, "b": 2}
diccionario2 = {"b": 3, "c": 4}

# Fusionar diccionario2 en diccionario1

diccionario1.update(diccionario2)

print(diccionario1) # {"a": 1, "b": 3, "c": 4}
```

Como se aprecia, el valor de la clave "b" en diccionario1 fue actualizado con el valor de diccionario2, mientras que la clave "c" y su valor fueron agregados a diccionario1.

En resumen, los diccionarios en Python son una estructura de datos versátil y eficiente para almacenar y organizar información en forma de pares clave-valor. Algunos de los casos de uso comunes para los diccionarios incluyen el almacenamiento de configuraciones, recuentos de frecuencia, tablas de hash y más.
