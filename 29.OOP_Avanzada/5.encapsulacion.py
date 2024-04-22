
class FechaEncapsulada:
    def __init__(self, dia, mes, anyo):
        self.__dia = 0
        self.__mes = 0
        self.__anyo = 0

        self.dia = dia
        self.mes = mes
        self.anyo = anyo

    @property
    def dia(self):
        return self.__dia

    @dia.setter
    def dia(self, dia):
        if dia >= 1 and dia <= 31:
            self.__dia = dia
        else:
            print('Dia no es valido')

    @property
    def mes(self):
        return self.__mes

    @mes.setter
    def mes(self, mes):
        if mes >= 1 and mes <= 12:
            self.__mes = mes
        else:
            print('Mes no es valido')

    @property
    def anyo(self):
        return self.__anyo

    @anyo.setter
    def anyo(self, anyo):
        if anyo == 2024 or anyo == 2025:
            self.__anyo = anyo
        else:
            print('Mes no es valido')

    # Metodo publico
    def __str__(self):
        # dia/mes/año
        return (f'{self.__dia}/{self.__mes}/{self.__anyo}')


fecha_buena = FechaEncapsulada(22, 4, 2024)
print(fecha_buena)

fecha_erronea = FechaEncapsulada(-12, 54, 2)
print(fecha_erronea)

fecha_erronea.dia = -12
fecha_erronea.mes = 54

# fecha_buena = FechaEncapsulada(22, 4, 2024)
# print(fecha_buena)

# try:
#     fecha_erronea = FechaEncapsulada(-12, 54, 2)
# except ValueError as e:
#     print(e)

# try:
#     fecha_erronea.dia = -12
# except ValueError as e:
#     print(e)

# try:
#     fecha_erronea.mes = 54
# except ValueError as e:
#     print(e)
