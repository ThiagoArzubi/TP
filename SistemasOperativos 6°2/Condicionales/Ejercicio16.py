import os
os.system ("cls")


#CALCULAR SI UN ALUMNO ESTA APROBADO
print("------------------------------------")
print(" EJERCICIO 16: DETERMINAR LA SALIDA")
print("------------------------------------")
print("")
a=int(input("Ingresa el valor de A: "))
b=int(input("Ingresa el valor de B: "))
c=int(input("Ingresa el valor de C: "))

if a > b:
    if a>c:
        if b>c:
            print (a,b,c)
        else: print(a,c,b)
    else: print(c,a,b)
else:
    if b>c:
        if a>c:
            print(b,a,c)
        else:
            print(b,c,a)
    print(c,b,a)

