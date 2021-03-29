
import csv

switch = True
tabla = list()
respuesta = 1

while switch:
    print("{1}. Agregar Registro")
    print("{2}. Consultar Registro")
    print("{3}. Consultar Tabla")
    print("{4}. Salir")
    opcion = int(input("Opcion: "))
    if opcion == 1:
        while respuesta == 1:
           clave = int(input("Ingrese una clabe a regitrar: "))
           nombre = input ("\nDime el nombre a capturar: ")
           correo_electronico = input("Dime el correo electronico a capturar: ")
           tabla.append([clave, nombre, correo_electronico])
           columna = ('Clave', 'Nombre', 'Correo Electronico')
           with open("datos.csv", "a+", newline="") as archivo:
                 registrador = csv.writer(archivo)
                 registrador.writerow(columna)
                 registrador.writerows(tabla)

           respuesta = int(input("\n ¿Deseas capturar otro registro? \n(1-Si / 0-No): "))

    elif opcion == 2:
        nombre_buscar = input("Dime qué nombre deseas consultar: ")
        for registro in tabla:
           if registro[0] == nombre_buscar:
                print(registro)
                break
        else:
             print("Lo siento, ese nombre no fue capturado")

    elif opcion == 3:
        for regis in tabla:
            print(regis)

    elif opcion == 4:
        switch = False
