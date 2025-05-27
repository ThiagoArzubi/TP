import os
os.system ("cls")


#CALCULAR TRIANGULO O CIRCULO
print("------------------------------------")
print(" Complemento 8: TRIANGULO O CIRCULO")
print("------------------------------------")
print("")

print("1: Area del triangulo - 2:Area del circulo")
opc=int(input("Ingrese el numero de lo que desea realizar: "))
if opc == 1:
    lado=float(input("Ingrese el lado del triangulo: "))
    area=((3**0.5)/4)*lado**2
    print("El area del triangulo es:",area)
elif opc == 2:
    radio=float(input("Ingrese el radio del circulo: "))
    area=3.1416*radio**2
    print("El area del circulo es:",area)
else:
    print("Error")