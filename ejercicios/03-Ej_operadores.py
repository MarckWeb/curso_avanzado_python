'''
Desarrollar un script que calcule la puntuación final de un participante en una competición de ciberseguridad, utilizando operadores aritméticos, de comparación y de asignación.
'''

# Puntuaciones del participante
puntuacion_pentesting = 3
puntuacion_analisis_vulnerabilidades = 8
puntuacion_desarrollo_exploits = 10
 
# Pesos de cada categoría
peso_pentesting = 0.5
peso_analisis_vulnerabilidades = 0.2
peso_desarrollo_exploits = 0.3
 
# Cálculo de la puntuación final
puntuacion_final = (puntuacion_pentesting * peso_pentesting) + (puntuacion_analisis_vulnerabilidades * peso_analisis_vulnerabilidades) + (puntuacion_desarrollo_exploits * peso_desarrollo_exploits)
 
# Determinación de aprobación y distinción de honor
participante_aprobado = puntuacion_final >= 5
distincion_honor = puntuacion_final == 10
 
# Mostrar resultados
print(f"La puntuación final es: {puntuacion_final}")
print(f"¿Participante aprobado?: {participante_aprobado}")
print(f"¿Distinción de honor?: {distincion_honor}")


'''
EJERCICIO
Implementa un programa en Python que verifique si una contraseña es segura bajo los criterios que se muestran a continuación. Para ello, utiliza operadores de pertenencia y lógicos.

Debe tener al menos 8 caracteres.

No debe contener el carácter @ ni #.

Debe contener al menos un número.

No debe contener espacios.
'''

# 
password='Testpass1234'

longitud = len(password) >= 8
print(longitud)
caracter = '@' in password or '#' in password
print(caracter)
numero = [char for char in longitud]
print(numero)
espacios = ' ' in password
print(espacios)