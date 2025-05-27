import os
os.system ("cls")


#CALCULADORA DE PRESUPUESTO
print("--------------------------------------------------")
print(" EJERCICIO 4: CALCULADORA DE PRESUPUESTO")
print("--------------------------------------------------")
print("")

ingresos = float(input("Ingrese sus ingresos mensuales: "))
gastos = {}

while True:
    cat = input("Categoría de gasto (o 'salir' para terminar): ")
    if cat.lower() == "salir":
        break
    monto = float(input(f"Ingrese el monto para {cat}: "))
    gastos[cat] = gastos.get(cat, 0) + monto

total_gastos = sum(gastos.values())
saldo = ingresos - total_gastos

print(f"\nGastos totales: ${total_gastos:.2f}")
print(f"Saldo disponible: ${saldo:.2f}")

for cat, monto in gastos.items():
    porcentaje = (monto / ingresos) * 100
    print(f"{cat}: ${monto:.2f} ({porcentaje:.1f}%)")