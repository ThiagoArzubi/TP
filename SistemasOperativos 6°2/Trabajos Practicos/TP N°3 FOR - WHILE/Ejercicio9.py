import os
os.system ("cls")


#CONTADOR DE TEMPERATURAS
print("---------------------------------------")
print(" EJERCICIO 9: CONTADOR DE TEMPERATURAS")
print("---------------------------------------")
print("")

bajo_cero = calor = 0
while True:
    temp = float(input("Ingresá una temperatura (-100 para salir): "))
    if temp == -100:
        break
    if temp < 0:
        bajo_cero += 1
    elif temp >= 30:
        calor += 1
print(f"Temperaturas bajo cero: {bajo_cero}, Mayores o iguales a 30: {calor}")