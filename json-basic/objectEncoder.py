import json
from classPersona import persona
from manejadorPersonas import manejador

class ObjectEncoder(object):
    def decodificarDiccionario(self, d):
        if '__class__' not in d:
            return d
        else:
            class_name = d['__class__']
            class_ = eval(class_name)
            if class_name == 'manejador':
                personas = d['personas']
                manejador = class_()
                for i in range(len(personas)):
                    dPersona = personas[i]
                    class_name = dPersona.pop('__class__')
                    class_ = eval(class_name)
                    atributos = dPersona['__atributos__']
                    unaPersona = class_(**atributos)
                    manejador.addPersona(unaPersona)
                return manejador
    
    def guardarJSONArchivo(self, diccionario):
        with open("json-basic/data.json", 'a', encoding="UTF-8") as destino:
            json.dump(diccionario, destino, indent=4)
    
    def leerJSONArchivo(self):
        with open("json-basic/data.json", encoding="UTF-8") as fuente:
            diccionario = json.load(fuente)
            return diccionario
