#1) realizar la carga del nombre de una persona y luego mostrar el primer caracter del nombre y la cantidad que letras que lo componen
#2) solicitar la carga del nombre de una persona en minusculas. Mostrar un mensaje si comienza con vocal dicho nombre
import os
os.system("cls")

nombre=input("ingrese su nombre: ")
print("El primer caracter de tu nombre es:",nombre[0],", y tiene un total de",len(nombre),"Letras")
