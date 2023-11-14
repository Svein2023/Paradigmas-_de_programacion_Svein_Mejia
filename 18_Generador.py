#=====================
#Svein Samuel Mejia Zavala
#=======================
#Paradigmas de Programacion
#Matematica Algoritmica
#ESFM-IPN Octubre-2023
#=========================


#========================================
# yield transforma la función a iterador
#=========================================
def migenerador():
    print("Primero")
    yield 10
    print("Segundo")
    yield "20"
    print("Tercero")
    yield "hola"

#=====================
# gen es un iterador
#======================
gen = migenerador()
vall = next(gen)
print(vall)
val2 = next(gen)
print(val2)
val3 = next(gen)
print(val3)

