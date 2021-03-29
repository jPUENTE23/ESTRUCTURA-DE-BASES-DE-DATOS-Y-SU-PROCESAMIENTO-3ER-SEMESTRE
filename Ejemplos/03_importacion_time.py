'''
Ejemplo para ilustrar la importación de la librería time en Python 3
Demuestra el uso de: sleep(x), time()
'''
import time
SEPARADOR = ("*" * 20) + "\n"

segundos = int(input("Cantidad de segundos a esperar:\n"))
time.sleep(segundos)    #Espera por lo menos la cantidad de segundos especificada
print(f"Han transcurrido, por lo menos, {segundos} segundos")
print(SEPARADOR * 2)

print("Iniciaremos la medición de un proceso simulado")

horaInicial = time.time()

for termino in range(10):
    time.sleep(segundos)

print("proceso simulado concluído!")
duracion = time.time() - horaInicial    #Puede verse afectado si se cambia la hora del sistema
print(f"La duración del proceso simulado fue de {duracion} segundos")
