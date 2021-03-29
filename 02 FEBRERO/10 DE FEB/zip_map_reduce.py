
'''
Ejemplo para demostar el manejo de agregado sobre iterables
Demuestra: zip(), map(), reduce(), accumulate()
'''
import functools
import itertools

def al_doble(valor1):
    return valor1 + valor1
def sumar_doc(valor1, valor2):
    return valor1 + valor2

# demostracion de la funcion zip para combinar dos iterables iterables
lista = [1,2,3,4,5,6,]
lista_letras = ["a","e","i","o","u"]
print(lista)
print(lista_letras)
resultado_conbinado = zip(lista,lista_letras)

print("El tipo de objeto resultado conbinado es : {}" .format(resultado_conbinado))
print("El resultado conbinado es {}".format(list(resultado_conbinado)))

# desmostracion de la funcion map para procesar cada elemento de la lista
numeros_al_doble = list(map(al_doble,lista))
print("El doble de cada elemento de la lista original {} ".format(numeros_al_doble))

# demostracion de la funcion reduce() y accumulate() para agregar elementos de una lista
print("La lista de numeros es {}".format (lista))

# reduce()
print("El agregado de la lista mediante reduce() es {}".format(functools.reduce(sumar_doc, lista)))

# accumulate()
print("El agregado de la lista mediente accumulate() es {}".format(list(itertools.accumulate(lista,sumar_doc))))

