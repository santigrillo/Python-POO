from class_mataprobada import materiaAprobada

class manejadorMa:
    
    def cargarinfo(materiasaprobadas):
        with open ("Integrador/materiasAprobadas.csv", 'r') as filemat:
            next(filemat)
            for line in filemat:
                line = line.split(";")
                m = materiaAprobada(line[0], line[1], line[2], float(line[3]), line[4])
                materiasaprobadas.append(m)
        return materiasaprobadas