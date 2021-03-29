'''
Implementación de colas mediante listas y deque()
Demuestra las diferencias en la forma de implementación

'''
SEPARADOR = ("*" * 20) + "\n"

cola = list()   #Cola utilizando una lista

for cantidad in range(5):
    nuevo = input("Nombre del recién llegado: ")
    cola.append(nuevo)

print(f"Se agregaron {len(cola)}, elementos:")
for elemento in cola:
    print(elemento)
print(SEPARADOR)
pass   #Hacer notar que los elementos permanecen en la cola

print("Procedemos a retirarlos de la cola")
while cola:
    print(cola.pop(0))
pass   #Verificar que la estructura se encuentra vacia

