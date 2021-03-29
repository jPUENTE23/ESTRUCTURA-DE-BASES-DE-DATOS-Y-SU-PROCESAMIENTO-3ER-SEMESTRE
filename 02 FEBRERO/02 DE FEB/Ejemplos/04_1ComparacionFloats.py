import math

def imprime_separador():
    print("")
    print("*" * 30)
    print("")


#Función para comparación de dos datos float
def floats_iguales(a, b, tolerancia):
    return a == b or math.fabs(a-b) < tolerancia #fabs requiere la importación de math

float1 = 1.0003
float2 = 1.0030

#Comparación de floats con tolerancia
print(floats_iguales(float1, float2, 0.01))   
pass
