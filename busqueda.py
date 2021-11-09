import random
import time
my_list = [21,2,4,22,3,5,8,9,20]
my_list.sort()

def busqueda_ingenua(lista,objetivo):
    for i in  range(len(lista)):
        #range(len(list))= 0,1,2,3,4....
        if lista[i] == objetivo:
            return i 
    return -1

def busqueda_binaria(lista, objetivo, limite_inferio=None, limite_superior=None):
    if limite_inferio is None:
        limite_inferio = 0
    if limite_superior is None:
        limite_superior = len(lista)-1#Final de la lista ultimo elemeto

    if limite_superior < limite_inferio: 
        return -1   

    punto_medio = (limite_superior + limite_inferio) // 2  

    if lista[punto_medio] == objetivo:
        return punto_medio
    elif objetivo < lista[punto_medio]:
        return busqueda_binaria(lista, objetivo, limite_inferio, punto_medio - 1)
    else: 
        return busqueda_binaria(lista, objetivo, punto_medio + 1, limite_superior)

busqueda_binaria(my_list, 2)
