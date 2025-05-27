import os
os.system ("cls")


#CALCULAR IGUALES O DISTINTOS
print("------------------------------------")
print(" Complemento 1: IGUALES O DISTINTOS")
print("------------------------------------")
print("")

num1=int(input("Ingrese el primer numero: "))
num2=int(input("Ingrese el segundo numero: "))
num3=int(input("Ingrese el tercer numero: "))
if num1+num2==num3:
    print("Iguales")
else:
    print("Distintos")