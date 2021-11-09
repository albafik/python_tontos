import time                        
import math
import random
import os
                          # FUNCIONES(DEF)
# def triple_del_doble(num):
#     return (num * 2) *3
# res = triple_del_doble(num=int(input("Ingresa un numero: ")))    
# print(res)

# def pantalla_inicio():
    
#     print("***********************************************")
#     print("*                                             *")
#     print("*                  INICIO                     *")
#     print("*                                             *")
#     print("*           Bienvenido al Sistema             *")
#     print("*                                             *")
#     print("***********************************************")
#     return None
# pantalla_inicio()

# def nota_exam(preguntas,aciertos,penalizacion):
#     nota_f = (aciertos * (10 / preguntas)) - (preguntas - aciertos) * penalizacion
#     return nota_f

# question = int(input("Cuantos preguntas tiene el examèm: "))
# correct = int(input("Cuantos aciertos tuvo: "))
# pena = float(input("¿Cual es el valor a restar por cada respuesta incorrecta?: "))
# res = nota_exam(question, correct,pena)
# print(res)

# def intermedio (a,b,c):
#     """"Busca el numero intermedio de una serie de tres"""
#     if a <= b <= c or c <= b <= a:
#             return b
#     elif b <= a <= c or c <= a <= b:
#             return a  
#     elif a <= c <= b or b <= c <= a:
#             return c

                           #Funciones dentro de otras funciones:
# def mayor(a,b):
#     if a > b:
#         return a
#     else:
#         return b    
# def menor(a,b):
#     if a < b:
#         return a
#     else: 
#         return b
# def intermedio (a,b,c):
#    if a < b:
#        m = menor(b,c)
#        n = mayor (m,a)
#        return n
#    else: 
#         d = menor(a,c)
#         s = mayor(d,b)
#         return s    
# print(intermedio(4,8,3))
# print(intermedio(9,3,6))
# print(intermedio(1,2,3))

# def seg_con(segundos):
#     horas = segundos // 60 // 60 # primero divide 60 y se deja solo la parte entera y luego se divide esa parte entera.
#     min = segundos // 60 % 60
#     seg = segundos % 60
#     hora = f"{horas}H,{min}min,{seg}s.  "  
#     return hora
# print(seg_con(4000))


# def valor_absoluto(num):
#     if num > 0:
#         return num
#     else:
#         return - num
# print(valor_absoluto(-54))

# def potencia (num,exp):
#     if exp > 0: 
#         resultado = 1
#         for n in range(exp):
#             resultado *= num
#         return resultado
#     elif exp == 0:
#         return 1
        
# print(potencia(3,3))

# def factorial(numero):
#     if numero > 0:
#         fact = 1
#         for i in range(1, numero +1):
#             fact *= i
         
#     return fact

# print(factorial(4))    
#
    
# def econtrar_primos(inicio, final):
#     primos = []
#     for n in range(inicio, final + 1):
#         contador = 0
#         for i in range(1, n + 1):
#             if n % i == 0:
#                 contador += 1
#         if contador == 2:
#             primos.append(n)    
#     return primos            
   
# def factores_primos(num):
#     factor_pri = []
#     for i in range(2, num + 1):
#         while num % i == 0:
#           factor_pri.append(i)
#           num = num / i
#     return factor_pri

# def multiplos(n):
#     multi = []
#     for i in range (1,10):
#         num = n * i
#         multi.append(num)
#     return multi

# print(multiplos(7))

# def divisor(n):
#     divisor = []
#     for i in range(1,n + 1):
#         if n % i == 0:
#             divisor.append(i)
#     return divisor

# print(divisor(30))     
#

# def conjetura_collatz(num):
#     secuencia = [num]
#     while num > 1:
#        if num % 2 == 0:
#           num //= 2
#        else:
#           num = num * 3 + 1
#        secuencia.append(num)
#     return secuencia

# n = conjetura_collatz(11)
# for i in n:
#     print(f"{i} ",end="")       


