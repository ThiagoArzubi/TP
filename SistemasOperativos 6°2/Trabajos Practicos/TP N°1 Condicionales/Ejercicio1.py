import os
os.system ("cls")


#CLASIFICACION DE EDAD EN CATEGORIAS
print("--------------------------------------------------")
print(" EJERCICIO 1: CLASIFICACION DE EDAD EN CATEGORIAS")
print("--------------------------------------------------")
print("")
edad=int(input("Ingrese la edad: "))
if edad < 18:
    print("Menor de edad")
elif edad >= 18 and edad <= 64:
    print("Adulto")
elif edad >= 65:
    print("Adulto Mayor")