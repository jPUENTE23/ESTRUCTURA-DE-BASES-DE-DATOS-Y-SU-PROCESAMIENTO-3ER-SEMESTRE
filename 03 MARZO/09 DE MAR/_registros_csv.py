import csv
import os


respuesta = 1
tabla = list()
doc = "registros.csv"


while respuesta:
    clave = int(input("INgresa una clave a ingresar: "))
    nombre = input("Ingresa el nombre a registrar: ")
    correo = input("Ingresa el correo a registrar: ")
    tabla.append([clave, nombre, correo])
    columna = ('Clave', 'Nombre', 'Correo Electronico')

    respuesta = int(input("\n ¿Deseas capturar otro registro? \n(1-Si / 0-No): "))

    with open("registros.csv", "a+", newline="") as archivo:
        registrador = csv.writer(archivo)
        registrador.writerows(tabla)

    '''else:
        with open("registros.csv", "w", newline="") as archivo:
            registrador = csv.writer(archivo)
            registrador.writerow(columna)
            registrador.writerows(tabla)

        tabla = {}
        respuesta = int(input("\n ¿Deseas capturar otro registro? \n(1-Si / 0-No): "))'''
