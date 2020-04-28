def leer_archivo (nombre_archivo):
    archivo_en_memoria = open(nombre_archivo,'r', encoding= "UFT-8")
    lineas_archivo = archivo_en_memoria.read().splitlines()
    archivo_en_memoria.close()
    return lineas_archivo

def escritura_archivo (nombre_archivo, lista_a_escribir):
    archivo_nuevo =  open (nombre_archivo,'w')
    archivo_nuevo.writelines(lista_a_escribir)
    archivo_nuevo.close()

def mostrar_lineas (lista_lineas):
    for linea in lista_lineas:
        print(linea)

def agregar_lineas_archivo(nombre_archivo, linea):
    archivo = open(nombre_archivo,'a')
    archivo.write(linea)
    archivo.close()