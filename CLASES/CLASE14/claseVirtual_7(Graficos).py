import matplotlib.pyplot as plt
import pandas as p
#___________Gráfico Curvas_____________
year = [2000,2001,2002,2003,2004,2005,2006]
dolar_pesos_colombianos = [1950,1820,1620,1650,1930,2050,2020]
dolar_soles =[250,820,620,350,430,280,920]
dolar_mexico =[50,25,20,50,30,80,20]

plt.plot(year,dolar_pesos_colombianos)
plt.plot(year,dolar_soles)
plt.plot(year,dolar_mexico)
plt.xlabel("Año")
plt.ylabel("Valor del dolar en pesos colombianos")
plt.title("Evolución del dolar")
plt.legend(["Dolar en pesos colombianos","Dolar en soles"] )
plt.savefig("Gráfico dolar.png")
plt.close()
# plt.show()
Ecg =p.read_csv("Ecg.csv",encoding='UTF-8',header=0, delimiter=";").to_dict()
x= list(Ecg["muestra"].values())
y = list(Ecg["valor"].values())
plt.title("ECG-uV")
plt.xlabel("Tiempo(ms)")
plt.ylabel("Volataje(uV)")
plt.plot(x,y)
plt.savefig("mi_ecg.png")
plt.close()
#__________Gráfico de torta_______________
labels = 'Java', 'python', 'C#', 'JavaScript'
sizes = [15, 45, 30, 10]
explode = (0.1, 0, 0, 0) 
plt.pie(sizes, explode=explode, labels=labels, shadow=False, startangle=0)
plt.title("Lenguajes más usados")
plt.savefig("Grafico_torta.png")
plt.show()