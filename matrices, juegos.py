# consumo = [[21, 18, 35, 40],[19, 11, 21, 14], [12, 15, 20, 30]]

# for lista in consumo:
#     print("[", end=" ")
#     for elemento in lista:
#         print(f"{elemento:8.2f}", end=" ")
#     print("]")

# matriz_cero = []

# for i in range(10):
#     matriz_cero.append([0] * 15)

# matriz_cero[2][3] = 2
# print(matriz_cero)

                     # RELLENAR UNA MATRIZ
# filas = int(input("Introduce un numero de filas: "))
# columnas = int(input("introduce el número de columnas: "))

# matriz = []
# for i in range(filas):
#     matriz.append([])
#     for j in range(columnas):
#         valor = float(input("Fila {}, columna {} : ".format(i + 1, j + 1)))
#         matriz[i].append(valor)

# print()
# for fila in matriz:
#     print("[", end=" " )
#     for elemento in fila:
#         print(f" {elemento:8.2f} ", end="")
#     print("]") 
# print()   
                                   # SUMA DE MATRIZ

# a = [
# [21, 18, 35, 40], 
# [19, 11, 21, 14], 
# [12, 15, 20, 30]]
# b = [
#     [11, 7, 21, 32],
#     [9, 15, 24, 10],
#     [23, 8, 12, 22]
# ]                                  

# def sumar_matriz(m1,m2):
#     if len(m1) == len(m2) and  len(m1[0]) == len(m2[0]):
#         m3 = []
#         for i in range(len(m1)):
#             m3.append([])
#             for j in range(len(m1[0])):
#                 m3[i].append(m1[i][j] + m2[i][j])
#         return m3
#     else:
#         return None

# c = sumar_matriz(a, b)
# if c == None:
#     print("No se puede sumar.")
# else:
#     for fila in c:
#         print("[", end=" ")  
#         for elemento in fila:
#             print(elemento, end=" ")
#         print("]")      
                              # MULTIPLICACION DE MATRICES

# a = [
#     [1, 2, 3],
#     [4, 5, 6]
# ]
# b = [
#     [1, 2],
#     [3, 4],
#     [5, 6]
# ]

# def multiplicar_matrices(m1, m2):
#     if len(m1[0]) == len(m2):
#         m3 = []
#         for i in range(len(m1)):
#             m3.append([])
#             for j in range(len(m2[0])):
#                 m3[i].append(0)

#         for i in range(len(m1)):
#             for j in range(len(m2[0])):
#                 for k in range(len(m1[0])):
#                     m3[i][j] += m1[i][k] * m2[k][j]
#         return m3
#     else:
#         return None    

# c = multiplicar_matrices(a,b)                    
# if c == None:
#     print("No se puede multiplicar.")
# else:
#     for fila in c:
#         print("[", end=" ")
#         for elemento in fila:
#             print(elemento, end=" ") 
#         print("]")        

                            # Transpuesta de una matriz
# matriz = [[1, 2, 3], [4, 5, 6]]

# def trasponer(m):
#     t = []
#     for i in range(len(m[0])):
#         t.append([])
#         for j in range(len(m)):
#             t[i].append(m[j][i])
#     return t

# traspueta = trasponer(matriz)


