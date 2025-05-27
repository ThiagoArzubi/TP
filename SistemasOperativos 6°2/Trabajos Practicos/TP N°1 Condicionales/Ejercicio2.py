import os
os.system ("cls")


#VERIFICACION DE VELOCIDAD PERMITIDA
print("--------------------------------------------------")
print(" EJERCICIO 2: VERIFICACIÓN DE VELOCIDAD PERMITIDA")
print("--------------------------------------------------")
print("")

vp = float(input("Ingrese la velocidad de su vehiculo: "))
if vp >=0 and vp <= 60:
    print("Está dentro del limite permitido")
elif vp >= 61 and vp <= 80:
    print("Está en exceso leve")
else:
    print("Está en exceso grave")