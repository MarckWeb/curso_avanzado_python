

numero1 = 5
numero2 = 4
suma = numero1 + numero2
print(suma)
print("Resaultado de la suma:", suma, type(suma))
# print("Resaultado de la suma:" + suma)

"""
Python no permite concatenar un numero con un string da un error:
(TypeError: can only concatenate str (not "int") to str), 
 - La solucion es convertir el numero a str
"""

print("Resaultado de la suma: " + str(suma))
# es lioso la concatenacion de python
print("Resaultado de la suma: " + str(type(str(suma))))

# numeros reales (float)
base = 5.78
altura = 9.23

triangulo = base * altura / 2
print("Area dek triangulo", triangulo, type(triangulo))

# booleanos: True o False (bool)
persona = True
print("Eres persona?", persona, type(persona))

# cadenas de texto (str)
nombre = "Pepito"
apellido = 'Perez'
print(nombre, apellido, type(nombre), type(apellido))
