import time

# crear fecha y hora a partir de la marca de tiempo
timestamp = 55675434
print(time.ctime(timestamp))  # Thu Oct  7 11:23:54 1971

# Crear fecha y hora actual
print(time.ctime())  # Tue Apr 16 14:17:50 2024


# Retorna la fecha y la hora en un objeto struct_time
# time.struct_time(tm_year=1971, tm_mon=10, tm_mday=7, tm_hour=9, tm_min=23, tm_sec=54, tm_wday=3, tm_yday=280, tm_isdst=0)
print(time.gmtime(timestamp))

# time.struct_time(tm_year=1971, tm_mon=10, tm_mday=7, tm_hour=11, tm_min=23, tm_sec=54, tm_wday=3, tm_yday=280, tm_isdst=1)
print(time.localtime(timestamp))

#
st = time.gmtime(timestamp)
# cohe el objetos struct_time y lo convierte en cadenas
print(time.asctime(st))  # Thu Oct  7 09:23:54 1971

# pasamos los datos de fecha y hora como tupla y devuelve timestamp
print(time.mktime((2024, 4, 16, 14, 19, 0, 0, 300, 0)))
