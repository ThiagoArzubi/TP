import os
os.system("cls")
N=int(input("Que cantidad de numeros le gustaria ingresar?: "))
menor=999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
mayor=0
promedio=0
for l in range (N):
    num=int(input("Ingresa cualquier numero: "))
    if num < menor:
        menor=num
    elif num > mayor:
        mayor=num
    promedio=promedio+num
media=promedio/N
print("El numero mayor es:",mayor)
print("El numero menor es:",menor)
print("La media es:",media)