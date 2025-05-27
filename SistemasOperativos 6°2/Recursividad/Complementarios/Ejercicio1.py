import os
os.system ("cls")


#CONTAR NUMEROS PARES
print("-------------------------------------")
print(" Complemento 1: CONTAR NUMEROS PARES")
print("-------------------------------------")
print("")

cant = 0
for contador in range(10):
    valor = int(input(f"Ingrese el número #{contador + 1}: "))
    if valor % 2 == 0:
        cant += 1

print("Total de números pares ingresados: ",cant)