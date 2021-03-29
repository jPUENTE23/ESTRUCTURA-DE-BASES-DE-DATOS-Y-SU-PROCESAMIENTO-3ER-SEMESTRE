'''
- Es una lista de pares de elementos con estructura clave:valor
- No se accesa a los elementos por posición, sino por el valor de su clave
- La clave puede ser de cualquier tipo inmutable (boolean, integer, string, etc.)
- Se delimita entre llaves { }
- A un diccionario se le refiere también como dict
'''

#Creación de diccionarios
diccionario_vacio = {}
diccionario_citas = {"T'Challa":"Wakanda Forever",
                     "Thanos":"The hardest choices require the strongest wills",
                     "AMLO":"Me canso ganso"}
print(diccionario_citas)
pass


#Accesar elementos
print(diccionario_citas["Thanos"])
pass


#Agregar elementos: Se agrega la nueva llave y se indica su valor
print("*" * 20)
diccionario_citas["Plankton"] = "¡Por fin tengo la fórmula de la cangreburger"
print(diccionario_citas)
pass


#Eliminar elementos de un diccionario
print("*" * 20)
del diccionario_citas["AMLO"]
print(diccionario_citas)
pass

#Opciones para obtener el volcado de un diccionario,
#en cada una, la respuesta DEBE convertirse a una lista primero
#para un más fácil manejo

#Opción 1 : Todas las claves, solamente las claves
print(list(diccionario_citas.keys()))
pass


#Opción 2 : Todos los valores, solamente los valores
print(list(diccionario_citas.values()))
pass


#Opción 3 : Todos los elementos, elemento por elemento
print(list(diccionario_citas.items()))