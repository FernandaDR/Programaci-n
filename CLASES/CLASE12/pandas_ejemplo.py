
import pandas as p 
diccionario =p.read_csv("balance.csv",encoding='UTF-8', header = 0,delimiter=';').to_dict()
print(diccionario)
print(diccionario.keys())
print(diccionario["Ciudad"])


nombre_mas_largo = max (diccionario["Ciudad"].values(), key=len)
nombre_mas_corto = min (diccionario["Ciudad"].values(), key=len)
print("\n\nla Ciudad con el nombre mas largo es",nombre_mas_largo, "y la que presenta el nombre mas corto es", nombre_mas_corto)

ganancia_mayor = max(diccionario["Ganancias"].values())
perdida_mayor= max(diccionario["Perdidas"].values())

print("\n\nla mayor ganancia fue",ganancia_mayor)
print("\n\nla mayor perdida fue",perdida_mayor)
