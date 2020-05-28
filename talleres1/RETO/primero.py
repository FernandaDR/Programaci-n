import matplotlib.pyplot as plt
import pandas as p
import sys
def graficarCurvas ():
    def validar():
        nombreArchivo = input("Ingrese el nombre del archivo: ")
        try :
            Archivo = p.read_csv(nombreArchivo,encoding='UTF-8',header=0, delimiter=";").to_dict()
        except FileNotFoundError :
            print("Ingresaste un archivo que no existe") 
            validar()
        return Archivo 
    csv = validar() 
    titulo1 = input("Ingrese el nombre de los datos que irán en el eje X: ")
    titulo2 = input("Ingrese el nombre de los datos que irán en el eje Y: ")
    titulo = input("Ingrese el nombre de la gráfica: ")
    medida1 = input("Ingrese en que unidades están medidos los datos del eje X: ")
    medida2 = input("Ingrese en que unidades están medidos los datos del eje Y: ")
    nombreGuardar = input("Ingrese el nombre con el que desea guardar el nuevo archivo y su formato: ")
    x= list(csv[titulo1].values())
    y = list(csv[titulo2].values())
    plt.title(titulo)
    plt.xlabel(medida1)
    plt.ylabel(medida2)
    plt.plot(x,y)
    plt.savefig(nombreGuardar)
    plt.close()
    return print("Gráfica creada")

graficarCurvas()