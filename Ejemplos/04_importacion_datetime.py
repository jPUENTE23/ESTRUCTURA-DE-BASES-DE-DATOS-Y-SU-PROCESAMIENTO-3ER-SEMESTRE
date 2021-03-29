'''
Ejemplo para ilustrar la importación de la librería datetime en Python 3
Demuestra el uso de: hora, fecha y aritmética de fechas
'''
import datetime
import time
SEPARADOR = ("*" * 20) + "\n"

#Creación de una hora específica
hora = datetime.time(10, 20, 30)
print(f"El tipo de objeto de la hora es {type(hora)}")
print(f"La hora es {hora}")
print(f"La hora de {hora} es {hora.hour}")		#Limitado 0..23
print(f"El minuto de {hora} es {hora.minute}")	#limitado 0..59
print(f"El segundo de {hora} es {hora.second}")	#limitado 0..59
print(f"El microsegundo de {hora} es {hora.microsecond}")	#limitado 0..999
print(SEPARADOR * 2)

#Determinar la fecha del sistema
fecha_actual = datetime.date.today()
print(f"El tipo de objeto de la fecha es {type(fecha_actual)}")
print(f"La fecha actual es {fecha_actual}")
print(f"El año actual es {fecha_actual.year}")
print(f"El mes actual es {fecha_actual.month}")
print(f"El día actual es {fecha_actual.day}")
print(SEPARADOR * 2)

#Convertir un string a fecha
fecha_capturada = input("Dime una fecha: \n")
fecha_procesada = datetime.datetime.strptime(fecha_capturada, "%d/%m/%Y").date()
print(type(fecha_capturada))
print(type(fecha_procesada))
print(f"La fecha capturada se transformó a {fecha_procesada}")

#Aritmética de fechas básica
cant_dias = int(input("Dime la cantidad de días a adelantar:\n"))
nueva_fecha = fecha_procesada + datetime.timedelta(days=+cant_dias)
print(f"La nueva fecha es {nueva_fecha}")
print(SEPARADOR)