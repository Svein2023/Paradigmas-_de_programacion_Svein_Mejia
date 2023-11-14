#=====================
#Svein Samuel Mejia Zavala
#=======================
#Paradigmas de Programacion
#Matematica Algoritmica
#ESFM-IPN Noviembre-2023
#=========================

#===============================================
#Graficos usando la tortuga que pinta al caminar
#===============================================
import turtle
tortuga = turtle.Turtle()
tortuga.left(90)  #Giro a la izquienda a 90 grados
tortuga.speed(500) #Velocidad de la tortuga

#==============================
#Con angulos de 90 es un árbol H
#=================================
angulo:float = 90

#=======================================
# El árbol se construye con recursividad
#==========================================
def arbol(i:float,angulo:float):
    if i<10.0:
        return
    else:
        tortuga.forward(i) # Camina 1
        tortuga.left(angulo) # Gira a la izquierda 90 grados
        arbol(3.0*i/4.25,angulo) # Pide otro arbol y pide la longitud del paso
        tortuga.right(2*angulo) # Gira a la derecha 180 
        arbol(3.0*i/4.25,angulo)
        tortuga.left(angulo)
        tortuga.backward(i)

arbol(100,angulo)
turtle.done()


