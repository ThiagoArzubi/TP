renta=int(input("Ingrese su renta anual: "))
if renta<10000:
    print("Le corresponde 5% de tipo impositivo")
elif renta>10000 and renta<20000:
    print("Le corresponde 15% de tipo impositivo")
elif renta>20000 and renta<35000:
    print("Le corresponde 20% de tipo impositivo")
elif renta>35000 and renta<60000:
    print("Le corresponde 30% de tipo impositivo")
else:
    print("A usted le corresponde 45% de tipo impositivo")