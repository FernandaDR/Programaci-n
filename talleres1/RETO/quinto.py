import matplotlib.pyplot as plt
import pandas as p
labels = "Leche", "Huevos", "Vino", "Arroz","Queso", "Salchicha"
sizes = [12, 8, 4, 26, 30, 20]
explode = (0, 0,0,0, 0.1, 0) 
plt.pie(sizes, explode=explode, labels=labels, shadow=False, startangle=0)
plt.title("Mercado")
plt.savefig("Mercado_torta.png")
plt.close()