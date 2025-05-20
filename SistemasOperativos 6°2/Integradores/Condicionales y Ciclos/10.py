import os
os.system ("cls")


#CONTROL DE COMBUSTIBLE DE UN VEHICULO
print("------------------------------------------------------")
print(" INTEGRADOR 10: CONTROL DE COMBUSTIBLE DE UN VEHICULO")
print("------------------------------------------------------")
print("")

combustible = 0
print("Simulación de carga y consumo de combustible (0 para salir)")

while True:
    opcion = input("¿Cargar (c), Consumir (x), Salir (0)? ").lower()
    if opcion == '0':
        break
    elif opcion == 'c':
        litros = float(input("Litros cargados: "))
        combustible += litros
    elif opcion == 'x':
        uso = float(input("Litros consumidos: "))
        if uso <= combustible:
            combustible -= uso
        else:
            print("¡No hay suficiente combustible!")
    else:
        print("Opción inválida.")

if combustible >= 50 * 0.07:
    print("Combustible suficiente para 50 km.")
else:
    print("¡Advertencia! No hay combustible suficiente para 50 km.")