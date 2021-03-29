
# funciones con modulo datetime

import datetime
import time

# la funcion de datetime.time, lo que hace es ayudarnos a combertir un tipo de dato str
# a uno datetime, solo deaccuerdo a una hora espesificada (HH-MM-SS) dentro de los argumentos
hora = datetime.time(22,10,10)
print("El tipo de datos de la hora es {}".format(type(hora)))
print("La hora es {} ".format(hora))
print("La hora de {} es {}".format(hora,(hora.hour)))           # limitado a 23
print("Los minutos de {} son {}".format(hora,(hora.minute)))    # limitado a 59
print("Los segundos de {} son {}".format(hora,(hora.second)))   # limitado a 59

# determinar la fecha del sistema
fecha = datetime.date.today()
print("El tipo de datos de ña fecha es {} ".format(type(fecha)))
print("La fecha es {} ".format(fecha))
print("El año actual es {}".format(fecha.year))
print("El mes actuañ es {}".format(fecha.month))
print("El dia actuañ es {}".format(fecha.day))

# convertir un str a fecha
fecha_capturada = input("Ingrese un fecha (DD/MM/AAAA): ")

# la funcion strptime es la que nos ayudara a convertir un string a un tipo de datos fecha...
# dentro de lla pondremos los argumentos que es la variable donde guardamos la fehca anteriormente...
# y el formato de fecha al que lo queremos converitr.
fecha_procesada = datetime.datetime.strptime(fecha_capturada, "%d/%m/%Y").date()
print(type(fecha_capturada))
print(type(fecha_procesada))
print("La fecha es {} ".format(fecha_procesada))

# aritmetica de fechas
cant_dias = int(input("Dame la cantidad de dias a extender: "))

# la sig funcion nos permite agregar mas dias de acuerdo a la fehca ingresada anteriormente...
# Ejemplo: si la fehca es 26/12/20201 y la extension de dias que queremos son 5...
# nos devolvera la fecha 31/12/20201.
nueva_fecha = fecha_procesada + datetime.timedelta(days=+cant_dias)
print("La nueva fecha es: {} ".format(nueva_fecha))