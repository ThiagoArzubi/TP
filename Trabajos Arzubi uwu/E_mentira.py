import os
os.system("cls")
suma=0
ans=int(input("Ingrese el numero de veces que desea que la serie se repita:"))
for i in range(1,ans):
    suma = suma+i/2**i
print(suma)