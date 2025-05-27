import os
os.system ("cls")


#CALCULAR RAÍCES DE ECUACIÓN CUADRÁTICA
print("----------------------------------------------")
print(" Complemento 7: RAÍCES DE ECUACIÓN CUADRÁTICA")
print("----------------------------------------------")
print("")

a=float(input("Ingrese el primer valor: "))
b=float(input("Ingrese el segundo valor: "))
c=float(input("Ingrese el tercer valor: "))
d=(b**2)-(4*a*c)
if d>0:
    x1=((-b)+d**0,5)/2*a
    x2=((-b)-d**0,5)/2*a
print("Racies iguales:",x1,x2)