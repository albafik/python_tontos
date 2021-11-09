from parte4 import Estudiantes as E
import pickle

est1 = E("Marcos", 35, "Python")
est2 = E("Carla", 25, "Javascript")


class listaDeEstudinates :
     estudiantes = []

     def __init__(self):
         archivoEstudiantes = open("lista_estudiantes","ab+")
         archivoEstudiantes.seek(0)

         self.estudiantes = pickle.load(archivoEstudiantes)
         print(f"{len(self.estudiantes)}")   


     def agregarEstudiantes(self, e):
         self.estudiantes.append(e)
    
     def mostrarEstudiantes(self):
         for e in self.estudiantes:
             print(0)    


lista = listaDeEstudinates()

lista.agregarEstudiantes(est1)
lista.agregarEstudiantes(est2)

lista.mostrarEstudiantes()