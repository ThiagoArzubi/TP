import os
os.system ("cls")


#CONTAR NUMEROS PARES
print("--------------------------------")
print(" Complemento 6: INVERTIR NUMERO")
print("--------------------------------")
print("")

aux = 0
aux2 = 0
n = int(input("Ingrese un numero:"))
i = 10
while i <=n:
    aux = n%10
    n = n//10
    aux2 = aux2*10+aux
aux2 = aux2*10+n
print(f"El numero invertido sera: {aux2}")