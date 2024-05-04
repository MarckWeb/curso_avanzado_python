# desplazamiento a la izquierda
# la potencia es el numero de desplazamiento
print(17 >> 1)  # 17 // 2**1
print(17 >> 2)  # 17 // 2**2
print(17 >> 3)  # 17 // 2**3
print(-17 >> 3)  # -17 // 2**3
print(17 >> 0)  # 17 // 2**0

# ErrorValue: negative shift count
# print(17 >> -3)
print(0 >> 3)  # 0 // 2 **3
print(0 // 2 ** 3)

# desplazamiento a la derecha
print(17 << 1)  # 17 * 2 ** 1
print(17 << 2)  # 17 * 2 ** 2
print(17 << 3)  # 17 * 2 ** 3


# Operador de desplazamiento a la izquierda (<<)
# Desplaza los bits de un número hacia la izquierda, agregando ceros a la derecha
numero = 8
# 8 en binario es 1000, después de desplazar dos bits a la izquierda: 100000 (32 en decimal)
desplazamiento_izquierda = numero << 2
print("Desplazamiento a la izquierda:", desplazamiento_izquierda)

# Operador de desplazamiento a la derecha (>>)
# Desplaza los bits de un número hacia la derecha, rellenando con el bit de signo o ceros a la izquierda
numero = 16
# 16 en binario es 10000, después de desplazar dos bits a la derecha: 100 (4 en decimal)
desplazamiento_derecha = numero >> 2
print("Desplazamiento a la derecha:", desplazamiento_derecha)
