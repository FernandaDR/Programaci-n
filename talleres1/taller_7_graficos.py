import matplotlib.pyplot as plt
import pandas as p
#___________Gráfico de barras_________________
barrios =p.read_csv("barrios.csv",encoding='UTF-8',header=0, delimiter=";")

plt.bar(barrios["Barrio"],barrios["Agua"], color ="r", alpha=0.5)
plt.title("Consumo de agua en Medellín")
plt.xlabel("Barrios")
plt.ylabel("Consumo de agua")
plt.xticks(rotation=90)
figure = plt.gcf()
figure.set_size_inches(12,23)
plt.savefig("consumo_agua.png")
plt.close()
plt.bar(barrios["Barrio"],barrios["Gas"], color ="g", alpha=0.5)
plt.title("Consumo de gas en Medellín")
plt.xlabel("Barrios")
plt.ylabel("Consumo de gas")
plt.xticks(rotation=90)
figure = plt.gcf()
figure.set_size_inches(12,23)
plt.savefig("consumo_gas.png")
plt.close()



#___________Gráfico de ECG_________________
ecg =p.read_csv("ecg_taller.csv",encoding='UTF-8',header=0, delimiter=";").to_dict()
x= list(ecg["muestra"].values())
y = list(ecg["valor"].values())
plt.title("ECG-uV")
plt.xlabel("Tiempo(ms)")
plt.ylabel("Volataje(uV)")
plt.plot(x,y)
plt.savefig("ecg_paciente.png")
plt.close()
# Veo 6 picos 
#_______________Gráfico de torta_______________
labels = 'Bogotá', 'Medellín', 'Leticia', 'Villavicencio'
sizes = [80, 7, 5, 8]
explode = (0, 0, 0.1, 0) 
plt.pie(sizes, explode=explode, labels=labels, shadow=True, startangle=0)
plt.title("Estudio de la población")
plt.savefig("Grafico_torta_taller.png")
plt.close()
#plt.show()

