#=================================
# Svein Samuel Mejia Zavala
#======================================
# Matemática Algorítmica
# Paradigmas de Programacion
# ESFM IPN Septiembre 2023
#=====================================

#==========================================
# Listas 
# Las listas pueden ser de objetos diferentes
#=================================================
miprimeralista = [] # Lista vacía
print(miprimeralista)

#==============================================
# Llenado de lista
#==========================================
miprimeralista = [1, "Svein", 1.34, "Bryan","Arturo","Alexis",True]
print(miprimeralista)

#======================================================
# list: hacer una lista
# range(i,j): secuencia de j-1
#==========================================================
nums = list(range(1,61))

for i in nums:
    print(i)

#============================================================
# Incluír nuevos elementos en la lista
#==========================================================
nums.append(61)
nums.append(62)
nums.append(61)
print(nums)

#===========================================================
# Quitar el elemento con el indice i
#===========================================================
i = 61
del nums[i]
print(nums)

#===========================================================
# Borrar lista
#==========================================================
del nums

#=============================================================
# Sumar listas
#=============================================================
L1 = [1,2,3]
L2 = [4,5,6]
print(L1+L2)

#==============================================================
#Llenado de la mano
#=============================================================
potencial = []
for i in range(0,10000) :
    potencial.append(float(i))
print(potencial[100])

#============================================================
# Genera una tupla con listas
#===========================================================
potencial =  tuple(potencial)
print(potencial[100])

