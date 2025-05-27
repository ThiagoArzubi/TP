import os
os.system ("cls")


#CALCULAR TIEMPO DE ENCUENTRO
print("------------------------------------")
print(" Complemento 5: CALCULAR TIEMPO DE ENCUENTRO")
print("------------------------------------")
print("")

v1=float(input("Ingrese la velocidad del primer vehiculo: "))
v2=float(input("Ingrese la velocidad del segundo vehiculo: "))
d=float(input("Ingrese la distancia que los separa: "))
if v1>0 and v2>0:
    t=d/(v1+v2)
    print(t)
else:
    print("Error")