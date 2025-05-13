import os
os.system ("cls")


#DETERMINAR LA SALIDA
print("-----------------------------------")
print(" EJERCICIO 4: DETERMINAR LA SALIDA")
print("-----------------------------------")
print("")
n=int(input("introduce un numero: "))
while n>0:
    resto=n%10
    print(resto)
    n=n//10