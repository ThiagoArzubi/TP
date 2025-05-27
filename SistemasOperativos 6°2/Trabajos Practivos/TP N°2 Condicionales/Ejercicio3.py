import os
os.system ("cls")


#ORGANIZADOR DE TAREAS
print("--------------------------------------------------")
print(" EJERCICIO 3: ORGANIZADOR DE TAREAS")
print("--------------------------------------------------")
print("")

# Inicializamos una lista vacía para almacenar tareas
tareas = []  # Lista de tareas, cada una es un diccionario con descripción y estado

# Bucle principal para gestionar el menú de opciones
while True:
    print("\nOrganizador de Tareas")  # Muestra el título del programa
    print("1. Agregar tarea")  # Opción para agregar una nueva tarea
    print("2. Ver tareas")  # Opción para ver todas las tareas
    print("3. Cambiar estado de tarea")  # Opción para cambiar el estado de una tarea
    print("4. Eliminar tarea")  # Opción para eliminar una tarea
    print("5. Salir")  # Opción para salir del programa
   
    opcion = input("Seleccione una opción: ")  # Solicita al usuario que elija una opción

    if opcion == "1":
        nombre = input("Ingrese la descripción de la tarea: ")  # Pide la descripción de la tarea
        tareas.append({"descripcion": nombre, "estado": "pendiente"})  # Agrega la tarea como pendiente
        print("Tarea agregada.")  # Confirma que la tarea fue agregada
    elif opcion == "2":
        print("\nListado de tareas:")  # Muestra el listado de tareas
        for i, t in enumerate(tareas):  # Recorre la lista de tareas
            print(f"{i+1}. {t['descripcion']} - Estado: {t['estado']}")  # Muestra cada tarea con su estado
    elif opcion == "3":
        num = int(input("Ingrese el número de la tarea a actualizar: ")) - 1  # Pide el número de tarea a actualizar
        if 0 <= num < len(tareas):  # Verifica que el número sea válido
            nuevo_estado = input("Nuevo estado (pendiente / en progreso / completada): ")  # Pide el nuevo estado
            tareas[num]["estado"] = nuevo_estado  # Actualiza el estado de la tarea
            print("Estado actualizado.")  # Confirma la actualización
        else:
            print("Tarea inválida.")  # Mensaje si el número es incorrecto
    elif opcion == "4":
        num = int(input("Ingrese el número de la tarea a eliminar: ")) - 1  # Pide el número de tarea a eliminar
        if 0 <= num < len(tareas):  # Verifica que el número sea válido
            tareas.pop(num)  # Elimina la tarea de la lista
            print("Tarea eliminada.")  # Confirma la eliminación
        else:
            print("Número inválido.")  # Mensaje si el número es incorrecto
    elif opcion == "5":
        print("Saliendo del organizador de tareas.")  # Mensaje de salida
        break  # Sale del bucle y termina el programa
    else:
        print("Opción inválida.")  # Mensaje si la opción no es válida