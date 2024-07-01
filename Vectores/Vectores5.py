import os
os.system("cls")
frase=input("Ingrese una frase: ").lower()
vocal=input("Ingrese una vocal: ").lower()
print(frase.replace(vocal,vocal.upper()))
