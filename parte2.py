number =[1, 25, 798, 49, 9, 9]
frutas = ["Naranja","Banana","Manzana","Mandarina","Pera","Uva"]
#print(frutas)
#print(frutas[4])
#print(frutas[-3]) 
#print(frutas[1:5])
frutas[1] = ("Guayaba")
#remplaza un elemento de la lista
frutas.append("Sandia")
#anade un elemento a la lista
print(frutas)
print(len(frutas))
#calcula la longitud de la cadena
print(frutas.index("Mandarina"))
#indica la posicion de un elemento de la lista
print(frutas.count("Uva"))
#indica cuantas veces se repite la lista
number.sort()
print(number)
#ordena la lista de menor a mayor
number.reverse()
print(number)
#ordena al reves la lista
frutas2 = frutas.copy()
print(frutas2)
coordenadas =(42.88, 55.16, "ppppjo")
print(len(coordenadas))
#funcion cuatro espacio abajo de lo cuatro puntos:dos espacio antes y despues de la función


def saludar(nombre, edad, tamaño):
    print("Hola usuario " + nombre + " tienes " + edad + " años" + ",tu estatura "+ str(tamaño) + " m")
    print("Adios Pendejo")
saludar("MARCOS", "35", 1.50)


#regla de la funciones cuando el nombre es dos palabras o mas usar_ :eje:saludar_participantes    


def multiplicar(num1, num2):
    return num1 * num2
res_multi = multiplicar(2, 10)       
print(res_multi)

si_es_hombre = False
eres_alto = True

if si_es_hombre and eres_alto:
    print("Eres un hombre")
elif si_es_hombre and  not eres_alto:
    print("Eres un hombre pequeño")
elif not si_es_hombre and eres_alto:
    print("No eres hombre pero si eres alto")    
else:
    print("No eres un hombre ni alto")  
"""
def mayor_edad(num) :
    if num >= 10:
        return True
    else:
        return False
        
edad = input("ingresa tu edad:")  
if mayor_edad(int(edad)):
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")
"""
def mayor_numero(n1, n2, n3):
    if n1 >= n2 and n1 >= n3:
        return n1
    if n2 >= n1 and n2 >= n3:
        return n2
    else:
        return n3
numero = mayor_numero(99, 556, 300)
#print(mayor_numero(100,66,104))
#print(numero)

conjuntos = {"Perro", 2, False, 49.50, True, 29}
print(conjuntos)
conjuntos.add(508)
print(conjuntos)
conjuntos.remove(False)
print(conjuntos)
#listas
dias = {
    "lun":"lunes",
    "Mar":"Martes",
    "Mie":"Miercoles",
    "Jue":"Jueves",
    "Vie":"Viernes"
}
#print(dias.get("lun"))
print(dias.pop("lun"))
print(dias.popitem())
dias.update(Mar="sabado")
print(dias)

C = 1
while C <= 5:
    print(C)
    C += 1
print("Termino el bucle")
print(C)

