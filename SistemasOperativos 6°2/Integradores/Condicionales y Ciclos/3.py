import os
os.system ("cls")


#SEGUIMIENTO DE HABITOS SALUDABLE
print("------------------------------------------------")
print(" INTEGRADOR 3: SEGUIMIENTO DE HABITOS SALUDABLE")
print("------------------------------------------------")
print("")

agua = []
print("Ingrese vasos de agua tomados cada día (7 días):")
for i in range(7):
    vasos = int(input(f"Día {i+1}: "))
    agua.append(vasos)

prom = sum(agua)/7
print("Promedio diario:", prom)
if prom < 8:
    print("Recomendación: aumentar el consumo de agua.")