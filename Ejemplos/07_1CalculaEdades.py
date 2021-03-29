import datetime
SEPARADOR = "*" * 30
#Se desea capturar una lista de fechas de nacimiento (3) y se deberá informar
#la edad de esa persona a la fecha de hoy


























def calcula_edad(fecha_nac):
    hoy = datetime.date.today()
    return hoy.year - fecha_nac.year - ((hoy.month, hoy.day) < (fecha_nac.month, fecha_nac.day))

lista_fechas = []
for elemento in range(3):
    fecha_capturada = input("Dime una fecha (dd/mm/aaaa): \n")
    fecha_procesada = datetime.datetime.strptime(fecha_capturada, "%d/%m/%Y").date()
    lista_fechas.append(fecha_procesada)

print(SEPARADOR)

edades = list(map(calcula_edad, lista_fechas))

for edad in edades:
    print(edad)