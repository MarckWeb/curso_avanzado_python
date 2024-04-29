import socket

# Crear el socket
mi_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conectar al servidor
mi_socket.connect(("www.python.org", 80))  # sin http:// y en tupla (host,puerto)

# Construir y enviar la solicitud HTTP correctamente formateada
solicitud_http = ("GET / HTTP/1.1\r\n"
                  "Host: www.python.org\r\n"
                  "Connection: close\r\n"
                  "\r\n")  # Dejar una línea en blanco al final de la solicitud

# Convertir la solicitud a bytes y enviarla
mi_socket.sendall(solicitud_http.encode())

# Recibir y almacenar la respuesta del servidor
respuesta = b""
while True:
    datos = mi_socket.recv(4096)  # Recibir datos en fragmentos de 4096 bytes
    if not datos:
        break
    respuesta += datos

# Cierre del socket
mi_socket.close()

# Mostrar la respuesta por consola
print(respuesta.decode())
