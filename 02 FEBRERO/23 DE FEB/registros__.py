
import re

def separador():
    print("-"*40) + "\n"

diccionario = {}
switch = True
respuesta = 1

while switch:
    # menu
    print("{1}. Agregar Registro")
    print("{2}. Consultar Registro")
    print("{3}. Consultar Tabla")
    print("{4}. Salir")
    opcion = int(input("Opcion: "))
    if opcion == 1:
           while respuesta == 1:
               while True:
                   matricula = int(input("Ingrese la matricula del alumno: "))
                   for termino in diccionario:
                       if diccionario[termino][2] == matricula:
                           print("La mtricula ya esta registrada")
                           print(diccionario[termino])
                           break
                           # si la matricula ya existe, mostrara las matriculas que
                           # ya se encuentarn registradas y le volveremos a preguntar al usuario
                   else:
                       # si la matricula no existe, procedemos a guardar los otros datos
                       if diccionario:
                          clave = max(diccionario) + 1
                          nombre = input("Ingrese el nombre a registrar: ")
                          correo = input("Ingrese el correo a registrar: ")
                          diccionario[clave] = [nombre, correo, matricula]

                          respuesta = int(input("\n ¿Deseas capturar otro registro?\n(1-Si / 0-No): "))
                          break
                       else:
                          clave = 1
                          nombre = input("Ingrese el nombre a registrar: ")
                          correo = input("Ingrese el correo a registrar: ")
                          diccionario[clave] = [nombre, correo, matricula]

                          respuesta = int(input("\n ¿Deseas capturar otro registro?\n(1-Si / 0-No): "))
                          break

    elif opcion == 2:
        buscar_clave = int(input("Ingrese la clave a buscar: "))
        if buscar_clave in diccionario.keys():
            print(diccionario[buscar_clave])

    elif opcion == 3:
        for termino in diccionario:
            print("{} {}".format(termino,diccionario[termino]))

    elif opcion == 4:
        switch = False


