import random
# pares = {
#     "A": 1,
#     "B": 2,
#     "C": 3,
#     "D": 4,
#     "E": 5
# }
# lista_l = []
# lista_n = []
# for par in pares:
#     lista_l.append(par)
#     lista_n.append(pares[par])
# print(lista_l)
# print(lista_n)
# letra = list(pares.keys())
# numero = list(pares.values())

# letras = ["A","B","C","D","E"]
# numeros = [1,2,3,4,5]

# pares = dict(zip(letras,numeros))

# for i in range(len(letras)):
#     pares[letras[i]] = numeros[i]
# print(pares)    

# prefijos = {
#     "COLOMBIA": 57,
#     "ARGENTINA": 54,
#     "PERU": 51,
#     "MEXICO": 591,
#     "BOLIVIA": 52,
#     "CHILE": 56,
#     "ESPAÑA": 34,
#     "ECUADOR": 593
# }
# print("PREFIJOS INTERNACIONALES")
# print("--------------------------------")
# busquedas = {}
# while True:    
#     busqueda = input("País (´x´ salir): ").upper()
#     if busqueda == "X":
#         break
#     prefijo = prefijos.get(busqueda, "No Disponible.")
#     print()
#     print(f"{busqueda}: {prefijo} ")

#     busquedas.setdefault(busqueda, 0)
#     busquedas[busqueda] += 1

#     print("----------------------------------")
#     print("REGISTRO DE BUSQUEDA: ")
#     for l, c in busquedas.items():
#         print(f" {l}: {c} ")
#         print("----------------------------------")
        
# frase = "Hoy ha salido el sol y hace una mañana estupenda."
# abc  = "abcdefghijklmnñopqrstuvwxyz."

# conteo = dict.fromkeys(abc, 0)
# for letra in frase.lower():
#     conteo.setdefault(letra, 0)
#     conteo[letra] += 1

# print(conteo)    

# capitales = {
#     "Canada": "Otawa",
#     "Uruguay": "Montevideo",
#     "Kenia": "Nairobi",
#     "Islandia": "Reikiavik",
#     "Filipinas": "Manila"
# }

# paises = list(capitales.keys())
# print("---------------------------------")
# print("----------REPASAR CAPITALES------")
# print("---------------------------------")
# while len(paises) > 0: 
#     fallos = []
#     random.shuffle(paises)
#     for pais in paises:
#         print()
#         print(f"La capital de {pais} es: ")
#         respuesta = input("--------->").capitalize()
#         if respuesta == capitales[pais]:
#             print("Respuesta correcta")
#         else:
#             print(f"Respuesta incorrecta era {capitales[pais]} ") 
#             fallos.append(pais)

#         print()
#     paises = fallos           

agenda = {
    "Jorge":{
        "Telefono": 11111111,
        "Pais": "Ecuador",
        "Personal":{
            "Aficion": "futbol",
            "Estudios": "Agronomia",
            "Musica": "Clásica"
        }
    },
    "Maria":{
        "Telefono": 222222222,
        "Pais": "Colombia",
        "Personal":{
            "Aficcion": "Astronomia",
            "Estudios": "Informatica",
            "Musica": "Rock",
        }
    },
    "Tomas":{
        "Telefono": 33333333,
        "Pais": "Ecuador",
        "Personal": {
            "Aficcion": "Oso peroo",
            "Estudios": "Gelogia",
            "Musica": "Clasica"
        }
    }
}
for nombre, datos in agenda.items():
    if datos["Pais"] == "Colombia" and datos["Personal"]["Musica"] == "Rock":
        print(nombre)
    
for nombre, datos in agenda.items():
    ho = datos["Personal"]["Aficcion"]
    print(ho)
  











