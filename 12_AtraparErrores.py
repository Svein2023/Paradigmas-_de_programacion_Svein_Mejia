#===============================
# Svein Samuel Mejia Zavala
#================================
# Matematica Algoritmica
# Paradigmas de Programacion
# ESFM IPN octubre 2023
#==============================

#================================
# La clase ClienteBancario esta en el subdirectorio
# aplicacion/banco/
#======================================================
from aplicacion.banco.cliente_bancario import ClienteBancario

#==============================================================
# try: intenta (correr las instrucciones )
# except : atrapar el error en una variable e 
# e se puede convertir a string
#============================================================

#=======================================================
# Error pór sacar mas dinero del que tiene
#====================================================
try:
    cliente = ClienteBancario("Jaime Andrade","Hernandez Sanchez ",28,0.0)
    cliente.guardarDinero(300)
    print(cliente.imprimirInfo())
    cliente.retirarDinero(400)
    print(cliete.imprimirInfo())
 #===============================================
 # Exception es el objeto mas general de error
 #===================================================
except Exception as e:
    print("Error: " + str(e))
#===========================
# Error por usar un atributo privado
#==========================
try:
    print(cliente._nombres)
except Exception as ex:
    print("Error:" + str(ex))

#============================
# Formar correcta
#=========================
print(cliente.nombres)

