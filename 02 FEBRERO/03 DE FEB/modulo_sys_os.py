
# el modulo sys nos ayuda a ver cuanto pesa o cuantos bytes nos consume un lista
import sys
import os

numeros = list()
for numero in range (1,10+1):
    numeros.append(numero)

print(numeros)
# este objeto guarda la cantidad de elmentos que tiene nuestra lista
cantidad = len(numeros)

# este objeto nos guarda el tamaño en bytes de nuestra lista anterior
# sys.getsizeof es la funcion que nos ayuda a calcular el tamaño
bits = sys.getsizeof(numeros)
print("La liste tiene {} elementos y tiene un tamañpo de {} bytes ".format(cantidad,bits))


# con el mismo procedimiento que el anterior solo que ahota con el uso de una tupla
# verificamos que una tuplan tiene menos tamaños en bytes que una lista
_numeros = tuple(numeros)
_cant = len(_numeros)
_bit = sys.getsizeof(_numeros)
print("La tupla tiene {} elementos y tiene un tamañpo de {} bytes ".format(_cant,_bit))

# uso del modulo os
# la funcion os.getcwd no ayuda a ver cual es el directorio de nuestro archivos
print("El directorio actual del trabajo es {} ".format(os.getcwd()))


# el metodo os.walk lo que hace es recorrer un directorio
# topdown=false nos ayuda a en que sentido se recorre el directorio
for raiz, dirs, archivos in os.walk(".", topdown=True):
    for nombre in archivos:
        print(os.path.join(raiz,nombre))
    for nombre in dirs:
        print(os.path.join(raiz,nombre))
