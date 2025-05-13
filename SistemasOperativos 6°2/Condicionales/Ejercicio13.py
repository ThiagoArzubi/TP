import os
os.system ("cls")


#CALCULAR SI EL AÑO ES BISIESTO
print("-----------------------------------------------")
print(" EJERCICIO 13: VERIFICAR SI EL AÑO ES BISIESTO")
print("-----------------------------------------------")
print("")
año=int(input("Ingrese un año"))
if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    print("El año es bisiesto")
else:
    print("El año no es bisiesto")