import random
import string
from palabras import palabras 
from ahorcado_diagrama import vidas_diccionario_visual as estructura

def obtener_palabras_valida(palabras):
    #Seleccionar una palabra la azar de la lista
    palabra = random.choice(palabras)

    while "-" in palabra or " "in palabras:
        palabra = random.choice(palabras)
    return palabra.upper()    


def ahorcado():
    print("=============")
    saludo = input(f"!Bienvenido como te llamas_: ")
    print("=============")
    
    palabra = obtener_palabras_valida(palabras)
    
    letras_por_adivinar = set(palabra)
    abecedario = set(string.ascii_uppercase) #retorna todas las letras del abecedario mayuscuklas.
    letras_asignadas = set()

    vidas = 7
    
    while len(letras_por_adivinar) > 0 and vidas > 0:
        print(f"Te quedan {vidas} vidas y has usado estas letras: {''.join(letras_asignadas)}")

        # Mostrar el estdo actual de la palabra.   
        palabra_lista = [letra if letra in letras_asignadas else "-" for letra in palabra]
        # Mostrar estado del ahorcado.
        print(estructura[vidas])
        # Mostrar las letras separadas por un espacio.
        print(f"Palabra: {''.join(letras_asignadas)} ")

        letra_usuario = input("Escoge una letra: ").upper()
        # Si la letra escogida por el usuario esta en el abecedario y no esta en el conjunto de letras que ya se han ingresado, se añade la letra al conjunto de letras ingresadas.
        if letra_usuario in abecedario - letras_asignadas:
            letras_asignadas.add(letra_usuario)
            
            # Si la letra esta en la palabra
            if letra_usuario in letras_por_adivinar:
                letras_por_adivinar.remove(letra_usuario)
                print("")
            else:
                vidas -= 1 
                print(f"\nTu letra, {letra_usuario} no esta en la palabra.")   

        if vidas == 0:
            print(estructura[vidas])  
            print(f"PERDISTE {saludo} lo lamento mucho la palabra era: {palabra} ")
        else: 
            print(f"Excelente {saludo} adivinaste la palabra {palabra} ")    
    





    