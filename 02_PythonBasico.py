#==============================
#Svein Samuel Mejia Zavala
#==============================
#Matemática Algoritmica
#ESFM IPN
#Septiembre de 2023 
#================================

#===============================
#Input permite obtener datos del usuario en prompter
#======================================================
nombre = input("Dame tu nombre: ")
print("Hola como estas ",nombre)

#=====================================
#Los enteros son de presicisión ilimitada
#==========================================
y=500000000000000000000000000000000000
print(y)

#==============================================
#Se puede delimitar números con guión bajo pero no con coma
#=====================================================
y=5_000_000
print(y)

#===================================================
#La funcion int() cambia strings y floats a enteros 
#===================================================
numero = int(input("Dame tu edad: "))
type(numero)

#================================================
#La notacion cientifica de flotantes utiliza e o E
#===================================================
#1.2 x 10 elevado a la -9
#==================================
y = 1.2E-09
print(y)

#=========================================
#La función float() convierte strings y enteros a floats
#==========================================================
y = float("14.3")
print(y)

#=====================================================
#Los complejos se escriben con la raíz de menos uno
#j siempre con un número como prefijo
#no acepta la j suelta
#===========================================================

z = 1+1j

#suma +
#resta -
#multiplicacion *
#division /
#módulo %
#exponente **
#// función piso
#Funciones para transformar números int() float() complex()
#Operaciones abs() round() pow()

print(round(3.14159,4))

#=======================================
# Strings de varias lineas
#========================================
parrafo = """En el bosque de la china
 la chinita se perdió """
print(parrafo)

 #======================================
 #La función len() obtiene el tamaño de string
 #=============================================
n=len(parrafo)
print(n)

#=============================================
 #Las letras de string ocupan lugares como en un arreglo
 #(tambien de atrás para adelante comenzando en -1 el ultimo)
 #=============================================================
palabra = "hola"
print(palabra[0])
print(palabra[-4])

