import os,math
os.system ("cls")


#CALCULAR TERCER LADO DE UN TRIANGULO
print("---------------------------------------------")
print(" COMPLEMENTO 7: TERCER LADO DE UN TRIANGULO")
print("---------------------------------------------")
print("")
#B - C - A SON LOS LADOS
pi=3.1416
b=int(input("Ingresa el lado del triangulo: "))
c=int(input("Ingrese el segundo lado: "))
alfa=float(input("Ingrese el angulo en grados sexagesimales: "))
a=(b**2+c**2-2*b*c*math.cos(alfa*pi/180))**0.5
print("el lado A es:",a)