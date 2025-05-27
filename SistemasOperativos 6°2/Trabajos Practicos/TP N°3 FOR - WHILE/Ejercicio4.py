import os,random
os.system ("cls")


#ADIVINAR UN NUMERO SECRETO
print("--------------------------------------------------")
print(" EJERCICIO 4: ADIVINAR UN NUMERO SECRETO")
print("--------------------------------------------------")
print("")

secreto = random.randint(1, 10)
intentos = 3
while intentos > 0:
    intento = int(input("Adiviná el número (1-10): "))
    if intento == secreto:
        print("¡Correcto!")
        break
    else:
        print("Incorrecto.")
    intentos -= 1
if intentos == 0:
    print(f"Perdiste. El número era {secreto}.")