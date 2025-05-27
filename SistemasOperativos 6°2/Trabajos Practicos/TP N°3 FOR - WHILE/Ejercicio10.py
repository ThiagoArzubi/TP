import os
os.system ("cls")


#SIMULAR MENU CON DO-WHILE
print("-----------------------------------------")
print(" EJERCICIO 10: SIMULAR MENU CON DO-WHILE")
print("-----------------------------------------")
print("")

while True:
    print("\nMenú:")
    print("1. Saludar")
    print("2. Mostrar número secreto")
    print("3. Salir")

    opcion = input("Elegí una opción: ")

    if opcion == "1":
        print("¡Hola!")
    elif opcion == "2":
        print("El número secreto es 42.")
    elif opcion == "3":
        print("Saliendo...")
        break
    else:
        print("Opción no válida.")