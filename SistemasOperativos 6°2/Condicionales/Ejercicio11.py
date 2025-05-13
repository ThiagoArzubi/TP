import os
os.system ("cls")


#CALCULAR SI UN ALUMNO ESTA APROBADO
print("----------------------------------------------------")
print(" EJERCICIO 11: VERIFICAR SI UN ALUMNO ESTA APROBADO")
print("----------------------------------------------------")
print("")
nota=float(input("Ingrese su nota: "))
if nota >= 7:
    print("Aprobado")
else:
    print("Desaprobado")
