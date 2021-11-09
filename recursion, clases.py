# def cuenta_atras2(n):
#     if n < 0:
#         print("Fin")
#     else:
#         print(n)
#         cuenta_atras2(n - 1)    

# cuenta_atras2(10)

# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n - 1)

# print(factorial(5))


# def potencia(base,exp):
#     if exp == 0:
#         return 1
#     else:  
#         return base * potencia(base, exp - 1)

# print(potencia(5,4))

# lista = [1, 2, 3, 4, 5]

# def sumar_lista(l):
#     if l == []:
#         suma = 0
#     else:
#         suma = l[0] + sumar_lista(l[1:])
#     return suma

# print(sumar_lista(lista))    

# lista = [1, 2, 3, 4, 5]

# def inversion_l(lis):
#     if lis == []:
#         inversa = lis
#     else:
#         inversa = [lis[-1]] + inversion_l(lis[:-1])
#     return inversa
          
# print(inversion_l(lista))



                       # ejemplo practico
# datos = [[1,2], [[3,4], [[[5,6],[7,8],[9,10]]], [11,12]]]

# def aplanar_lista(lista):
#     plana = []
#     for elemento in lista:
#         if type(elemento) == int:
#             plana.append(elemento)
#         else:
#             plana = plana + aplanar_lista(elemento)
#     return plana

# print(aplanar_lista(datos))

# lista = [3, 5, 7, 9, 11]
# def imprimir_lista(lis, indice=0 ):
#     if indice != len(lis):
#         print(lis[indice])
#         imprimir_lista(lis, indice+1)


# def crear_lista(n, a=[]):
#     if n < 0:
#         return a
#     else:gir
#         a.append(n)
#         return crear_lista(n - 1, a)
# print(crear_lista(9))

def lista_cuadrados(n, m):
    if n > m:
        return []
    else:
        return [n ** 2] + lista_cuadrados(n + 1, m)

print(lista_cuadrados(3,7))
   