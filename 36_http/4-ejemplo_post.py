import json
import requests

'''  POST para crear recurso nuevo   '''

'''new_alumno = {
      "id": "6",
      "nombre": "Pepito",
      "apellido": "Perez",
      "nota": 2.7,
      "repetidor": True
    }'''

# Si no pongo id genera un valor alfanumerico "id": "97fb"
new_alumno = {
    "nombre": "Prueba",
    "apellido": "Perez",
    "nota": 2.7,
    "repetidor": True
}

try:
    respuesta = requests.post(
        "http://localhost:3000/alumnos", data=json.dumps(new_alumno))

    # Volvemos a consultar el nuevo alumno
    # nuevo = requests.get("http://localhost:3000/alumnos/6")
except requests.RequestException:
    print("Error al crear nuevo alumno")
else:
    print("Alumno creado")
    # print(nuevo.json())
