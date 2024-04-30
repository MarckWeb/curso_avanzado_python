import requests
import json

'''  DELETE para eliminar recursos  '''

# Por defecto, solo se permite borrar por id
try:
    respuesta = requests.delete("http://localhost:3000/alumnos/6")
except requests.RequestException:
    print("Ha ocurrido un error")
else:
    if respuesta.status_code == requests.codes.ok:
        print(respuesta.json())  # Muestra como un json  # metodo


# Otra opcion es lanzar una query por nombre
# Recuperar el id del recurso a eliminar
# borrar por ese id
'''
try:
    respuesta = requests.get("http://localhost:3000/alumnos?nombre=Laura")
    lista = respuesta.json()
    identificador = lista[0]['id']
    respuesta = requests.delete(f"http://localhost:3000/alumnos/{identificador}")
except requests.RequestException:
    print("Ha ocurrido un error")
else:
    if respuesta.status_code == requests.codes.ok:
        print(respuesta.json())  # Muestra como un json  # metodo
'''

try:
    respuesta = requests.delete("http://localhost:3000/alumnos/97fb")
except requests.RequestException:
    print("Ha ocurrido un error")
else:
    if respuesta.status_code == requests.codes.ok:
        print(respuesta.json())  # Muestra como un json  # metodo
