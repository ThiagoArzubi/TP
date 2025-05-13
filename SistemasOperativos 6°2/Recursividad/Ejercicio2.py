import os
os.system ("cls")


#CALCULAR LA SUMA DE DIVISORES
print("-------------------------------------------")
print(" EJERCICIO 1: CALCULA LA SUMA DE DIVISORES")
print("-------------------------------------------")
print("")

print("Si desea cerrar el programa, ingrese un numero negativo")
print("")
num=int(input("ingrese un numero: "))
while num>0:
    suma=0
    for i in range(1,num+1):
        if num % i==0:
            suma=suma+i
    print("la suma de los divisores del numero es:" ,suma)
    print("Si desea cerrar el programa, ingrese un numero negativo")
    print("")
    num=int(input("ingrese un numero: "))
    