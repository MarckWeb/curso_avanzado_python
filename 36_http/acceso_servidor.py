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
print(respuesta.text)  # muestra todo el html


# Manejo de errores

try:
    respuesta = requests.get("http://localhost:8080", timeout=1)
except requests.exceptions.Timeout:
    print('Error de time out')
else:
    print('Conexion ok')


# Capturar un error de conexion = cuando la url es incorrecta

try:
    respuesta = requests.get("http://localhost:8010")
except requests.exceptions.ConnectionError:
    print('Error de conexion')
else:
    print('Conexion ok')

# Cuando la escritura de la url esta mal escrita
try:
    respuesta = requests.get("http:/localhost:8010")
except requests.exceptions.InvalidURL:
    print('Error de URL')
else:
    print('Conexion ok')

# Ver todas las excepciones
# print(requests.exceptions)
print("Todas las excepciones disponibles en 'requests.exceptions':")
for exception_name in dir(requests.exceptions):
    if not exception_name.startswith("_"):
        print(exception_name)
