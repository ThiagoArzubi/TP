import os
os.system ("cls")


#DETERMINAR SI UN NUMERO ES PRIMO
print("-----------------------------------------------")
print(" EJERCICIO 5: DETERMINAR SI UN NUMERO ES PRIMO")
print("-----------------------------------------------")
print("")

numero = int(input("Ingresa un número: "))

es_primo = True

if numero < 2:
    es_primo = False
else:
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            es_primo = False
            break

if es_primo:
    print(f"{numero} es un número primo.")
else:
    print(f"{numero} no es un número primo.")