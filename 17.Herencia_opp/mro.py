'''

class A:
    def super_clase(self):
        print('Superclase')


class B(A):
    def medio(self):
        print('Clase en el medio')


class C(A, B):
    def abajo(self):
        print('Clase abajo de todo')

c = C()
'''

# c.abajo() # TypeError: Cannot create a consistent method resolution order (MRO) for bases A, B
# c.super_clase() # TypeError: Cannot create a consistent method resolution order (MRO) for bases A, B


# Problema del diamanate


class AA:
    def super_clase(self):
        print("Superclase")


class BB(AA):
    def medio(self):
        print("Clase BB en el medio")


class CC(AA):
    def medio(self):
        print("Clase CC en el medio")


class DD(CC, BB):
    # En python no se permite sobre carga de metodos
    # Los metodo comunes entra CC Y BB, se resuelve que al ser
    # BB la segunda clase en herencia busca  los metodo heredados de CC
    def abajo(self):
        print("Clase abajo")


dd = DD()
dd.abajo()  # Clase abajo
dd.super_clase()  # Superclase
'''llama al metodo de la clase BB porque con herencia multiple es la primera(se refiere al orden delcarado en el paramtero)'''
dd.medio()  # Clase BB en el medio
'''Intercambiando orden de class DD(CC, BB,): //saldra =>> Clase CC en el medio'''

'''
   MRO: Orden de ejecucion de los metodos
   dd.abajo(): Busca ese metodo en la clase DD y lo encuentra
   dd.medio(): Empieza a buscar en la primera clase que pongo en herencia multiple DD(CC, BB)
               ejecuta el de la clase CC
   dd.super_clase(): Este metodo esta de forma implicita en DD
'''
