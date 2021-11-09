from tkinter import *

#Creamos la raiz o root de nuestra app
root = Tk()
#Añadimos un titulo
root.title("Oso perro")
# Añadimos un icono para windows(y creo que par linux no MAC)
root.iconbitmap("python_18894.ico")
#Decimos si puede redimensionable(modifica tamaño de pagina) o no con 0 y 1 o true or false
root.resizable(True,1) 
#Definir el alto y ancho que queramos
#root.geometry("600x300")
#cambiar algunas opciones
 #bg cambia color de fondo
#Hacer que el frane sea un hijo de la raiz"root"
frame = Frame(root)
#Empaquetamos el frame dentro de la raiz
frame.pack()

#Cambiamos el color de fondo de nuestro marco frame
frame.config(bg="green")
#Damos un tamaño al marco o frame
frame.config(width=600, height=300)
#Cambiar el cursor del mouse,podemos darle un borde y tamaño
frame.config(cursor="pirate")
frame.config(relief="sunken")
frame.config(bd=20)
#Podemos configurar la raiz en algunas propiedades
root.config(
    bg="blue",
    cursor="hand2",
    relief="groove",
    bd=20
)
#Posicionamieto del marco frame
frame.pack(
    side=RIGHT,
    anchor=S,#N=NORTE,S=SUR,....
)
#Redimencionamos ocupando todo el espacio de la raiz
frame.pack(
    fill= "both",#AUMETA EL TAMAÑO DE FRAME DEPENDIENDO DEL EJE AL AUMENTAR LA RAIZ
    expand =1
)


#Ejecutamos el bucle infinito
root.mainloop() #Siempre va al final del programa