#Programa para saber si tenes que tributar o no

edad=int(input("ingrese su edad: "))
ing=int(input("ingrese sus ingresos mensuales: "))
if edad>=16 and ing>=1000:
    print("Usted tiene que tributar")
else:
    print("Usted no tiene los requerimientos necesarios para tributar")
