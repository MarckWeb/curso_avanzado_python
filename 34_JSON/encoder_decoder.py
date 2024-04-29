import json
import ast

''' Las clases no son serializables '''
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

class PersonaEncoder(json.JSONEncoder):
    def default(self, objeto):
        if isinstance(objeto, Persona):
            return objeto.__dict__
        else:
            print("No es instancia de Persona")

class PersonaDecoder(json.JSONDecoder):
    def __init__(self):
        json.JSONDecoder.__init__(self, object_hook=self.decode)

    def decode(self, objeto):
        # El objeto recibido es un string y lo convertimos a diccionario
        # Cualquiera de las 2 formas es correcta
        #diccionario = ast.literal_eval(objeto)
        diccionario = json.loads(objeto)
        print(type(diccionario))
        return Persona(diccionario['nombre'],diccionario['edad'])


persona = Persona("Juan", 27)
persona_json = json.dumps(persona, cls=PersonaEncoder)
print(persona_json)  # '{"nombre": "Juan", "edad": 27}'
print(type(persona_json)) # <class 'str'>

new_persona = json.loads(persona_json, cls=PersonaDecoder)
print(new_persona)
