import os
os.system ("cls")


#DIAS LABORALES O NO LABORALES
print("--------------------------------------------")
print(" EJERCICIO 5: DIAS LABORALES O NO LABORALES")
print("--------------------------------------------")
print("")
print("-----------------------------------------------")
print(" Tomando en cuenta que 1 = Lunes y 7 = Domingo")
print("-----------------------------------------------")
d = float(input("Ingrese un numero del 1 al 7: "))
if d > 0 and d < 8:
    if d >= 1 and d <= 5:
        print("Dia laboral")
    elif d >= 6 and d <= 7:
        print("Fin de semana")
