#solicitar la carga del nombre de una persona en minusculas. Mostrar un mensaje si comienza con vocal dicho nombre
import os
os.system("cls")
nombre=input("Ingrese su nombre: ").lower()
if nombre[0] == "a" or nombre[0] == "e" or nombre[0] == "i" or nombre[0] == "o" or nombre[0] == "u":
    print("¡Su nombre es:",nombre,"y empieza por una vocal!")
else: print("Su nombre no empieza por una vocal :(")