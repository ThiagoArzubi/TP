import os
os.system ("cls")


#CALCULAR DISTANCIA DE DOS PUNTOS EN 3D
print("-----------------------------------------------")
print(" COMPLEMENTO 10: DISTANCIA DE DOS PUNTOS EN 3D")
print("-----------------------------------------------")
print("")
print("Le pediremos que ingrese los valores del primer punto")
x1=float(input("Ingrese los valores de x1: "))
y1=float(input("Ingrese los valores de y1: "))
z1=float(input("Ingrese los valores de z1: "))
print("Ahora le pediremos lo mismo, pero del segundo punto")
x2=float(input("Ingrese los valores de x2: "))
y2=float(input("Ingrese los valores de y2: "))
z2=float(input("Ingrese los valores de z2: "))
dis = ((z2-z1)**2+(y2-y1)**2+(x2-x1)**2)**0.5
print("La distancia es:",dis)