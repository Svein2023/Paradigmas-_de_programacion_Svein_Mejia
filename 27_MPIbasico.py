#=====================
#Svein Samuel Mejia Zavala
#===========================
#Paradigmas de Programacion
#Matematica Algoritmica
#ESFM-IPN Diciembre-2023
#===========================

#=================================
# OJO !!! PARA CORRER SE ESCRIBE:
# mpiexec -n 4 pyhon3 27_MPIbasico.py
# o este otro
# mpirun -n 4 python3 27_MPIbasico.py
#=====================================
# Para correr en 4 procesos
#====================================
from mpi4py import MPI

#====================================
#Crear un objeto comunicador 
#===================================
comunicadores = MPI.COMM_WORLD

#==================================
# Numero total de procesos
#==================================
n_procesos = comunicadores.Get_size()

#===============================
# Identificadores de este proceso
#=================================
quien_soy = comunicadores.Get_rank()

print("Saludos desde el proceso",str(quien_soy), "de", str(n_procesos))

#=========================================
# Si yo soy el cero hago esto
#=========================================
if quien_soy == 0:
    print("Yo soy el proceso 0")

#=======================================
# Si yo soy el uno hago esto otro
#========================================
elif quien_soy == 1:
    print("Yo soy el proceso 1")

#==========================================
# Si yo no soy ni el uno ni el dos hago esto
#===========================================
else:
    print("Yo no soy ninguno de lols dos primeros procesos")

