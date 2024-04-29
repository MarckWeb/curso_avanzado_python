import requests

# Consultar todos los alumnos
try:
    respuesta = requests.get("http://localhost:8080/alumnos.json")
    print(respuesta)
except requests.RequestException:
    print('ha ocurrido un error')
else:
    if respuesta.status_code == requests.codes.ok:
        print(respuesta.text)  # Muestra en modo texto # muestra propiedades
        print(respuesta.json())  # muestra como un json


# Consultar todos los alumnos ordenador por nota
# http://servidor:puerto/recurso?_sort=propiedad
try:
    #  respuesta = requests.get("http://localhost:8080/alumnos?_sort=nota")

    # OTRA FORMA
    respuesta = requests.get(
        "http://localhost:8080/alumnos.json", params={"_sort": "nota"})
    print(respuesta)

except requests.RequestException:
    print('ha ocurrido un error')
else:
    if respuesta.status_code == requests.codes.ok:
        print(respuesta.json())

# Consultar todos los alumnos ordenador por nota de forma desendente
# http://servidor:puerto/recurso?_sort=propiedad -propiedad signfica descendente
try:
    #  respuesta = requests.get("http://localhost:8080/alumnos?_sort=nota")

    # OTRA FORMA
    respuesta = requests.get(
        "http://localhost:8080/alumnos.json", params={"_sort": "-nota"})

except requests.RequestException:
    print('ha ocurrido un error')
else:
    if respuesta.status_code == requests.codes.ok:
        print(respuesta.json())


# Consultar los alumnos cateados
# https://docs.guidewire.com/cloud/pc/202306/cloudapibf/cloudAPI/topics/101-Fund/03-query-parameters/c_the-filter-query-parameter.html
try:
    # respuesta = requests.get("http://localhost:3000/alumnos?nota_lt=5")
    # Otra forma
    respuesta = requests.get("http://localhost:8080/alumnos.json",
                             params={"nota_lt": 5})  # nota menor o igual a 5
except requests.RequestException:
    print("Ha ocurrido un error")
else:
    if respuesta.status_code == requests.codes.ok:
        print(respuesta.json())  # Muestra como un json  # metodo

# Buscar un alumno por su id
print('-'*50)
try:
    respuesta = requests.get("http://localhost:8080/alumnos.json/3")
except requests.RequestException:
    print("Ha ocurrido un error")
else:
    if respuesta.status_code == requests.codes.ok:
        print('SOLO PEDRO', respuesta.json())  # Muestra como un json  # metodo
