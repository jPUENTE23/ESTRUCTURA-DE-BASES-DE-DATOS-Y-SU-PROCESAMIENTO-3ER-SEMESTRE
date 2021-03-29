import random

loteria = ["El borracho","El gallo","La botella","La sirena", "La escalera",
"El valiente","El diablo","El catrin","El paraguas","El barril","El arbol",
"El melon","El gorrito","La muerte","La pera"]

random.shuffle(loteria)

for i in loteria:
    print("Baraja {}".format(i))
    gano = int(input("Ya ganaronn? (1:si 2:no): "))
    if gano == 1:
        print("FELIZIDADES AH GANADO")
        break
else:
    print("FIN DEL JUEGO")





