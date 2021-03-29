import pandas as pd
import numpy as np


diccionario = {10:[[['jorge',10,20],['david',10,14]]]}

lista = diccionario[10][0]
print(lista)

df = pd.DataFrame(lista, columns=['Nombre','Edad','Precio'])

print(df)
