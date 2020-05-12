import matplotlib.pyplot as plt
#___________Gráfico de barras___________
personas = {
    "Nombres" : ["Ándrea","Martín","Jueanita","Mateo","Ester"],
    "Pesos" : [65,84,52,96,60]
}
print(personas["Nombres"])
print(personas["Pesos"])
#__________Vertical____________
plt.bar(personas["Nombres"],personas["Pesos"], color ="g", alpha = 0.5)
plt.title("Pesos de pacientes")
plt.xlabel("Nombres")
plt.ylabel("Pesos(Kg)")
plt.savefig("Pesos_pacientes.png")
plt.close()
# plt.show()
#________Horizontal____________
plt.barh(personas["Nombres"],personas["Pesos"], color ="g", alpha = 0.5)
plt.title("Pesos de pacientes")
plt.xlabel("Nombres")
plt.ylabel("Pesos(Kg)")
figure = plt.gcf()
figure.set_size_inches(9,9)
plt.savefig("Pesos_pacientes_horizontal.png")
plt.close()
# plt.show()