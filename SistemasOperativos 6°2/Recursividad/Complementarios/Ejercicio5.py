import os
os.system ("cls")


#CALCULAR SUMA DE SERIE 2
print("-----------------------------------------")
print(" Complemento 5: CALCULAR SUMA DE SERIE 2")
print("-----------------------------------------")
print("")

s = 0
n = int(input("Ingrese el numero de terminos: "))
for x in range (1,n+1):
    if x%2 == 0:
        s = s-(1/x)
    else:
        s = s+(1/x)
print(f"La suma sera: {s}")    
