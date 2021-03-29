'''
Demostración de implementación de pilas utilizando listas y con deques
'''
import collections
SEPARADOR = ("*" * 20) + "\n"

pila_con_lista = list()
for i in range(5):
    pila_con_lista.append(input("Dime el nombre a agregar: "))

#Sacar elementos de la pila
while pila_con_lista:
    print(pila_con_lista.pop())
print(SEPARADOR)








pila_deque = collections.deque()
for i in range(5):
    pila_deque.append(input("Dime el nombre a agregar: "))

#Sacar elementos de la pila
while pila_deque:
    print(pila_deque.pop())
pass