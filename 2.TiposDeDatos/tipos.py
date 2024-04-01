"""
   Ejemplo de tipos de datos en python
"""

# numeros enteros (int)

numero1 = 5
numero2 = 4
suma = numero1 + numero2
print(suma)
print("Resaultado de la suma:", suma, type(suma))
# print("Resaultado de la suma:" + suma)

"""Python no permite concatenar numero con string (TypeError: can only concatenate str (not "int") to str), La solucion es convertir el numero a str"""
print("Resaultado de la suma: " + str(suma))
# es lioso la concatenacion de python
print("Resaultado de la suma: " + str(type(str(suma))))

# numeros reales (float)

# booleanos: True o False (bool)

# cadenas de texto (str)
