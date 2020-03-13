#_cantidadSaltos = int(input("ingrese la cantidad de saltos :"))
#for i in range(4):
#    print(i)
#for i in range(_cantidadSaltos):
#    print("el canguro da susalto" , i+1)

#DIAS = ["lunes", "martes", "miercoles", "jueves", "viernes"]
#for dia in DIAS:
#    print(dia)


NOMBRE = ["octavio", "lucas", "abel", "isabella", "kathe", "maria"]
EDADES = [14,18,22,26,34,38]

print(len(NOMBRE), len(EDADES))
for i in range(len(NOMBRE)):
    if EDADES [i]>=18 :
        print(i,"la persona ", NOMBRE[i], "es mayor")

sumaEdades = 0
for edad in EDADES:
    sumaEdades = sumaEdades + edad
print (sumaEdades)
