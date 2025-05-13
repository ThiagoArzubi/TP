import os
os.system ("cls")


#CALCULAR FUNCIÓN
print("-----------------------")
print(" EJERCICIO 14: FUNCIÓN")
print("-----------------------")
print("")
num=int(input("Ingrese el calculo que desea realizar:"))
print("1= Multiplicacion - 2= Potenciacion - 3= División")
v=int(input("Ingrese un valor:"))
if num == 1:
    val=100*v
elif num==2:
    val=100**v
elif num == 3:
    if v != 0:
        val=100/v
    else:
        print("No se puede dividir por cero")
else:
    val=0
print("El valor es:",val)