#UNA CADENA DE CARACTERES ES UN VECTOR
#al realizar el codigo variable[], dentro de corchetes estara el indice de de la variable
#len() te indica la cantidad de caracteres de la variable
#1. Realizar la carga del nombre de una persona
#luego mostrar el primer caracter del nombre, y la cantidad de letras que lo componen
import os
os.system ("cls")
nombre = str(input("Ingrese su nombre: "))

print("El primer caracter de su nombre es: ", nombre[0])

print("La cantidad de letras que lo conforman son: ", len(nombre))