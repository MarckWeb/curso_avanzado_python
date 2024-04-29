import socket

# Crear el socket
mi_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conectar al servidor
mi_socket.connect( ("www.python.org", 80) )  # sin http://   y en tupla (host,puerto)

# Enviar la peticion
# b"...." el metodo send no acepta strings lo estamos convirtiendo a bytes
# 1ª linea: Get(metodo HTTP utilizado)  / (nos posicionamos en el root del servidor)
#           HTTP:/1.1 Protocolo utilizado \r\n obligado al final de cada linea
# 2ª linea: Host: www.pue.es con juego de caracteres UTF-8 \r\n obligado al final de cada linea
# 3ª linea: Connection: close (cerrar la conexion) \r\n obligado al final de cada linea
# 4ª linea: El metodo send nos obliga a dejar la ultima linea en blanco \r\n obligado al final de cada linea
mi_socket.send(b"GET / HTTP/1.1\r\nHost: " +
               bytes("www.python.org", "utf8") +
               b"\r\nConnection: close\r\n\r\n")

# Recibir la respuesta
respuesta = mi_socket.recv(20000) # tamaño del buffer

# Avisamos de los motivos por el que vamos a cerrar la conexion
#mi_socket.shutdown(socket.SHUT_RD)

# Cierre definitivo del socket
mi_socket.close()

# mostrar la respuesta por consola
#print(repr(respuesta))
print((respuesta.decode()))