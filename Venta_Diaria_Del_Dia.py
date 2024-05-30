import os,time,sys
def bdc(tiempo):
    print("Cargando:")
    for i in range(101):
        time.sleep(tiempo / 100)
        sys.stdout.write("\r%d%%" % i)
        sys.stdout.flush()
    print()
precios=0
while True:
    os.system("cls")
    while True:
        producto=int(input("ingrese el valor del producto: "))
        precios=precios+producto
        if producto==0:
            break 
    IVA= precios/100*21
    beneficios= precios/100*41
    resto= precios-(beneficios+IVA)
    print()
    print("El dinero total obtenido es:",precios,)
    print("El impuesto iva es:",IVA,)
    print("Los beneficios obtenidos son:",beneficios,)
    print("El dinero restante para comprar mercaderia es:",resto,)
    print()
    answer=input("Desea cerrar la aplicacion? >").capitalize()
    if answer=="No":
        os.system("cls")
        bdc(5)
        continue
    elif answer=="Si":
        break
    else:
        print("Escribi bien pelotudo")