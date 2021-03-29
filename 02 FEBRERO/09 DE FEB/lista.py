
import datetime

# se crea la lista en donde almacenamos las fechas
cumpleaños = list()

# creamos ciiclo en cuanto las fechas que se van a ingresar
for num in range (2):
    date = input("Fecha de nacimiento (dd/mm/aaaa): ")

    # la fecha ingresada la convertimos a tipo de string a tipo de dato fecha
    date_procesada = datetime.datetime.strptime(date, "%d/%m/%Y").date()

    # guardamos la fehca prosesada en la lista cumpleaños
    cumpleaños.append(date_procesada)


lista_edades = [datetime.date.today().year - fecha.year for fecha in cumpleaños]
print("Los años actuales son: {}".format(lista_edades))

for años in cumpleaños:
    print(años)



