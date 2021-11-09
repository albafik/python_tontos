import re
#for=permite recorrer una coleccion de valores
dias = {"lu": "lunes", "ma":"martes","mi":"miercoles"}

#for dia in dias:
    #print(dia)
#for indice in range(2,5):
    #print(indice)
#print(range(2, 5))    

dias2 = ["lunes", "mates", "miercoles", "jueves", "viernes", "sabado", "domingo"]
for dia in dias2:
    if dia == "mates":
        continue
    print(dia)
"""
#ciclos infinitos
while True:
# solicitar al usuario 1 para continuar el ciclo
#2 para deterner el ciclo
    print("Ingresa (1) para continuar")
    print("Ingresa (2) para detener")
    option = input(">")

    if option =="1":
        print("GRACIAS, selecciona otra opcion")
        print("----o----")
    if option =="2":
        print("GRACIAS, has detenido el ciclo")  
        break  
"""
grilla_numeros = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]
for fila in grilla_numeros:
    for col in fila:
        print(col)

"""
#errores en python
#try=ejecuta hasta un error; else=se ejecuta si no hay errore
try:
    num19 = int(input("Ingresa un número: "))
    num18 = 0
    print(num19)
    print(num19 / num18)
except ZeroDivisionError as err:
    print(err)
except ValueError :
    print("Entrada Invalida, debe ser un entero")         
else:
    print("No hubo ningun error")   
finally:
    print("Se ejecuta siempre sin importar que pase")    
"""
#PIP


#clases y objetos 

class Estudiante:
    def _init_(self, nombre, edad, profesion, curso_inicial):
        self.nombre = nombre
        self.edad = edad
        self.curso_inicial = curso_inicial
    def añadir(self): 
        self.curso = curso  
 

cadena = "Hola  estudiantes academiaCover. En academiaCoder los estudiantes aprenderan programacion. "

a_buscar = "estudiantes"

buscado = re.search(a_buscar, cadena)

print(buscado)
print(buscado.start())
print(buscado.end())
print(buscado.end() - 1)
print(buscado.span())

print(re.findall(a_buscar, cadena))

re_split = re.split("\s", cadena)
print(re_split)

re_sub = re.sub(a_buscar, "desrolladores",cadena )
print(re_sub)

lista = [
    "Marcos - Python",
    "Carlos - JavaScript",
    "Ana - JavaScript",
    "Marcos - PHP",
    "Natalia - Vue",
    "Violeta - Python",
    "Ana - PHP",
    "Carla - PHP"
]

for linea in lista :
    if re.findall("PHP$", linea):
        print(linea)
for linea in lista :
    if re.findall("^Marcos", linea):
        print(linea)
for linea in lista :
    if re.findall("[A]", linea):
        print(linea)

cadena2 = "abcdefg hijklñopqrstuvwxyz"\
           "0123456789"

print(re.findall("[a-d2-5]", cadena2))