'''
    Crear clase Fecha (dia, mes y anyo)
'''


class Fecha:
    def __init__(self, dia, mes, anyo):
        # Variables de Instancia
        # son publicas se pueden acceder a ella para leer o modificar el valor
        self.dia = dia
        self.mes = mes
        self.anyo = anyo

    # metodo de instancia
    # Metodo publico
    def mostrar_fecha(self):
        return (f'{self.dia}/{self.mes}/{self.anyo}')


fecha1 = Fecha(11, 4, 2024)
fecha1.dia = 122
print('Hoy:', fecha1.mostrar_fecha())

'''
Una clase encapsuada tiene todoas sus propiedades son privadas y se accede a
ellas a traves de los metodos de acceso publicos: getter y setter
'''


class FechaEncapsulada:
    # _name = variable protected (ligado a la herencia)
    # __name = variable privada
    # constructor
    def __init__(self, dia, mes, anyo):
        # Variables de Instancia
        # son privadas: no se pueden acceder desde fuera de la clase
        '''tambien se puede cerar aqui las variables inicializadas'''
        # self.__dia = dia
        # self.__mes = mes
        # self.__anyo = anyo
        self.__dia = 0
        self.__mes = 0
        self.__anyo = 0
        self.setDia(dia)
        self.setMes(mes)
        self.setAnyo(anyo)

    # Metodos de acceso publico:
    # getxxx() de lectura, retorna el valor de la variable
    # setXXX() de escrituta, establecer o modificar el valor
    def getDia(self):
        return self.__dia

    def setDia(self, dia):
        # comprobacion que el dia recibido es correcto
        # damos por bueno si el dia esta entre 1 y 30
        if dia >= 1 and dia <= 31:
            self.__dia = dia
        else:
            print('Dia no es valido')

    def getMes(self):
        return self.__mes

    def setMes(self, mes):
        # comprobacion que el dia recibido es correcto
        # damos por bueno si el dia esta entre 1 y 30
        if mes >= 1 and mes <= 12:
            self.__mes = mes
        else:
            print('Mes no es valido')

    def getAnyo(self):
        return self.__anyo

    def setAnyo(self, anyo):
        # comprobacion que el anyo recibido es correcto
        # damos por bueno si el dia esta entre 2024 y 2025
        if anyo == 2024 or anyo == 2025:
            self.__anyo = anyo
        else:
            print('Mes no es valido')

    # metodo de instancia
    # Metodo publico
    def mostrar_fecha(self):
        return (f'{self.__dia}/{self.__mes}/{self.__anyo}')
