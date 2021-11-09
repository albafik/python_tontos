caracter_elegido = input("ELEGIJE UN CARACTER: ")


def encriptar(frase, caracter):
    encriptada = ""
    for letter in frase:
        if letter.lower() in "AEIOUÁÉÍÓÚaeiouáéíóú":
            if letter.isupper():
                encriptada = encriptada + caracter.upper()
            else:
                encriptada = encriptada + caracter
        else:
            encriptada = encriptada + letter  
    return encriptada
             

while True:
    print(encriptar(input("Ingresa una frase:\n>"), caracter_elegido)) 
    print("\nIngresa:\n(1) para incriptar otra frase")
    print("(2) para finalizar")
    option  = input (">")
    if option == "2":
       break
    if option == "1":
        print("-----o----\n")