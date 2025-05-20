import os
os.system ("cls")


#CALCULAR COSTO DE ARTICULO
print("----------------------------------")
print(" Complemento 3: COSTO DE ARTICULO")
print("----------------------------------")
print("")

costo = float(input("Ingrese el Costo del artículo: "))
m = input("Ingrese la marca: ")

if costo >= 2000 and m == "NOSY":
    pa = costo * 0.90
    pt = pa * 0.95
elif costo >= 2000 and m != "NOSY":
    pt = costo * 0.90
elif costo < 2000 and m == "NOSY":
    pa = costo * 0.95
    pt = pa + pa * 0.20
else:
    pt = costo * 1.20

print("Usted pagará:",pt, "soles")