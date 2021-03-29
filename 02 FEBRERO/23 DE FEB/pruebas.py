
import re

diccionario = {
    10:[2036366,'jorge'],
    11:[2036368,'david']
}


for termino in diccionario:
    print(termino,"   ",diccionario[termino])


print("[", end="")
for dato in diccionario[termino]:
    print(f"{termino} -- {dato}",end="\t")
print("]")
print("")