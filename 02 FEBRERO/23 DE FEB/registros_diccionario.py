diccionario = {}
switch = True
respuesta = 1
lista_Datoa = list()
tabla = list()

while switch:
    print("{1}. Agregar Registro")
    print("{2}. Consultar Registro")
    print("{3}. Consultar Tabla")
    print("{4}. Salir")
    opcion = int(input("Opcion: "))
    if opcion == 1:
        while respuesta == 1:
            while True:
               llave = int(input("Ingrese la llave de los dato a registar: "))
               if llave in diccionario.keys():
                    print("La llave ya existe en el diccionario  ")
               else:
                    nombre = input("Dime el nombre a registrar: ")
                    correo_electronico = input("Dime el correo electronico a capturar: ")
                    diccionario[llave] = [nombre,correo_electronico]

                    respuesta = int(input("\n ¿Deseas capturar otro registro?\n(1-Si / 0-No): "))
                    break

    elif opcion == 2:
        llave_buscar = int(input("Ingrse la llave que desea consultar: "))
        if llave_buscar in diccionario.keys():
            print("Llave: {} .Datos registrados: {}".format(llave_buscar,diccionario[llave_buscar]))
        else:
            print("La llave no se encuentra registrada")

    elif opcion == 3:
        for dato in diccionario:
            print(diccionario[dato])

    elif opcion == 4:
        switch = False



