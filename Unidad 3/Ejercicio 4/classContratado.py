from classEmpleado import empleado

class contratado(empleado):
		__fechaInicioContrato = str
		__fechaFinContrato = str
		__cantidadDeHorasTrabajadas = int
		__valorPorHora = 250 #(variable de clase)

		def __init__(self, dni, nom, tel, fic, ffc):
				super().__init__(dni, nom, tel)
				self.__fechaInicioContrato = fic
				self.__fechaFinContrato = ffc
				self.__cantidadDeHorasTrabajadas = 0

		def calcularSueldo(self):
				return int(self.__cantidadDeHorasTrabajadas * self.__valorPorHora)

		def sumarHoras(self):
			super().getInfoEmpleado()
			horas = int(input("Ingrese horas a agregar > "))
			self.__cantidadDeHorasTrabajadas += horas
			print("Horas registradas con éxito.")
			return