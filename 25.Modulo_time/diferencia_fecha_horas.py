from datetime import datetime
from datetime import timedelta

# diferencia de fecha y horas

print(datetime(2024, 4, 16, 9) - datetime(2024, 4, 15, 9))  # 1 day, 0:00:00

# Crear un periodo de tiempo

# El strptime()método crea un objeto de fecha y hora a partir de la cadena dada .
dt_string = "16/04/2024 14:52:32"
print("dd/mm/yyyy")
dt_object1 = datetime.strptime(dt_string, "%d/%m/%Y %H:%M:%S")
print("dt_object1 =", dt_object1)  # dt_object1 = 2024-04-16 14:52:32

dt_string = "04/16/2024 14:52:32"
print("mm/dd/yyyy ")
dt_object2 = datetime.strptime(dt_string, "%m/%d/%Y %H:%M:%S")
print("dt_object2 =", dt_object2)  # dt_object2 = 2024-04-16 14:52:32
