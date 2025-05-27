import os
os.system ("cls")


#CONVERSOR DE UNIDADES
print("------------------------------------")
print(" EJERCICIO 2: CONVERSOR DE UNIDADES")
print("------------------------------------")
print("")

def convertir():
    print("1. Libras a Kilogramos")
    print("2. Kilómetros a Millas")
    print("3. Celsius a Fahrenheit")
    opcion = input("Seleccione una opción (1/2/3): ")

    if opcion == "1":
        libras = float(input("Ingrese el peso en libras: "))
        print(f"{libras} libras = {libras * 0.4536:.2f} kg")
    elif opcion == "2":
        km = float(input("Ingrese la distancia en kilómetros: "))
        print(f"{km} km = {km * 0.621371:.2f} millas")
    elif opcion == "3":
        celsius = float(input("Ingrese la temperatura en Celsius: "))
        print(f"{celsius}°C = {(celsius * 9/5) + 32:.2f}°F")
    else:
        print("Opción no válida")

convertir()
