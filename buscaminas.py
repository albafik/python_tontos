import random
import os


def crear_tablero(filas, colum, valor):
    tablero = []
    for i in range(filas):
        tablero.append([])
        for j in range(colum):
            tablero[i].append(valor)
    return tablero

def muestra_tablero(tablero):
    for fila in tablero:
        for elemento in  fila:
            print( elemento, end=" ")
        print()    

def coloca_minas(tablero, minas, fil, col):

    minas_ocultas = []
    numero = 0
    while numero < minas:
        y = random.randint(0,fil, -1)
        x = random.randint(0, col,-1)
        if tablero[y][x] != 9:
            tablero[y][x] = 9
            numero += 1
            minas_ocultas.append(y,x)
    return tablero, minas_ocultas        

def presentacion():
    os.system("cls")

    print("*******************************************************")
    print("*                                                     *")
    print("*                    BUSCAMINAS                       *")
    print("*                                                     *")
    print("*               w/a/s/d - moverse                     *")
    print("*                                                     *")
    print("*                  m - mostrar                        *")
    print("*                                                     *")
    print("*               b/v - marcar/desmarcar                *")
    print("*                                                     *")
    print("*                                                     *")
    print("*******************************************************")
    print()
    input(" ¨Enter¨ para empezar.....")

def menu():
    print()
    opcion = input("")




















columnas = 16
filas = 12

visible = crear_tablero(filas, columnas, "-")
oculto = crear_tablero(filas, columnas, 0)
