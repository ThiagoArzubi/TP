Aquí tienes el código completo que combina tu código original con la nueva función que calcula el total a pagar basado en los productos y cantidades:

```python
import os
os.system("cls")

chango = {
    "1": {"nombre": "Papas", "precio": 2999.99},
    "2": {"nombre": "VelasX10", "precio": 1999.99},
    "3": {"nombre": "Vino", "precio": 1999.99},
    "4": {"nombre": "Fernet 1L", "precio": 9999.99},
    "5": {"nombre": "Bondiola x kg", "precio": 6200.00},
    "6": {"nombre": "Fideos Tallarines 500g", "precio": 2300.00},
    "7": {"nombre": "Copos de maiz azucarados 490g", "precio": 3535.00}
}

pedidos = []

def agregar_pedido():
    cliente = input("Ingrese el nombre del cliente: ")
    stock()

    producto = input("Ingrese el numero del producto: ")
    cantidad = int(input("Ingrese la cantidad: "))
    pedido = {"cliente": cliente, "producto": producto, "cantidad": cantidad, "eliminado": False}
    pedidos.append(pedido)
    print("Pedido agregado con éxito.")

def eliminar_pedido():
    print("")
    cliente = input("Ingrese el nombre del cliente del pedido que desea eliminar: ")
    for pedido in pedidos:
        if pedido["cliente"] == cliente and not pedido["eliminado"]:
            pedido["eliminado"] = True  # Eliminación lógica
            print("")
            print("Pedido eliminado lógicamente con éxito.")
            return
    print("Pedido no encontrado o ya eliminado.")

def mostrar_pedidos():
    if not pedidos:
        print("No hay pedidos en la agenda.")
    else:
        for idx, pedido in enumerate(pedidos, start=1):
            if not pedido["eliminado"]:
                print(f"Pedido {idx}: Cliente: {pedido['cliente']}, Producto: {pedido['producto']}, Cantidad: {pedido['cantidad']}")

def calcular_total():
    total = 0
    while True:
        stock()
        np = input("Ingresa el número del producto: ")
        if np not in chango:
            print("Producto no válido. Inténtalo de nuevo.")
            continue

        cp = int(input("Ingresa la cantidad de pedidos (en números): "))
        
        # Calculamos el costo por producto y sumamos al total
        precio_producto = chango[np]["precio"]
        subtotal = cp * precio_producto
        total += subtotal

        print(f"Producto: {chango[np]['nombre']}, Cantidad: {cp}, Subtotal: ${subtotal:.2f}")
        
        pito = input("¿Desea ingresar otro producto? (Si/No): ").lower()
        if pito != "si":
            break

    print(f"\nTotal a pagar: ${total:.2f}")

def menu():
    while True:
        print("\nAgenda de Pedidos")
        print("1. Agregar pedido")
        print("2. Eliminar pedido")
        print("3. Mostrar pedidos")
        print("4. Calcular total")
        print("5. Salir")

        opcion = input("Seleccione una opción (1-5): ")

        if opcion == "1":
            agregar_pedido()
        elif opcion == "2":
            eliminar_pedido()
        elif opcion == "3":
            mostrar_pedidos()
        elif opcion == "4":
            calcular_total()
        elif opcion == "5":
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
    print("5. Bondiola x kg $6.200,00")
    print("6. Fideos Tallarines 500g $2.300,00")
    print("7. Copos de maiz azucarados 490g $3.535,00")

if __name__ == "__main__":
    menu()
```

### Explicación de los cambios:
1. **Función `calcular_total`:** He añadido la función que te permite calcular el total basado en los productos seleccionados y la cantidad que el cliente desea. 
   - Se muestra el precio de cada producto y su subtotal.
   - Se acumula el total de los productos seleccionados por el cliente y se imprime al final.
2. **Menú actualizado:** Se ha añadido una nueva opción en el menú llamada **"4. Calcular total"**, que ejecuta la función `calcular_total()`.

Este código ahora te permite agregar pedidos, eliminarlos lógicamente, mostrar los pedidos activos y calcular el total de una compra.
