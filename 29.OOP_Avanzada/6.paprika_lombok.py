from paprika import to_string, equals_and_hashcode, data, singleton


@singleton
@data
class FechaEncapsulada:
    dia: int
    mes: int
    anyo: int


fecha_buena = FechaEncapsulada(22, 4, 2024)
print(fecha_buena)

fecha_erronea = FechaEncapsulada(-12, 54, 2)
print(fecha_erronea)

fecha_erronea.dia = -12
fecha_erronea.mes = 54

print(fecha_buena == fecha_erronea and fecha_buena is fecha_erronea)  # True ✅
