lista = [0,88, 72, 23, 14, 16, 90, 47,35, 6, 12, 10, 54, 41 ]
lista.sort()
print(lista)

 #1ro buscar el punto medio
 #2do comprobar si el punto medio es el valor que buscamos
 #3ro si el numero es menor al valor que buscamos aumentamos inico 1 sobre el puntero
 #4to si el número es menor al valor que buscamos disminuinos  el final 1 bajo el puntero
#5to si el inicio es mayor o igual que el final entonces el valor no se encuentra en la lista
def busqueda_binaria(valor):
    inicio = 0
    final = len(lista) - 1
    while inicio <= final :
        puntero = (inicio + final) // 2
        if valor == lista[puntero]:
            return puntero
        elif valor > lista[puntero]:
            inicio = puntero + 1
        else:
            final = puntero - 1  
    return None               

def buscar_valor(valor):
    res_busqueda = busqueda_binaria(valor)
    if res_busqueda is None:
        return f"el numero {valor } no se encontró "
    else:
        return f"el numero {valor} se encuentra en la posicion {res_busqueda} "    

print(buscar_valor(16))
