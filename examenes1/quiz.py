import matplotlib.pyplot as plt
import pandas as p
#___________Gráfico de barras_________________
elementos =p.read_csv("inventario.csv",encoding='UTF-8',header=0, delimiter=";")
plt.bar(elementos["Elemento"],elementos["Unidades"], color ="y", alpha=0.5)
plt.title("Inventario del hospital")
plt.xlabel("Elemento")
plt.ylabel("Unidades")
plt.xticks(rotation=90)
figure = plt.gcf()
figure.set_size_inches(9,13)
plt.savefig("elemento_unidades.png")
plt.close()
plt.bar(elementos["Elemento"],elementos["Viejos"], color ="g", alpha=1.0)
plt.title("Inventario del hospital")
plt.xlabel("Elemento")
plt.ylabel("Elementos viejos")
plt.xticks(rotation=90)
figure = plt.gcf()
figure.set_size_inches(9,13)
plt.savefig("elemento_Viejo.png")
plt.close()
plt.bar(elementos["Elemento"],elementos["Nuevos"], color ="b", alpha=1.0)
plt.title("Inventario del hospital")
plt.xlabel("Elemento")
plt.ylabel("Elementos nuevos")
plt.xticks(rotation=90)
figure = plt.gcf()
figure.set_size_inches(9,13)
plt.savefig("elemento_Nuevo.png")
plt.close()
#__________Gráfico ppg__________
ppg =p.read_csv("ppg.csv",encoding='UTF-8',header=0, delimiter=";").to_dict()
x= list(ppg["muestra"].values())
y = list(ppg["valor"].values())
plt.title("PPG-uV")
plt.xlabel("Tiempo(ms)")
plt.ylabel("Volataje(uV)")
plt.plot(x,y)
plt.savefig("ppg_paciente.png")
plt.close()
print("Veo 9 picos en la Fotopletismografía del paciente")
#__________Gráfico Torta______________
labels = 'En casa', 'Hopilatizados', 'UCI'
sizes = [85, 10, 5]
explode = (0, 0, 0.1) 
plt.pie(sizes, explode=explode, labels=labels, shadow=True, startangle=0)
plt.title("Casos diagnosticados de COVID-19")
plt.savefig("Grafico_casosCovid-19.png")
plt.close()