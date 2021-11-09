def presentacion():
    print("***********************************************")
    print("*                                             *")
    print("*      Bienvenido al Juego de palillos        *")
    print("*                                             *")
    print("*       1.NIVEL FACIL/ 2.NIVEL DIFICIL        *")
    print("*                                             *")
    print("***********************************************")
    opcion = input("Ingresa el nivel de dificultad 1 o 2: ")
    while opcion != "1" and opcion != "2":
        opcion = input("Nivel no existen vuelve al elegir")

    return opcion

def presentacion2(palilllos,retiro):
    print("------------------------------------------------")
    print()
    print(f"        Habra {palilllos} palillos en Total   ")
    print(f"Se pueden quitar entre 1 y {retiro} palillos")
    print("Pulsa enter para empezar a jugar")
    print()
    print("------------------------------------------------")
    return

def sorteo():
    palillos = random.randint(16,24)
    retiro = random.randint(3,6)
    return palillos, retiro

def area_de_juego(palillos,retiro):
    print()
    print("************JUEGO DE PALILLOS**************")
    print()
    print()
    for fila in range(4):
        print(end="   ")
        for p in range(1,palillos+1):
            print("|", end="  ")
            if p % retiro == 0:
                print(end="  ")
        print()   
    print()
    print()
    print()  

def movimiento_jugador(palillos,retiro):
    if retiro == 3:
        retiro = ("1","2","3")
    elif retiro == 4:
        retiro = ("1","2","3","4")
    elif retiro == 5:
        retiro = ("1","2","3","4","5")
    q = input("Palillos a quitar: ")       
    while q not in retiro or int(q) > palillos:
        if q not in retiro:
            q = input(f"Elige entre 1 y {retiro} ")
        elif int(q) > palillos:
            q = input(f"Solo te quedan {palillos} palillos")
    else:
        palillos_quitar = int(q)   
    return palillos_quitar
     
def movimiento_aleatorio(palillos,retiro):
    palilos_quitar = random.randint(1,retiro)
    while palilos_quitar > palillos:
        palilos_quitar = random.randint(1,retiro)
    return palilos_quitar

def movimiento_ordenador_ia(palillos,retiro):
    palillos_quitar = None
    while palillos_quitar is None or palillos_quitar > palillos:
        if palillos <= retiro:
            palillos_quitar = palillos
        elif palillos %(retiro + 1) == 5:
            palillos_quitar = 5
        elif palillos %(retiro + 1) == 4:
            palillos_quitar = 4
        elif palillos %(retiro + 1) == 3:
            palillos_quitar = 3  
        elif palillos %(retiro + 1) == 2:
            palillos_quitar = 2
        elif palillos %(retiro + 1) == 1:
            palillos_quitar = 1  
        elif palillos %(retiro + 1) == 0:
            palillos_quitar = random.random(1,2)
    return palillos_quitar                 

def mostra_ganador(turno):
    if turno == 2:
        mensaje1 = "          HAS COGIDO EL ÚLTIMO PALILLO"
        mensaje2 = "       *******HAS GANADO*************   "
    elif turno == 1:
        mensaje1 = "    EL ORDENADOR COGE EL ULTIMO PALILLO  "
        mensaje2 = "******** GANA EL OPONENTE***************"

    print()
    print("******************JUEGO DE PALILLOS****************")
    print()
    print()
    print()
    print(f"{mensaje1}")
    print()
    print()
    print(f"{mensaje2}")
    print()
    print()
    print()



turno = 1

palillos, retiro = sorteo()
os.system("cls")
nivel = presentacion()

os.system("cls")
presentacion2(palillos, retiro)

jugando = True

while jugando:
    os.system("cls")
    area_de_juego(palillos,retiro)

    if turno == 1:
        jugada = movimiento_jugador(palillos, retiro)
        turno = 2
    elif turno == 2:
        print("....El ordenador esta pensando......")
        time.sleep(3)
        if nivel == "1":
            jugada = movimiento_aleatorio(palillos,retiro)
        elif nivel == "2":
            jugada = movimiento_ordenador_ia(palillos,retiro)    
        turno = 1

    palillos -= jugada

    if palillos == 0:
        os.system("cls")
        mostra_ganador(turno)
        jugando = False
