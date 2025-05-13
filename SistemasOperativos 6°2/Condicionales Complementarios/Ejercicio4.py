import os
os.system ("cls")


#CALCULAR EL DIA QUE SIGUE
print("------------------------------------------")
print(" Complemento 4: CALCULAR EL DIA QUE SIGUE")
print("------------------------------------------")
print("")

año=int(input("Ingrese el año: "))
mes=int(input("Ingrese el mes: "))
dia=int(input("Ingrese el dia: "))
if dia>0 and dia<30:
    print(dia+1,mes,año)
else:
    if mes>0 and mes<12:
        print(1,mes+1,año)
    else:
        print(1,1,año+1)

