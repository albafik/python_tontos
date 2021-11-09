import pickle
"""
estudiantes : {
    "Marcos",
    "Carla",
    "Agustin",
    "Pedro",
    "Maria"
}


archivo_serializado = open("estudiantes", "wb")
#creamos un archibo para guardar el estado
pickle.dump(estudiantes, archivo_serializado)
#volcamos el contenido de la lista en el archivo
archivo_serializado.close()
del archivo_serializado"""

"""archibo = open("estudiantes", "rb")
lista_estudiantes = pickle.load(archivo)

print(lista_estudiantes)"""

#serializacion de objetos

class Estudiantes:
    def __init__(self, nombre, edad, curso_inicial):
        self.nombre = nombre
        self.edad = edad
        self.curso_inicial = curso_inicial
        self.esta_activo = True
        self.cursos = [curso_inicial]

        print("Se ha creado un estudiante llamado: {self.nombre} ")

    def desactivar(self):
        self.esta_activo = False

    def Info (self):
        print(f"Estudiantes: {self.nombre}\nEdad: {self.edad}\nActivo: {self.esta_activo}\n ") 
        
    def __str__(self):
        return f"{self.nombre}, {self.edad} años " 
