
#import numpy as np
import pandas as pd # importacion de la libreria pandas
import random

# creacion de un dataframe a partir de un diccionario

diccionario_notas_aleatorias = {
    "Crescencio":[random.randrange(60,101) for x in range (3)],
    "Domitila":[60,100,57],
    "Domitila":[100,70,97],
    "Domitila":[40,95,75],
    "Domitila":[60,100,87],
}


lista = [[10,"hola"],[20,"adios"]]
# guardar diiccionario en un dataframe

#_notas = pd.DataFrame(lista)
notas = pd.DataFrame(diccionario_notas_aleatorias)
notas.index = ["Programacion","Base de Datos","Contabilidad"] # Damos nombre a las filas de un data frame
print(notas)

# guardar dataframe en un csv
notas.to_csv('notas.csv',index=True,header=True)

