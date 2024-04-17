import calendar

# con la funcion calendar mostramos el calendario del año pasado como argumento w=(ancho) l=(alto) c=(separacion) m=(fila por pantalla)
print(calendar.calendar(2024, w=4, l=2, m=2))


# mostrar el calendario de un mes y año especifico
print(calendar.month(2024, 4, w=4, l=2))


# mostrar el calendario de un mes y año especifico, sin nesecidad de meter en el print

calendar.prmonth(2024, 2, w=4, l=2)

# Mostrar el calendario pero comenzando la semana en domingo
# calendar.setfirstweekday(6)
calendar.setfirstweekday(calendar.SUNDAY)
calendar.prmonth(2024, 2, w=4, l=2)

# Dada una fecha retorna el dia de la semana en numero (lunes=0)
print(calendar.weekday(2024, 4, 17))


# Retorna una cadena con los dias de la semana en x caracteres(no pasa de tres letras, si se ponde 4 deja un espacio)
for i in range(10):
    print(calendar.weekheader(i), i)

'''Salidas de print(calendar.weekheader(i)) hasta el 10
Su Mo Tu We Th Fr Sa
Sun Mon Tue Wed Thu Fri Sat
Sun  Mon  Tue  Wed  Thu  Fri  Sat
 Sun   Mon   Tue   Wed   Thu   Fri   Sat
 Sun    Mon    Tue    Wed    Thu    Fri    Sat
  Sun     Mon     Tue     Wed     Thu     Fri     Sat
  Sun      Mon      Tue      Wed      Thu      Fri      Sat
  Sunday    Monday   Tuesday  Wednesday  Thursday   Friday   Saturday
'''

# Retorna un valor booleano indicando si el año es bisiesto o no
print('Es bisiesto?', calendar.isleap(2024))  # True
print('Es bisiesto?', calendar.isleap(2023))  # False


# Cuantos años bisiestos hay entre un rango de años que le vamos a pasar
# Recordar que en los rangps el ultimo no esta incluido [desde, hasta]
print('Cuantos bisiestos entre 2010 y 2024 => ',
      calendar.leapdays(2010, 2024))  # 3
print('Cuantos bisiestos entre 2010 y 2025 => ',
      calendar.leapdays(2010, 2025))  # 4

print(calendar.calendar(2024, w=1, l=2, c=10, m=1))


# otras clases para mostrar el calendario
calendar.prcal(2024)
calendar.prmonth(2024, 2)
