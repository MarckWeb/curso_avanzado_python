'''
Desarrolla un script que recomiende acciones de seguridad informática a realizar basándose en el nivel de amenaza actual, utilizando sentencias if/elif/else en Python junto con los conceptos previamente aprendidos.
'''
import random


# asignacion de amenazas
niveles_amenaza = ('bajo', 'moderado', 'alto', 'critico')
amenaza_actual = random.choice(niveles_amenaza)
print(f'Nivel de amenaza actual {amenaza_actual}')



# acciones recomendadas a tomar segun el nivel de amenaza
if amenaza_actual in niveles_amenaza:
    if amenaza_actual == 'bajo':
        print('Actividad recomendada: Realizar auditorías de seguridad regulares')

    elif amenaza_actual == 'moderado':
        print('Actividad recomendada: Reforzar la concienciación de los empleados sobre riesgos de Ciberseguridad.')

    elif amenaza_actual == 'alto':
        print('Actividad recomendada: Implementar medidas de seguridad adicionales y revisar accesos')

    elif amenaza_actual == 'critico':
        print('Actividad recomendada: Activar el protocolo de respuesta a incidentes.')
    
    else:
        print('El nivel de amenaa no existe')
else:
    print("Selecciona un nivel de amenaza adecuado (bajo, moderado, alto, crítico)")