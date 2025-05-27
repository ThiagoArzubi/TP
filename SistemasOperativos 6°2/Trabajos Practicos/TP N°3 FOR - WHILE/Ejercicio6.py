import os
os.system ("cls")


#VALOR CONTRASEÑA CON 3 INTENTOS
print("-----------------------------------------------")
print(" EJERCICIO 6: VALOR CONTRASEÑA CON 3 INTENTOS")
print("-----------------------------------------------")
print("")

contraseña = "secreta"
intentos = 3
while intentos > 0:
    clave = input("Ingresá la contraseña: ")
    if clave == contraseña:
        print("Acceso permitido.")
        break
    else:
        print("Contraseña incorrecta.")
    intentos -= 1
if intentos == 0:
    print("Acceso bloqueado.")