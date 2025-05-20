import os
os.system ("cls")


#NUMEROS, EL PRIMERO DECIDE
print("-------------------------------------------")
print(" Complemento 6: NUMEROS, EL PRIMERO DECIDE")
print("-------------------------------------------")
print("")

a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

if a < 0:
    r = a * b * c
else:
    r = a + b + c

print("Resultado:",r)