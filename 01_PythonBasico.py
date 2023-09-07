#=====================
#Svein Samuel Mejia Zavala
#=======================
#Paradigmas de Programacion
#Matematica Algoritmica
#ESFM-IPN sept-2023
#=========================
''' ESTE ES UN SUPER COMENTARIO DE INICIO A NUESTRO RESUMEN '''
#============
#Operaciones basicas
#==============
print (2+3)
print (2*3)
print (2/3)
print (2**10)
print (2**0.5) #raiz cuadrada
print (10%2)
print (10%0.1) #exclusivo en python
#=============================
#Para saber el tipo de objeto usa type
#===================================
t=0
print(type(t)) #entero
t=3.6
print (type(t)) #real (flotante)
t=True
print(type(t)) #booleano (bool)

#==============
#Mensaje en pantalla
#=================
print ("Este es un comando en python.", "Este es otro enunciado.",t)
print ('id: ', 1)
print ('Forst Name:','Steve')
print ('Last Name:','JObs')
print("Vamos a sumar esto "+" con esto otro")
#================
#Continuar una instruccion en varios renglones
#=========================
if 100>99 and \
    200<=300 and \
    True !=False:
    print('Hello World')

#===================
#Comandos diferentes en la misma linea
#===============
print("Hola"); print("tu!!") #Se considera malala practica
#======================
#Usando parentesis redondos, cuadrados o llaves
#se puede escribir en varios renglones
#=========================
list = [1,2,3,4,
        5,6,7,8,
        9,10,11,12]
matriz = [ [1,2,3,4],[5,6,7,8],[9,10,11,12] ]

print(list)
print(matriz)
#===========================
#Indentacion estricta para procesos dependientes de : (dos puntos)
#============================
if 10>5:
    print ("diez es mayor que cinco")
    print("Otra indeterminacion")
for i in list:
    print (i)
    print ("ok")
if 10>5:
    print ("verdadero")
if 10<20:
    print("verdadero")
elif 5>3:#comienza segunda condicional
    print ("esto no se imprimira")
else:
    print ("aqui nunca llega")

#==========
#Funciones
#==============
def say_hello(name):
    print("Hello",name)
    print("Welcome to Python Tutorials")
say_hello("Svein")
