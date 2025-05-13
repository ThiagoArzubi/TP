#Programa para calcular promedio y saber si está aprobado o no

num1=int(input("Ingrese la primer nota: "))
num2=int(input("Ingrese la segunda nota: "))
num3=int(input("Ingrese la tercera nota: "))
num4= (num1+num2+num3)/3
if num4 >= 7:
    print("Usted esta aprobado")
elif num4 >=4:
    print("regular")
else:
    print("Usted está desaprobado")
