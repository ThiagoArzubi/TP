import os,math
os.system ("cls")


#CALCULAR TRIANGULO O CIRCULO
print("------------------------------------")
print(" Complemento 8: TRIANGULO O CIRCULO")
print("------------------------------------")
print("")

print("1: Área del triángulo")
print("2: Área del círculo")

opc = int(input("Opción: "))

if opc == 1:
    l = float(input("Ingrese el lado del triángulo: "))
    A = (math.sqrt(3)/4) * l**2
    print("Área del triángulo:", A)
elif opc == 2:
    r = float(input("Ingrese el radio del círculo: "))
    C = math.pi * r**2
    print("Área del círculo:", C)
else:
    print("Error: opción inválida")