import requests

'''  GET es para consultas '''

# Consultar todos los alumnos
try:
    respuesta = requests.get("http://localhost:3000/alumnos")
except requests.RequestException:
    print("Ha ocurrido un error")
else:
    if respuesta.status_code == requests.codes.ok:
        # print(respuesta.text) # Muestra en modo texto   # propiedad
        print(respuesta.json())  # Muestra como un json  # metodo

# Consultar todos los alumnos ordenados por nota
# http://servidor:puerto/recurso?_sort=propiedad
try:
    # respuesta = requests.get("http://localhost:3000/alumnos?_sort=nota")
    # Otra forma
    respuesta = requests.get(
        "http://localhost:3000/alumnos", params={"_sort": "nota"})
except requests.RequestException:
    print("Ha ocurrido un error")
else:
    if respuesta.status_code == requests.codes.ok:
        print(respuesta.json())  # Muestra como un json  # metodo

# Consultar todos los alumnos ordenados por nota descendente
# http://servidor:puerto/recurso?_sort=-propiedad    -propiedad significa descendente
try:
    respuesta = requests.get("http://localhost:3000/alumnos?_sort=-nota")
    # Otra forma
    # respuesta = requests.get("http://localhost:3000/alumnos", params={"_sort": "-nota"})
except requests.RequestException:
    print("Ha ocurrido un error")
else:
    if respuesta.status_code == requests.codes.ok:
        print(respuesta.json())  # Muestra como un json  # metodo

# Consultar todos los alumnos repetidores
try:
    respuesta = requests.get("http://localhost:3000/alumnos?repetidor=1")
    # Otra forma
    # respuesta = requests.get("http://localhost:3000/alumnos", params={"repetidor": 1})  # solo funciona con 0,1
except requests.RequestException:
    print("Ha ocurrido un error")
else:
    if respuesta.status_code == requests.codes.ok:
        print(respuesta.json())  # Muestra como un json  # metodo

# Consultar los alumnos cateados
# https://docs.guidewire.com/cloud/pc/202306/cloudapibf/cloudAPI/topics/101-Fund/03-query-parameters/c_the-filter-query-parameter.html
try:
    # respuesta = requests.get("http://localhost:3000/alumnos?nota_lt=5")
    # Otra forma
    # nota menor o igual a 5
    respuesta = requests.get(
        "http://localhost:3000/alumnos", params={"nota_lt": 5})
except requests.RequestException:
    print("Ha ocurrido un error")
else:
    if respuesta.status_code == requests.codes.ok:
        print(respuesta.json())  # Muestra como un json  # metodo

# Buscar un alumno por su id
try:
    respuesta = requests.get("http://localhost:3000/alumnos/3")
except requests.RequestException:
    print("Ha ocurrido un error")
else:
    if respuesta.status_code == requests.codes.ok:
        print(respuesta.json())  # Muestra como un json  # metodo
