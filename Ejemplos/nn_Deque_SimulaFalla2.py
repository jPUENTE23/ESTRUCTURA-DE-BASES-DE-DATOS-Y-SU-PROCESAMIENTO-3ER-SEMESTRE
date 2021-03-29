import time #Solamente para pausar el despliegue
import collections

switch_general = True
opcion_principal = 0
falla = False
cola_seguridad = collections.deque()

while switch_general:
    print("\n* * *    MENÚ U-N-O    * * *")
    print(f"{'#FALLA ACTIVA#' if falla else ''}")
    print("\n1 .- Captura datos")
    print("2 .- # SIMULAR FALLA #")
    print("3 .- * Recuperarse de la falla *")
    print("4 .- Salir")
    opcion_uno = int(input("\nIndique su elección: "))
    
    if opcion_uno == 1 and not falla:
        nombre = input("Indique su nombre: ")
        while cola_seguridad:
            print()
            print(cola_seguridad.popleft())
            time.sleep(1)
        print(f"\n{nombre.upper()}\n")
    elif opcion_uno == 1 and falla:
        nombre = input("Indique su nombre: ")
        print("¡FALLA DETECTADA! -- Se almacenarán sus datos temporalmente en espera de poder procesarlos\n")
        cola_seguridad.append(nombre.upper())
    elif opcion_uno == 2:
        falla = True
    elif opcion_uno == 3:
        falla = False
    elif opcion_uno == 4:
        switch_general = False
    else:
        print("\n -- OPCIÓN NO VÁLIDA --\n")
 

