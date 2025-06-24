import os
os.system("cls")
#Decoración: Nombre del Algoritmo
print("-----------------------------------------")
print(" Vector1: LECTURA DE N ELEMENTOS ENTEROS")
print("-----------------------------------------")
print("")
i=1
F=[]
# ne = Numero de elementos
ne = int(input("Ingrese el numero de elementos a ingresar: "))

while i <= ne:
    elemento = int(input("Ingrese elemento: "))
    F.append(elemento)
    i = i + 1
print(F)


