import json
import requests


# fetch('https://jsonplaceholder.typicode.com/todos/1')
#       .then(response => response.json())
#       .then(json => console.log(json))
# Peticiones get

# OBTENER UN USUARIO
try:
    resp = requests.get('https://jsonplaceholder.typicode.com/todos/1')
    print(resp)
except:
    print('erro')
else:
    print(resp.json())

# ACTUALIZAR UN USUARIO
try:
    resp = requests.get('https://jsonplaceholder.typicode.com/todos/1')
    print(resp)
except:
    print('erro')
else:
    print(resp.json())

try:
    resp = requests.put("http://localhost:8080/alumnos.json/5",
                        headers=cabecera, data=json.dumps(new_pedro))
    pedro = requests.get("http://localhost:8080/alumnos.json/5")
except requests.RequestException:
    print('Error al actualizar')
else:
    print('Alumno modificado')
    print(pedro.json())
