def crear_lista (lista):
    print ("Lista nueva :", lista)
    return ("lista creada")

def mostrar_lista (lista):
    i=1
    for nombre in lista:
        print (nombre)
        i+=1
    return

def mostrar_3_listas (lista_1,lista_2,lista_3):
    for i in range(len(lista_1) and len(lista_2) and len(lista_3)):            
        print(lista_1[i],lista_2[i],lista_3[i])
    return


def mostrar_dos_listas ( lista_1, lista_2):
    for i in range (len(lista_1) and len(lista_2)):           
        print(lista_1[i],lista_2[i])


_listaNueva = input("Ingrese por favor el nombre de la lista : ")
crear_lista(_listaNueva)
doctores = ["juan", "pedro", "matha"]
enfereros = ["felipe", "Marco"]
Enfermo =["juanes"]
mostrar_dos_listas(doctores,enfereros)
mostrar_3_listas(doctores, enfereros, Enfermo)