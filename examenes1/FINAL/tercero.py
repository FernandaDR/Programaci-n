import matplotlib.pyplot as plt
import pandas as p
import sys

ecg = p.read_csv("ecg.csv" , encoding='UTF-8',header=0, delimiter=";").to_dict()
eeg = p.read_csv("eeg.csv" , encoding='UTF-8',header=0, delimiter=";").to_dict()
ppg = p.read_csv("ppg.csv" , encoding='UTF-8',header=0, delimiter=";").to_dict()
x = list((ecg["muestra"].values()),((eeg["muestra"].values())),((ppg["muestra"].values())))
y = list((ecg["valor"].values()),((eeg["valor"].values())),((ppg["valor"].values())))
plt.title("ECG , EEG , PPG -uV")
plt.xlabel("Tiempo(ms)")
plt.ylabel("Volataje(uV)")
plt.plot(x,y)
plt.savefig("grafico_ecg_eeg_ppg.png")
plt.close()

picos = {
    "Numero de Picos" : [9,10,9],
    "Estudio" : ["ECG","EEG","PPG"] 
}

plt.bar(picos["Numero de Picos"],picos["Estudio"], color ="r", alpha=0.5)
plt.title("Picos Estudios")
plt.xlabel("Nuemro de Picos") 
plt.ylabel("Estudio")
plt.savefig("Picos.png") 
plt.close() 
# plt.show()