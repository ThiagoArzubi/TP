import os
os.system("cls")
lista=[]
caracter=0
while True:
    caracter=int(input("Ingrese un numero: "))
    print("para cerrar el programa es necesario ingresar un numero negativo")
    if caracter >= 0:
        lista.append(caracter)
        print (lista)
    else:
        print("cerrando el programa....")
        break
    