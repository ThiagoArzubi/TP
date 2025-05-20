import os
os.system ("cls")


#CALCULAR REGISTRO DE NOTAS Y DETECCION DE DESAPROBADOS
print("----------------------------------------------------------------------")
print(" INTEGRADOR 4: CALCULAR REGISTRO DE NOTAS Y DETECCION DE DESAPROBADOS")
print("----------------------------------------------------------------------")
print("")

aprobados = 0
print("Ingrese las notas de 10 alumnos:")
for i in range(10):
    nota = float(input(f"Nota {i+1}: "))
    if nota >= 7:
        aprobados += 1

print("Aprobados:", aprobados)
print("Desaprobados:", 10 - aprobados)