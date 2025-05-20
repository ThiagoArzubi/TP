import os
os.system ("cls")


#CALCULAR TIEMPO DE ENCUENTRO
print("------------------------------------")
print(" Complemento 5: TIEMPO DE ENCUENTRO")
print("------------------------------------")
print("")

v1 = float(input("V1: "))
v2 = float(input("V2: "))
d = float(input("Distancia: "))

if v1 > 0 and v2 > 0:
    t = d / (v1 + v2)
    print(t, "segundos")
else:
    print("ERROR")