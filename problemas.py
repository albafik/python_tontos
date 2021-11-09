#                           import (modulos)
# math.sqrt(raiz cuadrada)
import math
import random
import time
import itertools
# a = float(input("Ingresa el valor del cateto: "))
# b = float(input("Ingresa el valor del cateto: "))
# c = math.sqrt(a**2 + b**2)
# print(f"El valor de la hipotenusa es {c} ")

# Elipse
# r = float(input("Ingresa un valor : "))
# s = float(input("Ingresa un valor: "))


# perimetro_de_elipse = 2 * math.pi * math.sqrt((r ** 2 + s ** 2)/2)
# print(perimetro_de_elipse)


# inicio = time.time()
# for i in range(21):
#     print(20 - i / 2)
#     time.sleep(0.5)  
# final = time.time()
# print(f"Tiempo es: {final - inicio - 0.5} ")


# colores = ["azul", "amarillo", "rojo", "blanco", "violeta", "negro", "plateado", "dorado","marron","rosa"]
# while True:
#     muestra = random.sample(colores, 4)
#     print("Memoriza los colores en 3")
#     time.sleep(1)
#     print("-------2-------")
#     time.sleep(1)
#     print("------------1---------")
#     time.sleep(1)
#     for i in range(len(muestra)):
#         print("", muestra[i], end="" )
   

# cadena = "Estaba alli. Era un pajara, en la ventana. Pero entonces, de repente, se echo a volar."  
# palabras = cadena.split()
# for i in palabras:
#     ma = i.strip(".")
#     n = ma.strip(",")
#     print(n)


# mayor = None
# for i in range(7):
#     n = int(input("Ingresa un num: "))
#     if mayor is None or n > mayor:
#         mayor = n
# print(f"El num mayor es {mayor}")


# jugadores = ["1. Jugador A,\n2. Jugador B, \n3. Jugador C "]
# jugador1 = None
# jugador2 = None
# jugador3 = None
# while jugador1 is None or jugador2 is None or jugador3 is None:

                   # FUNCIONES DE LAS LISTAS
# nums = [1,5,8,4,7,2,9]
# num_copy = list(nums)  o reverso = nums[:::-1]
# num_copy.reverse()
# print(num_copy)

                  # BUCLES ANIDADOS FOR

# for n in range(2, 8):
#     print(f"La tabla de {n}")
#     for m in range(1,13):
#         operation = n * m
#         print(f" {n} * {m} = {operation} ",end="")
#     print() 
#    
# COMBINACION:    
# for m in range(10):
#     for n in range(10):
#         for l in range(10):
#             posible_clave = str(m) + str(n) + str(l)
#             print(f"La lista de claves posibles: {posible_clave}")
#         print()    

# lista = ["Tomas", "Maria", "Laura", "Miguel", "Carlos"]
# for elemento in lista:
#     for i in range(1,5):
#         print(f" {elemento} quedo en la posicion {i}", end="" )
#     print()    

# nums = [2,3,5,1,4,3,6,7,9,5,8]
# repetidos = []
# archivo = []
# for i in nums:
#     if i not in archivo:
#         archivo.append(i)
#     else:
#         repetidos.append(i)
# print(repetidos)

# numeros = [2,3,5,8,4,7,6,1]
# parejas = []

# for n in numeros:
#     if 10 - n in numeros:
#         pareja = sorted([n, 10-n])
#         if pareja not in parejas:
#             parejas.append(pareja)

# print(parejas)