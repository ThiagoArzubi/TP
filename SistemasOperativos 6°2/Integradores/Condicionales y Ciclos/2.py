import os
os.system ("cls")


#CONTROL DE CARGA DE COMBUSTIBLE
print("-----------------------------------------------")
print(" INTEGRADOR 2: CONTROL DE CARGA DE COMBUSTIBLE")
print("-----------------------------------------------")
print("")

cargas = []
print("Ingrese cargas de combustible en litros (0 para terminar):")
while True:
    carga = float(input("Carga: "))
    if carga == 0:
        break
    cargas.append(carga)
    if carga < 5:
        print("Alerta: carga sospechosamente baja.")

if cargas:
    print("Total cargado:", sum(cargas))
    print("Promedio por carga:", sum(cargas)/len(cargas))
else:
    print("No se ingresaron cargas.")