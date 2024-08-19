import os
os.system("cls")
nombres=["Hoffer","Ciro","Koziel","Javier","Thiago"]
contador=0
for i in nombres:
    if len(i) >=5:
        contador+=1
print(contador)