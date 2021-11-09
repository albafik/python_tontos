import random
from ahorcado_diagrama import vidas_diccionario_visual as estructura
from palabras import palabras 
# velador = [[[["A",8], ["B",5], ["C", 0], ["D", 2], ["E", 8]], [["F",7], ["G",3], ["H",4], ["I", 5], ["J", 6] ], [["K",1], ["L",3], ["M",9], ["N", 12], ["Ñ", 1] ]], [[["O",8], ["P",5], ["Q", 0], ["R", 2], ["S", 8]], [["T",7], ["U",3], ["V",4], ["W", 5], ["X", 6] ], [["Y",1], ["Z",3], ["",0], ["",0 ], ["",0 ] ]]]

# while True:
#     print()
#     print("1 Mostra Inventario")
#     print("2 Ventas de letras")
#     print("3 Reposicion de letra")
#     print("4 Salir.")
#     print()

#     opcion = int(input("Ingresa  el numero:  "))
#     print()
#     if opcion == 1:
#         print("Inventario de ventas".center)
#         for cajon in velador:
#             for fila in cajon:
#                 for espcio in fila:
#                     print(f"{espcio}  ",end="")
#                 print()    
#             print()
#     elif opcion == 2:
#         letra = input("Introduce una letra: ").upper()
#         cantidad = int(input("Introduce la cantidad: "))
#         for cajon in velador:
#             for fila in cajon:
#                 for espcio in fila: 
#                     if espcio[0] == letra:
#                         espcio[1] -= cantidad 
#     elif opcion == 3:
#         letra = input("Introduce una letra: ").upper()
#         cantidad = int(input("Introduce la cantidad: "))
#         for cajon in velador:
#             for fila in cajon:
#                 for espcio in fila:
#                     if espcio[0] == letra:
#                         espcio[1] += cantidad
#     elif opcion == 4:
#         break
#     else:
#         print("Opcion incorrecta") 
#                    
#  CONVERTIR A LISTA PLANA DE ANIDADA:
# datos = [[1,2,3],[4,5,6],[7,8,9]]
# planos = []
# for lista in datos:
#     for elemento in lista:
#         planos.append(elemento)
# print(planos)

# datos = [[1,2,3],4, 5, [6,7], 8, 9]
# plana = []
# for dato in datos:
#     if type(dato) == int:
#         plana.append(dato)
#     elif type(dato) == list:
#         for elemeto in dato:
#             plana.append(elemeto)
# print(plana)            

# se salto un elemento la lista por las condiciones for
# meses = ["enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre"]
# copia_meses = list(meses)
# for mes in copia_meses:
#      if "b" in mes:
#         meses.remove(mes)
# print(meses)

# cadena = "Hoy hace un dia estupendo."
# reverso = ""
# for i in range(len(cadena)):
#     reverso += cadena[-i-1]

# print(reverso)


  


















