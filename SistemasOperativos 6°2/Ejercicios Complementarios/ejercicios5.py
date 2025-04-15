import os
os.system ("cls")


#CALCULAR MONTO A PAGAR
print("-------------------------------------------------")
print(" COMPLEMENTO 5: CALCULAR MONTO A PAGAR")
print("-------------------------------------------------")
print("")
#P=PRECIO TOTAL - C=COSTO DEL PRODUCTO - D=DOCENAS
c=float(input("Ingrese costo unitario del articulo: "))
d=input("Ingrese el numero de docenas: ")
p=d*12*c
print("el precio del articulo es:",p)