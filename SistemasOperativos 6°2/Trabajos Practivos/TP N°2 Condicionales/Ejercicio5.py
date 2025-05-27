import os,random,string
os.system ("cls")


#GENERADOR DE CONTRASEÑAS SEGURAS
print("-----------------------------------------------")
print(" EJERCICIO 5: GENERADOR DE CONTRASEÑAS SEGURAS")
print("-----------------------------------------------")
print("")


# Solicitamos al usuario la longitud deseada de la contraseña
longitud = int(input("Ingrese la longitud de la contraseña: "))  # Pide la longitud de la contraseña

# Preguntamos qué tipos de caracteres incluir
usar_letras = input("¿Incluir letras? (s/n): ").lower() == "s"  # Pregunta si incluir letras
usar_numeros = input("¿Incluir números? (s/n): ").lower() == "s"  # Pregunta si incluir números
usar_simbolos = input("¿Incluir símbolos? (s/n): ").lower() == "s"  # Pregunta si incluir símbolos

# Construimos el conjunto de caracteres posibles
caracteres = ""  # Inicializa la cadena de caracteres posibles
if usar_letras:
    caracteres += string.ascii_letters  # Incluye a-z y A-Z si el usuario lo desea
if usar_numeros:
    caracteres += string.digits         # Incluye 0-9 si el usuario lo desea
if usar_simbolos:
    caracteres += string.punctuation    # Incluye símbolos especiales si el usuario lo desea

# Validamos que haya al menos un tipo seleccionado
if caracteres == "":
    print("Debe seleccionar al menos un tipo de carácter.")  # Mensaje si no se seleccionó ningún tipo
else:
    # Generamos la contraseña seleccionando aleatoriamente
    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))  # Genera la contraseña
    print(f"Contraseña generada: {contraseña}")  # Muestra la contraseña generada