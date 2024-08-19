import os
os.system("cls")
print("Que operacion desea hacer?")
print("1. Suma")
print("2. Resta")
print("3. Multiplicacion")
print("4. Division")
print("5. Potenciacion")
print("6. Sacar raiz")
opcion=int(input("Seleccione una opcion (1-6): "))
def suma(num1,num2):
    res=num1+num2
    print("El numero es:",res)
def resta(num1,num2):
    res=num1-num2
    print("El numero es:",res)
def multiplicacion(num1,num2):
    res=num1+num2
    print("El numero es:",res)
def div(num1,num2):
    res=num1/num2
    if num2 == 0:
        print ("No se puede dividir por 0. Ingrese otra operacion")
    print("El numero es:",res)
def potencia(num1,num2):
    res=num1**num2
    print("El numero es:",res)
def raiz(num1,num2):
    res=num1**(1/num2)
    if num2 == 0:
        print("el indice de una raiz no puede ser 0. Ingrese otra operacion")
    print("El numero es:",res)








if opcion == 1:
    num1=int(input("ingrese el primer numero: "))
    num2=int(input("ingrese el segundo numero: "))
    suma(num1,num2)
elif opcion == 2:
    num1=int(input("ingrese el primer numero: "))
    num2=int(input("ingrese el segundo numero: "))
    resta(num1,num2)
elif opcion == 3:
    num1=int(input("ingrese el primer numero: "))
    num2=int(input("ingrese el segundo numero: "))
    multiplicacion(num1,num2)
elif opcion == 4:
    num1=int(input("ingrese el dividendo: "))
    num2=int(input("ingrese el divisor: "))
    div(num1,num2)
elif opcion == 5:
    num1=int(input("ingrese la base: "))
    num2=int(input("ingrese el exponente: "))
    potencia(num1,num2)
elif opcion == 6:
    num1=int(input("ingrese el radicando: "))
    num2=int(input("ingrese el indice: "))
    raiz(num1,num2)
else:
    print("A seleccionado una opcion que no existe. Vuelva a ingresar una opcion.")