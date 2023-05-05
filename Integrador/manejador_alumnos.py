class manejadorAl:
    def promedio(alumnos, materiasaprobadas):
        dni = input("Ingrese DNI del alumno > ")
        prom = float(0)
        cant = 0
        for i in range(len(materiasaprobadas)):
            if(materiasaprobadas[i].getDNI() == dni):
                prom += materiasaprobadas[i].getNota()
                cant += 1
        if prom == 0:
            print("El alumno no tiene notas o no existe.")
        elif prom != 0:
            print("El promedio para el alumno dni ", dni, " es ", prom/cant)
        return
        
    def obtenerAlumno(alumnos, dni):
        i = 0
        band = False
        while i < len(alumnos) and band == False:
            if(dni == alumnos[i].getDNI()):
                band = True
            i += 1 
        return i
        
    def promocionales(alumnos, materiasaprobadas):
        mat = input("Ingrese nombre de materia > ")
        print("DNI - Apellido y nombre - Fecha - Nota - Año que cursa")
        for i in range(len(materiasaprobadas)):
            if (mat == materiasaprobadas[i].getNomb()) and (materiasaprobadas[i].getNota() >= 7):
                dni = materiasaprobadas[i].getDNI()
                id = manejadorAl.obtenerAlumno(alumnos, dni)
                print(alumnos[id].getDNI(), " - ", alumnos[id].getNyA(), " - ", materiasaprobadas[i].getFecha(), " - ", materiasaprobadas[i].getNota(), " - ", alumnos[id].getAAAA())
                
    def ordenar(alumnos):
        alumnos.sort()
        for i in range(len(alumnos)):
            print(alumnos[i].getNyA())
        