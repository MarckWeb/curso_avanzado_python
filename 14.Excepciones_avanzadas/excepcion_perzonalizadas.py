'''Crear una excepcion perzonalizada'''

# todas la excepciones en python con clases que estan heredando
# directa o indirectamente d ela clase BaseExcepcion
# Nuestra excepcion personalizada sera una ckase que herede de Excepcion


class NegativoError(Exception):  # NegativeError es una Excepcion
    def __init__(self, message):
        self.message = message
        # super().__init__(message)

    def get_message(self):
        return self.message


try:
    edad = int(input('Introduce tu edad: '))
    if edad < 0:

        # lanzar la excepcion de forma manual
        raise NegativoError('La edad no puede ser negativa')
except NegativoError as ex:
    print(ex.message)
    print(ex.get_message())


'''
Traceback (most recent call last):
  File "C:/Users/cursos/Curso_Python/14.Excepciones_avanzadas\excepcion_perzonalizadas.py", line 13, in <module>
    raise NegativoError
NegativoError
'''
