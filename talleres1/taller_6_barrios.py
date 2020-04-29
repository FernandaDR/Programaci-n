import pandas as p 
diccionario =p.read_csv("barrios.csv",encoding='UTF-8', header = 0,delimiter=';').to_dict()
nombre_mas_largo = max (diccionario["Barrio"].values(), key=len)
nombre_mas_corto = min (diccionario["Barrio"].values(), key=len)
consumo_agua_max = max(diccionario["Agua"].values())
consumo_agua_min = min(diccionario["Agua"].values())
consumo_energia_max = max(diccionario["Energía"].values())
consumo_energia_min = min(diccionario["Energía"].values())
consumo_gas_max = max(diccionario["Gas"].values())
consumo_gas_min = min(diccionario["Gas"].values())
consumo_internet_max = max(diccionario["Internet"].values())
consumo_internet_min = min(diccionario["Internet"].values())
cantidad_habitantes_max = max (diccionario["Habitantes"].values())
cantidad_habitantes_min = min (diccionario["Habitantes"].values())
print("Bienvenidos al sistema de barrios de Medellín","\nEl barrio con el nombre más largo es",nombre_mas_largo, "y el que presenta el nombre mas corto es",nombre_mas_corto,
"\nEl consumo mínimo de agua es de",consumo_agua_min,"y el máximo es de",consumo_agua_max,"\nEl consumo mínimo de energía es de",
consumo_energia_min,"y el consumo máximo es de",consumo_energia_max,"\nEl consumo mínimo de gas es de",consumo_gas_min,
"y el consumo máximo es de",consumo_gas_max,"\nEl consumo mínimo de internet es de",consumo_internet_min,"y el máximo es de",
consumo_internet_max,"\nLa cantidad mínima de haitantes es de", cantidad_habitantes_min,"y la máxima es de",cantidad_habitantes_max)