import os
os.system("cls")




#Preguntamos si el que desea ingresar es el propietario o un cliente




# Inicializamos la lista de pedidos
pedidos = []

# Función para agregar un nuevo pedido
def agregar_pedido():
    cliente = input("Ingrese el nombre del cliente: ")
    producto = input("Ingrese el nombre del producto: ")
    cantidad = int(input("Ingrese la cantidad: "))
    pedido = {"cliente": cliente, "producto": producto, "cantidad": cantidad}
    pedidos.append(pedido)
    print("Pedido agregado con éxito.")

# Función para eliminar un pedido
def eliminar_pedido():
    cliente = input("Ingrese el nombre del cliente del pedido que desea eliminar: ")
    for pedido in pedidos:
        if pedido["cliente"] == cliente:
            pedidos.remove(pedido)
            print("Pedido eliminado con éxito.")
            return
    print("Pedido no encontrado.")

# Función para mostrar todos los pedidos
def mostrar_pedidos():
    if not pedidos:
        print("No hay pedidos en la agenda.")
    else:
        for idx, pedido in enumerate(pedidos, start=1):
            print(f"Pedido {idx}: Cliente: {pedido['cliente']}, Producto: {pedido['producto']}, Cantidad: {pedido['cantidad']}")

# Función principal que muestra el menú y maneja la interacción del usuario
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




# Ejecutamos el menú
if __name__ == "__main__":
    menu()
