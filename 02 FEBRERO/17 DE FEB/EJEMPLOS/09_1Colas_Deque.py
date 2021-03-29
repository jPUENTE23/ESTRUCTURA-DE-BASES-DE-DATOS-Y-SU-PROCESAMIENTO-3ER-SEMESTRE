'''
Implementación de colas mediante deque()
Demuestra las diferencias en la forma de implementación

'''
SEPARADOR = ("*" * 20) + "\n"
import collections

cola = collections.deque()   #Cola utilizando deque

for cantidad in range(5):
    nuevo = input("Nombre del recién llegado: ")
    cola.append(nuevo)

print(f"Se agregaron {len(cola)}, elementos:")
for elemento in cola:
    print(elemento)
print(SEPARADOR)
pass   #Hacer notar que los elementos permanecen en la cola

# el siguiente procediemiento nos ayuda a retirar el elemento de una lista
# que se se encuentra del lado izquierdo
print("Procedemos a retirarlos de la cola")
while cola:
    print(cola.popleft())
pass   #Verificar que la estructura se encuentra vacia

print(cola)
