import matplotlib.pyplot as plt
import pandas as p
labels = "pieza" , "cocina" , "porche" , "Sala" , "piso"
sizes = [70 , 5 , 10 , 5 , 10]
explode = (0.1 , 0 , 0 , 0  , 0) 
plt.pie(sizes, explode=explode, labels=labels, shadow=False, startangle=0)
plt.title("Lugares visitados en cuarentena")
plt.savefig("Curentena.png")
plt.close()
# plt.show()