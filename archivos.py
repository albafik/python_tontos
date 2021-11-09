import os

# archivo = open("quijote.txt", "r", encoding="utf-8")
# texto = archivo.read()
# archivo.close()
# palabras = {}

# lista = texto.split()
# for elemento in lista:
#     palabra = elemento.strip(".").strip(",").strip(";").strip(":")
#     if len(palabra) > 12:
#         palabras.setdefault(palabra,0)
#         palabras[palabra] += 1 #aumenta el valor de la palabra en el diccionario

# for i in range(5):
#     numero_mayor = 0
#     for palabra in palabras: 
#         if palabras[palabra]  > numero_mayor:
#             numero_mayor = palabras[palabra]
#             palabra_mayor = palabra
#     print(palabra_mayor,":", numero_mayor)
#     del palabras[palabra_mayor]


# archivo = open("alfabeto.txt","r",encoding="utf-8")
# texto = archivo.read(10)

# print(texto)

# texto2 = archivo.read()
# print(texto2)
# archivo.seek(5)
# texto3 = archivo.read()
# print(texto3)

# archivo.close()

# if os.path.exists("notas/nota1.txt"):
#     with open("notas/nota1.txt", "r") as archivo:
#        texto = archivo.read()
#        print(texto) 
# else:
#     print("Ese archivo no existe")       

# with open("archivo2.txt","r+") as archivo:
#     archivo.seek(0, 2)
#     archivo.write("b")

#     archivo.seek(0)
#     texto = archivo.read()
#     print(texto)
if not os.path.exists("notas.txt"):
    with open("notas.txt", "w", encoding="utf-8") as archivo_notas:
        pass

while True:

    os.system("cls")
    
    with open("notas.txt", "r", encoding="utf-8") as archivo_notas:
        lista_notas = archivo_notas.readlines()

    for  i in range(len(lista_notas)):
        lista_notas[i] = lista_notas[i].strip()     

    print("----------------------------------------------")
    print("CUADERNO DE NOTAS")
    print("-------------------NOTAS----------------------")
    if len(lista_notas) == 0:
        print("No hay notas")
    else:
        n = 0
        for nota in lista_notas:
            n += 1
            print(f"Nota {n} : {nota} ")

    print("------------------OPCIONES--------------------")
    print("1. Crear nueva nota")
    print("2. Leer una nota")
    print("3.cambiar nombre nota")
    print("4. Borrar una nota")
    print("5. Salir del programa")
    print("----------------------------------------------")
    opcion =  ""

    while opcion not in ("1","2","3","4","5"):
        opcion = input("------->")

    if opcion == "1":
        nombre = input("Nombre de la nota: ").strip()
        if os.path.exists(nombre + ".txt"):
            print("Ese nombre ya existe")
            print()
            print("Enter para continuar.......")
        else:
            with open("notas.txt", "a", encoding="utf-8")as archivo_notas:
                archivo_notas.write(nombre + "\n")        
            
            with open(nombre + ".txt", "w", encoding="utf-8") as nuevo_archivo:
                while True:
                    print("Escribe contenido {´S´ para salir}")
                    contenido = input("> ").capitalize()
                    if contenido == "S": 
                        break
                    else:
                        nuevo_archivo.write(contenido + "\n")
    
    elif opcion == "2":
        numero = input("Numero de nota: ")
        numeros_posibles = []
        for i in range(1, len(lista_notas)+ 1):
            numeros_posibles.append(str(i))

        if numero not in numeros_posibles:
            print("Numero de nota incorrecto")
            print()
            print("Enter para continuar...")
        else:
            numero = int(numero)
            nota = lista_notas[numero - 1] 
            with open(nota + ".txt", "r", encoding="utf-8") as archivo_notas_leer:
                contenido_nota = archivo_notas_leer.read()
            print("-----------------------------------------------")
            print()
            print(contenido_nota)
            print()
            print("Enter para continuar.")
    
    elif opcion == "3":
        numero = input("Numero de nota: ")
        
        for i in range(1, len(lista_notas)+ 1):
            numeros_posibles.append(str(i))

        if numero not in numeros_posibles:
            print("Numero de nota incorrecto")
            print()
            print("Enter para continuar...")
        
        else:
            numero = int(numero)
            nuevo_nombre = input("Ingresa el Nuevo nombre: ")
            if os.path.exists(nuevo_nombre + ".txt"):         
               print("Ese nombre ya existe")
               print()
               print("Enter para continuar.......")

            else:
                nombre_cambiar = lista_notas[numero - 1 ]
                os.rename(nombre_cambiar + ".txt", nuevo_nombre + ".txt")

                lista_notas[numero - 1] = nuevo_nombre
                with open("notas.txt", "w", encoding="utf-8") as archivo_notas:
                    for nota in lista_notas:
                        archivo_notas.write(nota + "\n")

    elif opcion == "4":
        numero = input("Numero de nota: ")
        
        for i in range(1, len(lista_notas)+ 1):
            numeros_posibles.append(str(i))

        if numero not in numeros_posibles:
            print("Numero de nota incorrecto")
            print()
            print("Enter para continuar...")
        
        else: 
            borrar = int(numero)

            nota_borrar = lista_notas[borrar - 1]

            os.remove(nota_borrar + ".txt")

            del lista_notas[borrar - 1 ]
            with open ("notas.txt", "w", encoding="utf-8") as archivo_notas:
                for nota in lista_notas:
                    archivo_notas.write(nota + "\n")

    elif opcion == "5":
        break                




          
