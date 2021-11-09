import math
import time
import random
# intentos = 0
# while True:    
#     try:
#        numero = int(input("Introduce tu edad: "))
#     except ValueError:
#         intentos += 1
#         if intentos < 3:
#             print("No has introducido un numero entero.")
#         else:
#             print("Salimos de programa")
#             break    
#     else:    
#        if numero > 18:
#         print("Eres mayor de edad.")
#        else:
#         print("Eres menor de edad.")
#         break    
   
# try:
#     dividendo = float(input("Introduce el dividendo: "))
#     divisor = float(input("Introduce el divisor: "))

#     resultado = dividendo / divisor
# except ValueError:
#     print("No as introducido datos correctos.")
# except ZeroDivisionError:
#     print("No se puede dividir para cero.")
# else:
#     print(resultado)     

# try:
#     numero = float(input("Introduce un número: "))
#     resultado = math.sqrt(numero)
# except ValueError:
#     print("Datos incorrectos, ten encuenta que no se puede sacar raiz cero o negativa. ")

# else:
#     print(f"Raiz cuadrada de : {numero} es {resultado}")      

# suma de gaus ALGORITMO CONSTANTE.
# def suma_constante(n):
#     suma = (n / 2) * (n + 1)
#     return suma




# lista = [2, 3, 5, 6, 8, 11, 12, 15, 17, 18, 21, 23, 24, 29, 30]
# buscado = 22

# def busqueda_binaria(lista, elemento):
#     inicio = 0
#     final = len(lista) - 1 
#     while inicio <= final :   
#        medio = (inicio + final) // 2
#        if lista[medio] < elemento:
#           inicio = medio + 1
#        elif lista[medio] > elemento:
#           final = medio - 1
#        else:
#           return True    
#     return False

# print(busqueda_binaria(lista, buscado))

# datos = []
# for i in range(15000):
#     datos.append(i)


# def busqueda_binaria(lista, elemento):
#     pasos = 0
#     inicio = 0
#     final = len(lista) - 1 
#     while inicio <= final : 
#        pasos += 1  
#        medio = (inicio + final) // 2
#        if lista[medio] < elemento:
#           inicio = medio + 1
#        elif lista[medio] > elemento:
#           final = medio - 1
#        else:
#           return True , pasos   
#     return False


# print(busqueda_binaria(datos,12347),)


censo = []
alfabeto = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
numero = 0
print("Creando censo......")


for i in range(500_000):
    
    aumento = random.randint(1,2)
    numero += aumento
    
    letras = random.sample(alfabeto, 5)
    nombre = "".join(letras)

    edad = random.randint(18,99)

    impuestos = random.choice((True, True, True, True))

    censo.append([numero, nombre, edad, impuestos])

    if len(censo) % 100_00 == 0:
        print("Creados", len(censo), "registros")

print("Censo Creados.")
print("Ultimo registro: ", censo[-1])


def busqueda_numero(lista, elemento):

    inicio = 0
    final = len(lista) - 1

    while inicio <= final:
        medio = (inicio + final) // 2
        if lista[medio][0] == elemento:
            return lista[medio]
        elif lista[medio][0] <  elemento:
            inicio = medio + 1
        elif lista[medio][0] > elemento:
            final = medio - 1    
    return None

def busqueda_nombre(lista, elemento):
    encontrados = []
    for registro in lista:
        if registro[1] == elemento:
            encontrados.append(registro)
    if len(encontrados) == 0:
        return None
    else:
        return encontrados

def muestra_registro(registro):
    if registro == None:
        print("No existe regristro con ese dato. ")
    else:
        print("No existe registro con ese dato")
        print("Numero:", registro[0])
        print("Nombre:", registro[1])
        print("Edad:", registro[2])
        print("Impuesto:", registro[3])


def menu():
    print("---------------------------------------------")
    print("-----------CENSO DE POBLACION----------------")
    print("---------------------------------------------")
    print("1. Buscar por Número")
    print("2. Buscar por Nombre")
    print("3. Salir")
    
    opcion = ""
    while opcion not in ("1","2","3"):
        opcion = input("--------->")
    return opcion    

while True:
    opcion = menu()
    if opcion == "1":
        try:
            numero = int(input("Introduce número: "))
        except ValueError:
            print("Introduce un numero entero.")
        else:
            registro = busqueda_numero(censo, numero)
            muestra_registro(registro)

    elif opcion == "2":
        nombre = input("Introduce el nombre: ").upper
        registros = busqueda_nombre(censo, numero)
        if registros == None:
            print("No se encuentra registrado con ese dato.")
        else:
            for registro in registros:
                muestra_registro(registro)

    elif opcion == "3":
        break            

