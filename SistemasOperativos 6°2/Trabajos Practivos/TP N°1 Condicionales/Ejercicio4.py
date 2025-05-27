import os
os.system ("cls")


#CAJERO AUTOMATICO BASICO
print("--------------------------------------------------")
print(" EJERCICIO 4: CAJERO AUTOMATICO BASICO")
print("--------------------------------------------------")
print("")

st = float(input("Ingrese el saldo total de su cuenta: "))
sr = float(input("Ingrese la cantidad de saldo que desea retirar: "))

if st > sr:
    print("Ha retirado", sr ,"correctamente")
elif sr > st:
    print ("Dinero insuficiente en la cuenta")