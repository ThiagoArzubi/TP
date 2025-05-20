import os
os.system ("cls")


#CALCULAR RAICES DE ECUACION CUADRATICA
print("----------------------------------------------")
print(" Complemento 7: RAICES DE ECUACION CUADRATICA")
print("----------------------------------------------")
print("")

a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

d = b**2 - 4*a*c

if d > 0:
    x1 = (-b + d**0.5) / (2*a)
    x2 = (-b - d**0.5) / (2*a)
    print("Raíces reales:", x1, x2)
else:
    print("Raíces Irracionales")
