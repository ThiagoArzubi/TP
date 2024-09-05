import os
os.system("cls")

chango={
    "Papas":2999.99,
    "VelasX10":1999.99,
    "Vino":1999.99,
    "Fernet 1L":9999.99,
    "Bondiola x kg":6200.00,
    "Fideos Tallarines 500g":2300.00,
    "Copos de maiz azucarados 490g":3535.00,
}

productos=[]
papas=0
velas=0
vino=0
fernet=0
bondiola=0
fideo=0
cereal=0
#Preguntamos si el que desea ingresar es el propietario o un cliente



pedidos = []

def agregar_pedido():
    Borrado = False 
    cliente = input("Ingrese el nombre del cliente: ")
    stock()
    producto = input("Ingrese el numero del producto: ")
    cantidad = int(input("Ingrese la cantidad: "))
    pedido = {"cliente": cliente, "producto": producto, "cantidad": cantidad, "eliminado": Borrado}
    pedidos.append(pedido)
    print("Pedido agregado con éxito.")

def eliminar_pedido():
    print("")
    cliente = input("Ingrese el nombre del cliente del pedido que desea eliminar: ")
    for pedido in pedidos:
        if pedido["cliente"] == cliente and not pedido["eliminado"]:
            pedido ["eliminado"]=True
            print("")
            print("Pedido eliminado con éxito.")
            return
    print("Pedido no encontrado.")

def mostrar_pedidos():
    if not pedidos:
        print("No hay pedidos en la agenda.")
    else:
        for idx, pedido in enumerate(pedidos, start=1):
            print(f"Pedido {idx}: Cliente: {pedido['cliente']}, Producto: {pedido['producto']}, Cantidad: {pedido['cantidad']}, Borrado: {pedido['eliminado']}")

def menu():
    while True:
        print("\nAgenda de Pedidos")
        print("1. Agregar pedido")
        print("2. Eliminar pedido")
        print("3. Mostrar pedidos")
        print("4. Salir")
        
        opcion = input("Seleccione una opción (1-4): ")
        
        if opcion == "1":
            agregar_pedido()
        elif opcion == "2":
            eliminar_pedido()
        elif opcion == "3":
            mostrar_pedidos()
        elif opcion == "4":
            print("Saliendo de la agenda.")
            break
        else:
            print("Opción no válida. Por favor, elija una opción del menú.")

def stock():
    print("Productos disponibles: ")
    print("1. Papas $2.999,99")
    print("2. VelasX10 $1.999,99")
    print("3. Vino $1.999,99")
    print("4. Fernet 1L $9.999,99")
    print("5. Bondiola x kg 6.200,00")
    print("6. Fideos Tallarines 500g $2.300,00")
    print("7. Copos de maiz azucarados 490g $3.535,00")

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
        volver=str(input("Desea ingresar otro producto?(Si/No): ")).lower()
        if volver == "si":
            continue
        else:
            break

if __name__ == "__main__":
    menu()
