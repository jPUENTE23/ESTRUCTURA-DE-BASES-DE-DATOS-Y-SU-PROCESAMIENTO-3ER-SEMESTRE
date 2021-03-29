tabla = []
respuesta = 1
nombre = ""
correo_electronico = ""


while respuesta == 1:
    registro = []
    nombre = input ("\nDime el nombre a capturar: ")
    correo_electronico = input("Dime el correo electronico a capturar: ")
    registro.append(nombre)
    registro.append(correo_electronico)
    tabla.append(registro)

    respuesta = int(input("\n ¿Deseas capturar otro registro? \n(1-Si / 0-No): "))

nombre_buscar = input("Dime qué nombre deseas consultar: ")
for registro in tabla:
    if registro[0] == nombre_buscar:
        print(registro)
        break
else:
    print("Lo siento, ese nombre no fue capturado")