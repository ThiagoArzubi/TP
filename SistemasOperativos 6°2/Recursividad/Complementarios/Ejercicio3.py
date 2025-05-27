import os
os.system ("cls")


#CALCULAR CUBO DE UN NUMERO PRIIMO
print("-------------------------------------------------")
print(" Complemento 3: CALCULAR CUBO DE UN NUMERO PRIMO")
print("-------------------------------------------------")
print("")

b = 2
for i in range(1,29):
    cont = 0
    for a in range(2,b//2): 
        if b%a == 0:
            cont = cont + 1
            a=b
    if cont == 0:
        print(f"El cubo de {b} es {b**3}")
    b = b + 1