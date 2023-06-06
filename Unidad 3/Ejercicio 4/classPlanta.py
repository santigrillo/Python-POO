from classEmpleado import empleado

class planta(empleado):
	__sueldoBasico = int
	__antiguedad = int
	
	def __init__(self, dni, nombre, telefono, sueldobasico, antiguedad):
		super().__init__(dni, nombre, telefono)
		self.__sueldobasico = sueldobasico
		self.__antiguedad = antiguedad

	def calcularSueldo(self):
		return int(self.__sueldobasico * (1/100) * self.__antiguedad)