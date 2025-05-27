import os
os.system ("cls")


#CALCULADORA DE PROPINAS
print("--------------------------------------")
print(" EJERCICIO 1: CALCULADORA DE PROPINAS")
print("--------------------------------------")
print("")

cuenta = float(input("Ingrese el total de la cuenta: "))
porcentaje = float(input("Ingrese el porcentaje de propina que desea dejar: "))

propina = cuenta * (porcentaje / 100)
total = cuenta + propina

print(f"Propina: ${propina:.2f}")
print(f"Total a pagar: ${total:.2f}")