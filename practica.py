# split(""): separa las lista con "elemento asignado" tambien convierte una str a list
# num = 1
#sumar numeros en secuencia
# num = 1
# suma = 0
# while num <= 10:
#     suma += num
#     num +=1

# print(f"resultado es {suma}")


# num_inicio = int(input("Ingresa el numero de inicio: "))
# num_final = int(input("Ingresa el numero del final"))
# suma = 0
 
# while num_inicio <= num_final:
#     if num_inicio % 3 == 0:
#         suma += num_inicio
#     num_inicio += 1
# print(f"EL resultado es {suma}")

# adivina_n = "4"
# adivina_v = "i"
# puntos = 100
# jugando = True

# while jugando:
#     numero = input("Ingresa un numero del 1 al 5: ") 
#     vocal = input("Ingresa un vocal: ")
#     if adivina_n == numero and adivina_v == vocal:
#         print("Acertaste felicitaciones")
#         break
#     else: 
#         if adivina_n != numero and adivina_v != vocal: 
#             puntos -= 5
#             print(f"Fallaste te quedan {puntos} puntos") 
        
#         elif (adivina_v != vocal or adivina_n != numero) :
#             puntos -= 2
#             print(f"Fallaste te quedan {puntos} puntos")

# cadena = "Muchos años despues, frente al peloton de fusilamiento , el coronel Aureliano Buendia habia de recordar tarde remota en que se padre lo llevo a conocer el hielo."        
# n = 0
# longitud = len(cadena)
# veces = 0
            
# while n <= longitud - 1:
#     if cadena[n] == "o" or cadena[n] == "ó":
#         veces += 1
#     n += 1
# print(f"las VECES QUE APARECE O ES {veces} ")
# SE Necesita una variable 0 para que recora en cada posicion del str hasta completar la longitud -1

                           #TUPLAS() Y LISTAS[]
# animales = ("oso", "perro", "gato")

#Concatenacion de listas
# lista = []
# indice = 1

# while indice <= 100:
#     lista.append(indice)
#     indice += 1

# print(lista)

# color = input("Ingresa un color: ")
# colores =("rojo", "amarillo", "verde", "azul", "violeta")
# puntos = 0
# while color in colores:
#     puntos += 1
#     print(f"Has acertado el color {color} , has ganado un {puntos} puntos")
#     color = input("Ingresa otro color: ")
# else:
#     print(f"Lo siento el color {color} es incorrecto has obtenido un total de {puntos} puntos ")         

                       #FOR

# suma = 0
# for i in range(5):
#     num = float(input("Ingresa otro numero: "))
#     suma += num
# print(suma)

# lista = [2,5,90,23,45,87,54,11,38]
# elemento = 54

# for i in range(len(lista)):
#     if lista[i] == elemento:
#         print(f"el elemento {elemento} se encuentra en la posicion {i+1} ")

# numero = int(input("Ingresa un numero: "))

# for i in range(12):
#     if numero != 0:
#         tabla = numero * i
#         print(f"La tabla del {numero} es: {numero} x {i} = {tabla} ")

# palabras = "zanahoria"

# for i in palabras:
#     if i != "h":
#         print(i)
#     else: 
#         continue    
                              