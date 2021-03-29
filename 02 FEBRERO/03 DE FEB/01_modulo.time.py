
# importamos el modulo time
import time

segundos = int(input("Cantidad de segundos a esperar: "))

# esta funcion no ayuda a que el progrma se detendra de acuerdo a los segundos
# que usuario haya indicado
# solo acepta argumentos de numeros enteros
time.sleep(segundos)
print("Han transcurrido {} segudnos de espera".format(segundos))


print("Iniciamos la medision de un proceso simulado")

# la funcion time.time nos ayuda capturar la hora deacuerdo a nuestro equipo
horaInicial = time.time()

# el proceso simulado ejecutara los segundos antes ingresados
# deacuerdo a los segundos los acumulara al rango dentreo del argumento del for
# Ejemplo: 3 seg * 10 que es nuetro rango en el argumento = 30 seg
for termino in range (10):
    time.sleep(segundos)

print("Proceso simulado concluido")

# ya capturamos la hora inicial anterior mente, se la restaremos deacuerdo ah la hora capturado del equipo
# una vez que haya terminado la simulacion, asi obtenemos el tiempo de diferencia
duracion = time.time() - horaInicial
print("La duracion de proceso simulado fue de {} segundos".format(duracion))

#print(type(duracion))