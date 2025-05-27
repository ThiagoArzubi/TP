import os
os.system ("cls")


#NUMEROS, EL PRIMERO DECIDE
print("-------------------------------------------")
print(" Complemento 6: NÚMEROS, EL PRIMERO DECIDE")
print("-------------------------------------------")
print("")

n1=int(input("Ingrese el primer numero: "))
n2=int(input("Ingrese el segundo numero: "))
n3=int(input("Ingrese el tercer numero: "))
if n1<0:
    r=n1*n2*n3
else:
    r=n1+n2+n3
print(r)