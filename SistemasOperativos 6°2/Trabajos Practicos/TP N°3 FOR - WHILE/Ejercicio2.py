import os
os.system ("cls")


#CLASIFICAR EDADES INGRESADAS
print("-------------------------------------------")
print(" EJERCICIO 2: CLASIFICAR EDADES INGRESADAS")
print("-------------------------------------------")
print("")

niño = 0
ad = 0
adult = 0

while True:
  edad = int(input("ingresa una edad (0 para terminar): "))
              
  if edad == 0:
      break
  elif edad <13:
      niño += 1
  elif 13 <= edad <= 17:
      ad <= 1
  else:
      adult += 1
print("Cantidad de niños", niño )
print("Cantidad de adolecentes", ad)
print("Cantidad de adultos", adult)