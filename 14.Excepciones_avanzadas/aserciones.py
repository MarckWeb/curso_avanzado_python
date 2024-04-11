# las aserciones son afirmaciones que si son:
# -True no pasa nada
# -False genera un AssertionError


edad = int(input('Introduce tu edad: '))
assert edad >= 18, 'aqui va el mensaje de error'
print('Eres mayor de edad')

'''
Traceback (most recent call last):
  File "C:/Users/cursos/Curso_Python/14.Excepciones_avanzadas/aserciones.py", line 7, in <module>
    assert edad >= 18
AssertionError
'''