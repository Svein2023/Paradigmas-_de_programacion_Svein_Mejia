#=====================
#Svein Samuel Mejia Zavala
#===========================
#Paradigmas de Programacion
#Matematica Algoritmica
#ESFM-IPN Noviembre-2023
#===========================

#============================
# Importar modulos necesarios
#============================
import numpy as np
import matplotlib.pyplot as plt
from mpl_tooklkits.mplot3d import Axes3D
from matplotlib impor cm
import time
from numba import jit

#==========================
# Parametros de entrada
#==========================

#-------------------------------
#Numeros de celdas
n = np.array([512,512])
# Tamano del dominio (menor que uno)
L = np.array([1.0,1.0])
# Constante de difusion
k = 0.2
# Pasos de tiempo
pasos = 100
#---------------------------------

#====================================
# Parametros secundarios
#=======================================
# Tamano del las celda
dx = L/n
udx2 = 1.0/(dx*dx)
# Paso de tiempo
dt = 0.25*(min(dx[0]dx[1]**2)/k
print("dt = ",dt)
           # Total de celdas
