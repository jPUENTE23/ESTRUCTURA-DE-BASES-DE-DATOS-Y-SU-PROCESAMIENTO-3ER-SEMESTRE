import csv

columnas = ("clave", "nombre", "correo")
datos = [[1, "Rodimiro", "rod@gmail.com"],
        [2, "Téofilo", None],
        [3, "Leonardo", "domi@algo.com"]]



with open("datos.csv", "w", newline="") as archivo:
    registrador = csv.writer(archivo)
    registrador.writerow(columnas)
#     for registro in datos:
#         registrador.writerow(registro)
    registrador.writerows(datos)



columnas = None
datos = list()



with open("datos.csv", "r") as archivo:
    lector = csv.reader(archivo, delimiter = ",")
    registros = 0
    
    for clave, nombre, correo in lector:
        if registros == 0:
             columnas = (clave, nombre, correo)
             registros = registros + 1
        else:
            clave = int(clave)
            datos.append([clave, nombre, correo])

print(datos)






#Codificar una variación al almacenamiento en CSV de la lista de listas
#En esta variación al iniciar la ejecución del script se debe validar la existencia
#previa del archivo de datos .csv (os, pathlib).
#Si el archivo ya existe, se deben cargar los datos previos del mismo.
#Realizar la captura de los datos a agregar y almacenarlos en el archivo de datos












