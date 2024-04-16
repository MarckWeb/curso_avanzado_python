import pytz
import datetime
import time

# crear un objeto date a partir de la clase date
hoy = datetime.date(2024, 4, 16)
print(hoy)  # 2024-04-16

# para cerar la marca de tiempo necesitamos el modulo time
timestamp = time.time()
print("Marca de tiempo:", timestamp)  # 1713263392.9983482

# Crear la fecha a partir de esa marca de tiempo
fecha = datetime.date.fromtimestamp(timestamp)
print('Fecha:', fecha)  # 2024-04-16

fecha = datetime.date.fromtimestamp(432262.32244)
print("Fecha:", fecha)  # 1970-01-06

hoy = datetime.date.today()
print(hoy)
print('Año', hoy.year)
print('Mes', hoy.month)
print('Dia', hoy.day)

# Crear uan fecha a partir de ISO 8601
ayer = datetime.date.fromisoformat("2024-04-15")  # completar con 0 por delante

print(ayer)

# reemplazar datos de fech
anteayer = ayer.replace(day=14)
print(anteayer)
print(ayer)

# numero del dia de la semana empezando 0=lunes
print('Dia semana:', hoy.weekday())  # 1

# numero del dia de la semana empezando 1=lunes
print('Dia semana:', hoy.isoweekday())  # 2

# Crear la hora con al clase time
# hora = datetime.datetime(12, 48, 39, 27, 2)
# print("Hora:", hora)


# Crear una hora con información de zona horaria utilizando la clase time
zona_horaria = pytz.timezone('Europe/Madrid')
hora = datetime.time(12, 48, 39, 27, tzinfo=zona_horaria)

print("Hora con zona horaria:", hora)
print("tzinfo:", hora.tzinfo)
