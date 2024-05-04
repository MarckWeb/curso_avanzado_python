"""
   Solicitar al usuario la letra del dia de la suma (l, m, x, j, v, s, d)
   puede ser que introduzca la letra en mayuscula
   controlar si la letra no es valida
   mostrar el dia de la semana
"""

dia = input('Introduce el dia de la semana: ')

if dia == 'l' or dia == 'L':
    print('El dia es lunes')
elif dia == 'm' or dia == 'M':
    print('El dia es martes')
elif dia == 'x' or dia == 'X':
    print('El dia es miercoles')
elif dia == 'j' or dia == 'J':
    print('El dia es jueves')
elif dia == 'v' or dia == 'V':
    print('El dia es viernes')
elif dia == 's' or dia == 'S':
    print('El dia es sabado')
elif dia == 'd' or dia == 'D':
    print('El dia es domingo')
else:
    print('el dia no existe')
