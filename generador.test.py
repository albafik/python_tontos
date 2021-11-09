import random
import os

def lista_usuarios():
    with open("datos.txt", "r", encoding="utf-8") as archivo_datos:
        lista_datos = archivo_datos.readlines()

    lista_usuarios = []
    for dato in lista_datos:
        lista_usuarios.append(dato.strip().split(","))

    return lista_usuarios

def menu_entrada():
    print("--------------------------------------------")
    print("             GENERADOR DE TEST               ")
    print("---------------------------------------------")
    print("1. Entrada al sistema")
    print("2. Darse de alta")
    print("3. Salir")
    print("---------------------------------------------")
    opcion = ""

    while opcion not in ("1","2","3"):
        opcion = input("----->")
    return opcion  

def menu_principal(nombre_usuario):
    print("--------------------------------------------")
    print(f"             USUARIO: {nombre_usuario}                ")
    print("---------------------------------------------")
    print("1. Hacer Test")
    print("2. Puntuaciones")
    print("3. Salir")
    print("---------------------------------------------")
    opcion = ""

    while opcion not in ("1","2","3"):
        opcion = input("----->")
    return opcion  

def entrada_al_sistema(lista_usuarios):

    usr = input(" Introduce usuario: ")
    con = input(" Introduce contraseña: ")

    for usuario in lista_usuarios:
        if usuario[0] == usr  and usuario[1] == con:
            return usuario
    else:
        return None


def darse_de_alta(lista_usuarios):

    while True:
        usr = input(" Elige usuario: ")
        if len(usr) < 4:
            print("Ha de tener al menos 4 caracteres")
        else:
            for usuario in lista_usuarios:
                if usr == usuario[0]:
                    print("Ese nombre esta cogido")
                    break 
            else:
                while True:
                    con1 = input("Elige contraseña: ")
                    if len(con1) < 4:
                        print("Ha de tener al menos 4 caracteres.")
                    else:
                        con2 = input("Repite la contraseña.: ")
                        if con1 != con2:
                            print("La contraseña no coincide")
                            break           
                        else:
                            lista_usuarios.append([usr, con1, "0", "0", "0"])
                            print("Usuario dado de alta.")

                            return lista_usuarios

def grabar_datos(lista_usuarios):

    with open("datos.txt", "w", encoding="utf-8") as archivo_datos:
        for u in lista_usuarios:
            archivo_datos.write(u[0] + "," + u[1] + "," + u[2] + "," + u[3] + "," + u[4] +"\n")
    return None        





if not os.path.exists("datos.txt"):
    with open("datos.txt", "w", encoding="utf-8") as  archivo_datos:
        pass

while True:

    jugando = False
    os.system("cls")

    lista_usuarios = lista_usuarios()
    opcion_entrada = menu_entrada()

    if opcion_entrada == "1":
        usuario = entrada_al_sistema(lista_usuarios)

        if usuario == None:
            input("Datos Incorrectos")
        else:
            jugando = True

    elif opcion_entrada == "2":
        lista_usuarios = darse_de_alta(lista_usuarios)

        grabar_datos(lista_usuarios)
        input("Enter para continuar")

    elif opcion_entrada == "3":
        break



