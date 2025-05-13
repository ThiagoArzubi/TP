import os
os.system ("cls")


#CALCULAR RADIANES A SEXAGESIMALES Y CENTESIMALES
print("--------------------------------------------------------")
print(" COMPLEMENTO 9: RADIANES A SEXAGESIMALES Y CENTESIMALES")
print("--------------------------------------------------------")
print("")
pi=3.1416
x=float(input("Ingrese angulo en radianes: "))
sex = x*180/pi
cen = x*200/pi
print("En sexagesimales es:",sex)
print("En centesimales es:",cen)