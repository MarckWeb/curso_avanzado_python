import socket

host = '127.0.0.1'
port = 8050
 
obj = socket.socket()
obj.connect((host, port))

print("Conectado al servidor")
 
while True:
    mens = input("Comando >> ")
 
    obj.send(mens.encode())

    respuesta = obj.recv(1024)

    print(respuesta.decode())

obj.close()

print("Conexión cerrada")