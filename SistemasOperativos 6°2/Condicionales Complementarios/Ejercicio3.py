import os
os.system ("cls")


#CALCULAR COSTO DE ARTICULOS
print("----------------------------------")
print(" Complemento 3: COSTO DE ARTICULO")
print("----------------------------------")
print("")

costo=float(input("Ingrese el costo: "))
marca=str(input("Ingrese la marca: ")).capitalize
if costo >= 2000 and marca=="Nike":
    total=(costo*0.90)*0.95
    print("Usted pagara:",total)
else:
    if costo >= 2000 and marca!="Nike":
        total=costo*0.90
        print("Usted pagara:",total)
    else:
        if costo < 2000 and marca=="Nike":
            total=((costo*0.95)+(costo*0.95))*0.20
            print("Usted pagara:",total)
        else:
            if costo < 2000 and marca!="Nike":
                total=costo*1.20
                print("Usted pagara:",total)
            else:
                exit