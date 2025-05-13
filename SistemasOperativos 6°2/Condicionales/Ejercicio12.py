import os
os.system ("cls")


#CALCULAR SUELDO A PERCIBIR
print("---------------------------------")
print(" EJERCICIO 12: SUELDO A PERCIBIR")
print("---------------------------------")
print("")
sueldo=float(input("Ingrese su sueldo:"))
if sueldo < 1000:
    sueldo=sueldo+(sueldo*0.15)
    print("Su sueldo es:",sueldo)
else:
    print("Su sueldo es mayor a 1000. No recibe aumento")