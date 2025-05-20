import os
os.system ("cls")


#CALCULAR CONTROL DE STOCK EN UNA TIENDA
print("-------------------------------------------------------")
print(" INTEGRADOR 5: CALCULAR CONTROL DE STOCK EN UNA TIENDA")
print("-------------------------------------------------------")
print("")

stock = int(input("Stock inicial: "))
inicial = stock

while stock > 0:
    venta = int(input("Cantidad vendida (0 para salir): "))
    if venta == 0:
        break
    if venta <= stock:
        stock -= venta
    else:
        print("Venta excede el stock.")

    if stock < inicial * 0.1:
        print("Alerta: queda menos del 10% del stock.")

print("Stock final:", stock)