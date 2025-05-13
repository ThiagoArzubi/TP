import os
os.system ("cls")


#CALCULAR TIEMPO DE ENCUENTRO
print("------------------------------------")
print(" COMPLEMENTO 8: TIEMPO DE ENCUENTRO")
print("------------------------------------")
print("")
va=float(input("Ingrese la velocidad de A: "))
vb=float(input("Ingrese la velocidad de B: "))
d=float(input("Cual es la distancia que separa ambos lados?: "))
te= d/(va+vb)
print("Los cuerpos se encontraran en:",te,"segundos")