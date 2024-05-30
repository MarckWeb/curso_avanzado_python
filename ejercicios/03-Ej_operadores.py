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

# Definición de la contraseña
password = "Testpass1234"
 
# Revisión de los criterios
longitud = len(password) >= 8
caracter = "@" not in password and "#" not in password
numero = "0" in password or "1" in password or "2" in password or "3" in password or "4" in password or "5" in password or "6" in password or "7" in password or "8" in password or "9" in password
espacios = " " not in password
 
# Mostramos por pantalla el resultado
resultado = longitud and caracter and numero and espacios
 
print(f"Contraseña: {password}")
print(f"¿La contraseña cumple con los criterios establecidos? {resultado}")