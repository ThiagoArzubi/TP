import os
os.system ("cls")


#MOSTRAR DE MENOR A MAYOR
print("-----------------------------------------")
print(" Complemento 2: MOSTRAR DE MENOR A MAYOR")
print("-----------------------------------------")
print("")

a = int(input("Ingrese a: "))
b = int(input("Ingrese b: "))

if a < b:
    print("Los números son:", a, b)
else:
    print("Los números son:", b, a)