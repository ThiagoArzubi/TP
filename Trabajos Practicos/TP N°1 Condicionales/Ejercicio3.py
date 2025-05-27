import os
os.system ("cls")


#MENU DE RESTAURANTE
print("----------------------------------")
print(" EJERCICIO 3: MNEU DE RESTAURANTE")
print("----------------------------------")
print("")
print("----------------------")
print(" MENU DEL RESTAURANTE")
print("----------------------")
print("")
print("1. Hamburguesa completa")
print("2. Pizza tradicional")
print("3. Ensalada de papa y huevo")
print("4. Salir")
while True:
    selec = float(input("Ingrese una de las opciones: "))

    if selec == 1:
        print("Una vez hecha se le enviara a su mesa. ¡Muchas gracias por la espera!")
    elif selec == 2:
        print("Una vez hecha se le enviara a su mesa. ¡Muchas gracias por la espera!")
    elif selec == 3:
        print("Una vez hecha se le enviara a su mesa. ¡Muchas gracias por la espera!")
    elif selec == 4:
        print("Saliendo del programa....")
        break
    else:
        print("Eliga una opcion correcta")