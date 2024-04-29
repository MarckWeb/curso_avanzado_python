import requests

respuesta = requests.get("http://localhost:8080")
print(respuesta.status_code)  # 200 ok

# Ver todos los codigos de respuesta
for code in requests.codes.__dict__:
    # print(code)
    pass

# Condicional para ejecutar algo, solo si la respuesta se ha recibido correctamente
if respuesta.status_code == requests.codes.ok:
    print("Conexion correcta")

# Obtener las cabeceras
cabeceras = respuesta.headers
print(cabeceras)
print(type(cabeceras))

# Ver una cabecera en concreto
print("cabecera =>", cabeceras['Content-Type'])
print(respuesta.headers['Connection'])

# Mostrar el texto de la respuesta
# print(respuesta.text)  # muestra todo el html
