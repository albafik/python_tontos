import random
import time
import os

def presentacion_1():
    print()
    print("                    TRES EN RAYA")
    print()
    print()
    print("                          1. FACIL")
    print("                        2. DIFICIL")
    print()
    print()
    print()
    nivel = ""
    while nivel != "1" and nivel != "2":
        nivel = input("                  --->")
    return nivel    

def presentacion_2():
    print()
    print("                    TRES EN RAYA")
    print()
    print("                 Sale la ficha O")
    print()
    print("                Elige: O / X")
    print()
    print()

    ficha = ""
    while ficha != "O" and ficha != "X":
        ficha = input("--------->")

    if ficha == "O":
        humano = "O"
        ordenador = "X"
    else:
        humano = "X"
        ordenador = "O"
    return humano, ordenador


def mostrar_tablero(tablero):
    print()
    print("                       TRES EN RAYA")
    print("        1              |2               |3     ")
    print(f"             {0}      |      {1}       |   {2}   ")
    print("                       |                |        ")
    print("----------------+----------------+----------------")
    print("        4              |5               |6     ")
    print(f"             {3}      |      {4}       |   {5}   ")
    print("                       |                |        ")
    print("----------------+----------------+----------------")
    print("        7              |8               |9     ")
    print(f"             {6}      |      {7}       |   {8}   ")
    print("                       |                |        ")
    print()


def seguir_jugando():
    print()
    respuesta = input("              ¿Otra partida? (s) ").lower()
    if respuesta == "s " or respuesta == "si":
        return True
    else:
        return False


def hay_ganador(tablero,jugador):
    if tablero[0] == tablero[1] == tablero [2]== jugador or\
       tablero[3] == tablero[4] == tablero [5]== jugador or\
       tablero[6] == tablero[7] == tablero [8]== jugador or\
       tablero[0] == tablero[3] == tablero [6]== jugador or\
       tablero[1] == tablero[4] == tablero [7]== jugador or\
       tablero[2] == tablero[5] == tablero [8]== jugador or\
       tablero[0] == tablero[4] == tablero [8]== jugador or\
       tablero[6] == tablero[4] == tablero [2]== jugador:
       return True
    else:
        return False

def tablero_lleno(tablero):
    for i in tablero:
        if i == " ":
            return False
        else:
            return True

def casilla_libre(tablero, casilla):
    return tablero[casilla] == " "


def movimiento_jugador(tablero):
    posiciones = ["1","2","3","4","5","6","7","8","9"]
    posicion = None
    while True:
        if posicion not in posiciones:
            posicion = input("----------- Te toca del 1 al 9: ")
        else:
            posicion = int(posicion)
            if not casilla_libre(tablero, posicion - 1):
                print("          Esta posicion esta ocupada")
            else:
                return posicion - 1

def mov_ordenador_facil(tablero,jugador):
    if tablero[0] == tablero [1] == jugador and tablero[2] == "":
        casilla = 2
    elif tablero[0] == tablero [2] == jugador and tablero[1] == "":
        casilla = 1   
    elif tablero[3] == tablero [4] == jugador and tablero[5] == "":
        casilla = 5
    elif tablero[1] == tablero [2] == jugador and tablero[0] == "":
        casilla = 0   
    elif tablero[3] == tablero [5] == jugador and tablero[4] == "":
        casilla = 4
    elif tablero[4] == tablero [5] == jugador and tablero[3] == "":
        casilla = 3
    elif tablero[6] == tablero [7] == jugador and tablero[8] == "":
        casilla = 8
    elif tablero[6] == tablero [8] == jugador and tablero[7] == "":
        casilla = 7
    elif tablero[7] == tablero [8] == jugador and tablero[6] == "":
        casilla = 6
    elif tablero[0] == tablero [4] == jugador and tablero[8] == "":
        casilla = 8
    elif tablero[0] == tablero [8] == jugador and tablero[4] == "":
        casilla = 4
    elif tablero[4] == tablero [8] == jugador and tablero[0] == "":
        casilla = 0
    elif tablero[2] == tablero [4] == jugador and tablero[6] == "":
        casilla = 6
    elif tablero[2] == tablero [6] == jugador and tablero[4] == "":
        casilla = 4
    elif tablero[4] == tablero [6] == jugador and tablero[2] == "":
        casilla = 2


    else:  
        while True:
            casilla = random.randint(0,8)
            if tablero[casilla] == " ":
                break

    return casilla

            




jugando = True
while jugando:

    tablero = [""] * 9

    os.system("cls")

    nivel = presentacion_1()

    os.system("cls")

    humano, ordenador = presentacion_2()

    os.system("cls")

    mostrar_tablero(tablero)

    if humano == "O":
        turno = "Humano"
    else:
        turno = "ordenador"
    partida = True
    while partida:
        if tablero_lleno(tablero):
            print("                   Empate")
            partida = False
        elif turno == "Humano":
            casilla = movimiento_jugador(tablero) 
            tablero[casilla] = humano
            turno = "Ordenador"
            os.system("cls")
            mostrar_tablero(tablero)
        if hay_ganador(tablero, humano):
            print("                Has ganado")
            partida = False   

        elif turno == "Ordenador":
            print("              El ordenador esta pensando ")
            time.sleep(2)
            if nivel == 1:
                casilla = mov_ordenador_facil(tablero,humano)
            tablero[casilla] = ordenador
            turno = "Humano"
            os.system("cls")
            mostrar_tablero(tablero)
            if hay_ganador(tablero,ordenador):
                print("            Has perdido")
                partida = False            
