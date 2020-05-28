import matplotlib.pyplot as plt
_kilosArroz = 0.0
_kilosLentejas = 0.0
_kilosFrijoles = 0.0
_kilosPapa = 0.0

_kilosArroz = int(input("Ingrese cuántos kilos de arroz tiene: "))
_kilosLentejas = int(input("Ingrese cuántos kilos de lentejas tiene: "))
_kilosFrijoles = int(input("Ingrese cuántos kilos de frijol tiene: "))
_kilosPapa = int(input("Ingrese cuántos kilos de papa tiene: "))

mercado = {
    "Productos" : ["Arroz","Lentejas", "Frijoles", "Papa"],
    "Cantidad" : [_kilosArroz,_kilosLentejas,_kilosFrijoles,_kilosPapa]
}
plt.bar(mercado["Productos"],mercado["Cantidad"], color ="r", alpha = 0.9)
plt.title("El mercado en cuarentena")
plt.xlabel("Productos")
plt.ylabel("Cantidad(Kg)")
plt.savefig("Mercado.png")
plt.close()
# plt.show()