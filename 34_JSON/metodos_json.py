import json

# dumps() -> traduce los datos de Python en JSON
cansado = True
print(json.dumps(cansado))  # true

# probar a traducir None, ['a','b','c']
print(json.dumps(None)) # null
print(json.dumps(['a','b','c']))  # ["a", "b", "c"]

# loads() -> coge un string de JSON y lo transforma en dato Python
texto_n = '1234.56'
print(json.loads(texto_n))
print(type(json.loads(texto_n)))

texto = '"Esto es una prueba"'
print(json.loads(texto))
print(type(json.loads(texto)))

lista = '[1, 2.5, true, null, ["a", "b", "c"]]'  # cadena de texto con valores JSON
print(json.loads(lista))
print(type(json.loads(lista)))

objeto = '{"nombre": "Anabel", "edad": 53, "cursos":["Python","Java","Angular"]}'
print(json.loads(objeto))
print(type(json.loads(objeto)))

''' Las clases no son serializables '''
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    # metodo estatico
    def encode(objeto):
        if isinstance(objeto, Persona):
            return objeto.__dict__
        else:
            print("No es instancia de Persona")

    # metodo dinamico
    '''
    def encode(self):
        if isinstance(self, Persona):
            return self.__dict__
        else:
            print("No es instancia de Persona")
    '''

    def decode(objeto):
        print(objeto)
        print("Nombre:", objeto['nombre'])
        print("Edad:", objeto['edad'])
        return Persona(objeto['nombre'], objeto['edad'])

    def __str__(self):
        return f"Nombre:{self.nombre}, Edad:{self.edad}"

persona = Persona("Juan", 27)
#print(json.dumps(persona)) # TypeError: Object of type Persona is not JSON serializable

# Si el metodo encode es estatico
#print(json.dumps(persona, default=Persona.encode)) # {"nombre": "Juan", "edad": 27}
# Si el metodo es dinamico -> metodo de instancia
#print(json.dumps(persona.encode())) # {"nombre": "Juan", "edad": 27}

persona_json = '{"nombre": "Juan", "edad": 27}'
print(json.loads(persona_json, object_hook=Persona.decode))

'''
persona_json2 = json.dumps(persona, default=Persona.encode)
print(persona_json2)
new_persona = json.loads(persona_json2, object_hook=Persona.decode)
print(new_persona)
print(type(new_persona))
'''











