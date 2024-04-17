import calendar

calendario = calendar.Calendar()

# Mostrar los numeros de los dias de la semana
for num in calendario.iterweekdays():
    print(num, end='')  # 0123456

# Mostrar los dias que tiene el mes (a semanas completas)
# Retorna el numero del dia y los rellenos seran 0
for num_dia in calendario.itermonthdates(2024, 5):
    print(num_dia)
print()

# Mostrar lso dias que tiene el mes (a semanas completas)
# Retorna un objeto date
for num_dia in calendario.itermonthdays(2024, 5):
    print(num_dia)  # 0 0 1 2 .... 30 31 00

# Mostrar lso dias que tiene el mes (a semanas completas)
# Retorna una tupla (dia del mes, dia de la semana), los rellenos seran (0, dias de la semana)
for tupla in calendario.itermonthdays2(2024, 5):
    print(tupla)  # (0, 0) (0, 1) (1, 2) (2, 3) .... (30, 3) (31, 4) (0, 5) (0, 6)

# Mostrar lso dias que tiene el mes (a semanas completas)
# Retorna una tupla (año, mes, dia), los rellenos seran los dias anteriores y posteriores
for tupla in calendario.itermonthdays3(2024, 5):
    print(tupla)  # (2024, 4, 29) (2024, 4, 30) (2024, 5, 1) (2024, 5, 2) .... (2024, 5, 30) (2024, 5, 31) (2024, 6, 1) (2024, 6, 2)

# Mostrar lso dias que tiene el mes (a semanas completas)
# Retorna una tupla (año, mes, dia, dia de la semana), los rellenos seran los dias anteriores y posteriores
for tupla in calendario.itermonthdays4(2024, 5):
    print(tupla)
'''
   (2024, 4, 29, 0) 
    (2024, 4, 30, 1) 
    (2024, 5, 1, 2) 
    (2024, 5, 2, 3) 
    .... 
    (2024, 5, 30, 3)
    (2024, 5, 31, 4) 
    (2024, 6, 1, 5) 
    (2024, 6, 2, 6)
'''

# Mostrar las semanas que tiene el mes en listas por semana completas
# Retorna una lista con los dias de la semana, los faltantes los rellena a cero
for lista_semana in calendario.monthdayscalendar(2024, 5):
    print(lista_semana)

'''
[0, 0, 1, 2, 3, 4, 5]
[6, 7, 8, 9, 10, 11, 12]
[13, 14, 15, 16, 17, 18, 19]
[20, 21, 22, 23, 24, 25, 26]
[27, 28, 29, 30, 31, 0, 0
'''

# Mostrar las semanas que tiene el mes (a semanas completas)
# Retorna una lista con las tuplas (dia del mes, dia de la semana), lso rellenos (0, dia de la semana)
for lista_semana in calendario.monthdays2calendar(2024, 5):
    print(lista_semana)

'''
[(0, 0), (0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6)]
[(6, 0), (7, 1), (8, 2), (9, 3), (10, 4), (11, 5), (12, 6)]
[(13, 0), (14, 1), (15, 2), (16, 3), (17, 4), (18, 5), (19, 6)]
[(20, 0), (21, 1), (22, 2), (23, 3), (24, 4), (25, 5), (26, 6)]
[(27, 0), (28, 1), (29, 2), (30, 3), (31, 4), (0, 5), (0, 6)]
'''
