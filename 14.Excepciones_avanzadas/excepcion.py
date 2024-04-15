''' Crear una exception personalizada'''
# Todas las excepciones en Python son clases que estan herando
# directa o indirectamente de la clase BaseException
# Nuestra excepcion personalizada sera una clase que herede de Exception
import sys
import traceback


# NegativoError es una Exception que hereda de la clase BaseException
class NegativoError(BaseException):
    def __init__(self, message="La edad no puede ser negativa"):
        self.message = message
        super().__init__(self.message)


try:
    edad = int(input("Introduce tu edad: "))
    if edad < 0:
        # lanzar la excepcion de forma manual
        raise NegativoError
        # raise NegativoError("La edad no puede ser negativa")
except NegativoError as ex:
    # print(ex.getMensaje())
    # obtener las excepciones del sistema actuales
    ex_type, ex_value, ex_traceback = sys.exc_info()

    # stacktraces  como  tupla
    trace_back = traceback.extract_tb(ex_traceback)

    # Formatear stacktrace
    stack_trace = list()

    for trace in trace_back:
        # stack_trace.append("File : %s , Line : %d, Func.Name : %s, Message : %s" % (trace[0], trace[1], trace[2], trace[3]))

        print("Exception tipo : %s " % ex_type.__name__)
        print("Exception tipo : ", ex_type)

        print("Exception Archivo : ", trace[0])
        print("Exception Linea : %s", trace[1])
        print("Exception modulo : %s", trace[2])
        print("Exception lanzado : %s", trace[3])

        print("Exception message : %s", ex_value)

else:
    print("Edad positiva")
