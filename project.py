# organización = "freeCodeCamp"
import random
# print("Aprende a programar con " + organización)
# print("Aprende a programar con {}".formar)


# adj = input("Adjetivo:  ")
# verbo1 = input("Verbo1:  ")
# verbo2 = input("Verbo2:  ")
# sustantivo_plural1=input("sustantivoPlural:  ")

# # madlib = f"!Programar es tan {adj}¡ Siempre me emociona porque me encanta {verbo1} problemas. !Aprende a {verbo2} con freeCodeCamp y alcanza tus {sustantivo_plural1}¡"
# print(madlib)

# limite = 39
# intentos = 0
# intentos_restantes = 5
# adivina = random.randint(1,limite)



# while True:
#     print("Ingresa (1) para Jugar")
#     print("Ingresa (2) para Salir")
#     option = input("")
#     if option == "1":
#         saludar = input(f"Hola como te llamas:  ")
#         print(f"Bienvenido {saludar}, Intenta adivinar un numero entre 1 y {limite}, Recuerda solo tienes {intentos_restantes} intentos ")
#         while intentos < intentos_restantes:
#             numero = int(input(f"Intenta adivinar el numero: "))
#             if numero == adivina:
#                 print("Adivinaste el numero ganaste")
#                 break
#             elif numero < adivina:
#                 print("Intenta con un numero mas alto")
#             else:
#                 print("intenta con un numero mas pequeño")
#             intentos += 1  
#     if option =="2":
#         print("Vuelve pronto")  
#         break
        

# def adivina_el_numero_computadora(x):
#     saludo = input(f"Hola bienvenido como te llamas: ")
#     print(f"{saludo}, seleciona un numero entre 1 y {x} para que la computadora intente adivinarlo")
#     num_min = 1
#     num_max = x
#     respuesta = ""
#     while respuesta != "c":
#         #Generar una prediccion
#         if num_min != num_max:
#             prediccion = random.randint(num_min,num_max)
#         else: 
#             prediccion = num_min 
#         respuesta = input(f"Mi prediccion es: {prediccion}. Si es muy ala ingresa(A).Si es muy baja,ingresa(B).Y si es correcta ingresa (C)").lower()#transforma las letras a minusculas para procesar
#         if respuesta == "a":
#             num_max = prediccion - 1
#             #intervo reasignado [1,predicion-1]
#         elif respuesta == "b":
#             num_min = prediccion + 1
#             #Intervo reasignado [predicion + 1 , x]
#     print(f"!SIII¡ {saludo} ,La computadora adivino tu numero correctamente: {prediccion} ")   


# adivina_el_numero_computadora(20)     


def Jugar():
    usuario = input("Escoge una opción:´TI´ para tijeras,´PI´ para piedra y ´PA´ para papel.!\n").lower()
    computadora = random.choice(["pi","pa","ti"])#seleciona al alzar una de las opciones en el corchete.
    
    if usuario == computadora:
        return "!Empate¡"
    
    if gano_el_jugador(usuario, computadora):
        return "!Ganaste¡"
    
    return "!Persiste¡"        
    

def gano_el_jugador(jugador,oponente):
    #Retorna True si gana el jugador
    if ((jugador == "pi" and oponente == "ti")
       or(jugador == "ti" and oponente == "pa")
       or(jugador == "pa" and oponente == "pi")):
       return True
    else:
        return False


print(Jugar())        

             







