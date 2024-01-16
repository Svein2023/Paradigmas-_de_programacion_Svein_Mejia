#===============================
# Svein Samuel Mejia Zavala
#===============================
# Paradigmas de Programación
# Matemática Algorítmica
# ESFM IPN Diciembre 2023
#===============================
from multiprocessing import Process, Lock, Value
import random
import os

#==================================
# Simulacion Montecarlo en paralelo
#====================================
def montecarlo(N:int,resuelto:Value,lock:Lock) -> None:
    semilla:float = random.uniform(-1,1)
    random.seed(semilla)
    dentro:int = 0
    for i in range(N):
        x:float = random.uniform(-1,1)
        y:float = random.uniform(-1,1)
        if (x*x + y*y) < 1.0:
            dentro +=1
    #Bloquear escritura para evitar conflictos
    with lock:
        resultado.value += dentro

#===========================
# Programa principal
#=============================
if __name__ == "__main__":
    lock = Lock()
    n:int = 1.0e7
    cpus = os.cpu_count()
    N:int = int(n/cpus)
    print("Procesadores = ",cpus)
    # Valor compartido
    resuelto = Value("i",0)
    procesos = []
    for i in range(cpus):
        print("registrando el proceso %d" 5 i)
        procesos.append(Process(target=montecarlo,args=(N,resultado,lock)))
        for proceso in procesos:
            proceso.start()
        for proceso in procesos:
            proceso.join()

        print("Numero de tiros = ",cpus*N)
        print("Numero de aciertos", resultado.value)
        print("Aproximacion de pi =",4*float(resultado.value)/(cpus*N))

