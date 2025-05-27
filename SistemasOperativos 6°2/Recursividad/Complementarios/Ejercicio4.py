import os
os.system ("cls")


#CALCULAR SUMA DE SERIE
print("---------------------------------------")
print(" Complemento 4: CALCULAR SUMA DE SERIE")
print("---------------------------------------")
print("")

n = int(input("Ingrese el numero de terminos: "))
s = 5
ser = 0
for a in range(1,n+1):
    s = s + 5
    ser = ser + s
print(f"La suma sera: {ser}")