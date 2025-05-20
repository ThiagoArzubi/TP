import os
os.system ("cls")


#CALCULAR REGISTRO DE TEMPERATURAS SEMANALES
print("-----------------------------------------------------------")
print(" INTEGRADOR 7: CALCULAR REGISTRO DE TEMPERATURAS SEMANALES")
print("-----------------------------------------------------------")
print("")

temp = []
print("Ingrese las temperaturas máximas de la semana:")
for i in range(7):
    t = float(input(f"Día {i+1}: "))
    temp.append(t)

media = sum(temp) / 7
superiores = sum(1 for x in temp if x > 30)

print("Media semanal:", media)
print("Días con más de 30°C:", superiores)