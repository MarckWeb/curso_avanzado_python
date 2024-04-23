# https://python.19633.com/es/Python/1002017286.html
'''
    Un método de clase toma clase (cls ) en sí mismo como el primer argumento. 
    Un método de clase solo puede cambiar el estado de la clase pero 
    no el estado del objeto de clase porque los objetos de clase 
    no pueden acceder a los métodos de clase, solo la clase 
    puede acceder directamente a los métodos de clase. 
    Actúa como un constructor alternativo de la clase.
'''

'''
    Los métodos estáticos son métodos independientes, 
    lo que significa que no aceptan ni el objeto de clase 
    ni la clase en sí como argumento, 
    no funciona con variables de instancia ni con variables de clase. 
    Se puede acceder directamente desde la Clase o desde el objeto Clase
'''


class Student:
    # class variable
    students_count = 0

    # class constructor
    def __init__(self, first_name, last_name, roll_no):
        self.first_name = first_name
        self.last_name = last_name
        self.roll_no = roll_no
        self.increment_student()

    # class method
    @classmethod
    def student_full_name(cls, full_name, roll_no):
        full_name = full_name
        return cls(full_name, '', roll_no)

    # class method
    @classmethod
    def increment_student(cls):
        cls.students_count += 1

    # static method
    @staticmethod
    def get_student_rules():
        rules = """
        1. Respect the teacher.
        2. Ask questions.
        """
        return rules


e1 = Student('Aman', 'Gupta', 25)
print(e1.first_name)
print(e1.last_name)
print(e1.roll_no)

res = Student.student_full_name("a", 30)
print(res.first_name)
print(res.last_name)
print(res.roll_no)

# Los métodos de clase también se usan cuando queremos acceder solo a las variables de clase,
count = Student.students_count
print(f'Number of students: {count}')

# Invocamos al metodo estatico a traves de la instancia y de la clase
print(e1.get_student_rules())
print(Student.get_student_rules())
