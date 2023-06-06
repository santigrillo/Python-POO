from manejadorEmpleados import manenajadorEmpleados

def test():
    mE = manenajadorEmpleados()
    mE.cargaPlanta()
    mE.cargaContratados()
    mE.cargaExternos()
    
    #Registrar horas trabajadas por empleado (contratado).
    mE.registrarHoras()
    
    #Dada una tarea, mostrar el monto a pagar. (solo se consideran tareas no finalizadas.)
    mE.totalTarea()    
    
    #Se les dará una ayuda económica a los empleados con sueldo menor a $xxx.xxx, listar los empleados que percibirán la ayuda.
    mE.ayudaEconomica()
    
    #Listar informacion y sueldo de todos los empleados.
    mE.muestraSueldos()
    
if __name__ == "__main__":
    test()
