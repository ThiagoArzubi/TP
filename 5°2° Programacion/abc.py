def chango1():
    while True:
        np=str(int("Ingresa el numero del producto: "))
        cp=int(input("Ingresa la cantidad de pedidos (en numeros): ")) 
        if np == 1: 
            papas+=cp
            pt=cp*2999.99
        elif np == 2:
            velas+=cp
            pt=cp*1999.99
        elif np == 3:
            vino+=cp
            pt=cp*1999.99
        elif np == 4:
            fernet+=cp
            pt=cp*9999.99
        elif np == 5:
            bondiola+=cp
            pt=cp*6200.00
        elif np == 6:
            fideo += cp
            pt=cp*2300.00
        elif np == 7:
            cereal += cp
            pt=cp*3535.00
        pito=str(input("Desea ingresar otro producto?(Si/No): ")).lower()
        if pito == "si":
            continue
        else:
            break
    
chango={
    "Papas":2999.99,
    "VelasX10":1999.99,
    "Vino":1999.99,
    "Fernet 1L":9999.99,
    "Bondiola x kg":6200.00,
    "Fideos Tallarines 500g":2300.00,
    "Copos de maiz azucarados 490g":3535.00,
}

def stock():
    print("Productos disponibles: ")
    print("1. Papas $2.999,99")
    print("2. VelasX10 $1.999,99")
    print("3. Vino $1.999,99")
    print("4. Fernet 1L $9.999,99")
    print("5. Bondiola x kg 6.200,00")
    print("6. Fideos Tallarines 500g $2.300,00")
    print("7. Copos de maiz azucarados 490g $3.535,00")