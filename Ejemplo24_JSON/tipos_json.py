# Objeto JSON  {"propiedad":valor}
{"nombre": "Anabel", "edad": 53}
# Objeto JSON con una propiedad de tipo Array
{"nombre": "Anabel", "edad": 53, "cursos":["Python","Java","Angular"]}

# Crear un array de objetos JSON
[{"id":1,"descripcion":"Pantalla","precio":129.95,"stock":true},
 {"id":2,"descripcion":"Raton","precio":22.50,"stock":true},
 {"id":3,"descripcion":"Teclado","precio":49.80,"stock":false}]

''' Tipos de datos JSON '''
# numeros enteros:
{"decimal":6, "hexadecimal": 0x11, "octal": 0o11, "binario":0b11}

# numeros reales:
{"real":3.7865, "cientifica":8.12233E13, "negativo":-39.564444E-12}

# cadenas de texto, solo acepta comillas dobles
{"nombre": "Anabel"}

# booleanos: true y false
{"cansados":true, "ganas_fiesta":false}