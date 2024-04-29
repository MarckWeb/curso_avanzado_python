import json
import requests

# PETICIONES PUT = para modificar, actualizar datos
# Vamos a aprobar a Pedro y le ponemos un 5
new_pedro = {
    "id": 5,
    "nombre": "Pedro",
    "apellido": "González",
    "nota": 5,
    "repetir": True
}

cabecera = {'Content-type': 'aplication/json'}

try:
    resp = requests.put("http://localhost:8080/alumnos.json/5",
                        headers=cabecera, data=json.dumps(new_pedro))
    pedro = requests.get("http://localhost:8080/alumnos.json/5")
except requests.RequestException:
    print('Error al actualizar')
else:
    print('Alumno modificado')
    print(pedro.json())
