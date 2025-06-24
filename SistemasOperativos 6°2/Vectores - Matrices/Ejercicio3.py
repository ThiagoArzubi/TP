import os
os.system("cls")
#Decoración: Nombre del Algoritmo
print("----------------------------------------------------------")
print(" Vector3: ORDENAR Y QUITAR ELEMENTOS REPETIDOS DEL VECTOR")
print("----------------------------------------------------------")
print("")

VEC = []
print("Ingrese número de elementos del vector")
N = int( input())

if 1 <= N and N <= 200:
    for i in range(1,N+1):
        elemento = int( input("Ingrese Entero {0}: ".format(i)))
    VEC.append(elemento)
    i = 0
    #TODO:
    lista_nueva = [] 
    for elemento in VEC:

        if elemento not in lista_nueva:
            lista_nueva.append(elemento)

lista_nueva.sort()

print(lista_nueva)