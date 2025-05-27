import os
os.system ("cls")


#CALCULAR EL PROMEDIO DE POSITIVOS Y NEGATIVOS
print("------------------------------------------------------------")
print(" EJERCICIO 7: CALCULAR EL PROMEDIO DE POSITIVOS Y NEGATIVOS")
print("------------------------------------------------------------")
print("")

positivos = []
negativos = []
for _ in range(10):
    num = float(input("Ingresá un número: "))
    if num > 0:
        positivos.append(num)
    elif num < 0:
        negativos.append(num)
if positivos:
    print(f"Promedio positivos: {sum(positivos)/len(positivos):.2f}")
else:
    print("No hay números positivos.")
if negativos:
    print(f"Promedio negativos: {sum(negativos)/len(negativos):.2f}")
else:
    print("No hay números negativos.")