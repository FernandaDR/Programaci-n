

listaNombres = ["David", 
                "Susana", 
                "Mafe", 
                "SantiagoH", 
                "Ysabella", 
                "Leslly", 
                "CamilaM", 
                "CamilaB", 
                "Marco", 
                "Juanes", 
                "SantiagoB", 
                "Elena", 
                "Daniel", 
                "DanielP"]

listaEdades = [18,25,17,20,20,21,18,22,24,19,19,21,18,21]
listaNotas = [2.5,3.6,4.2,4.4,5.0,3.9,2.1,4.3,3.5,2.8,3.7,3.4,3.9,4.4]


MENU ="""Presione 1 para - Mostrar nombres 
Presione 2 para - Mostrar edades 
Presione 3 para - Mostrar notas 
Presione 4 para - salir \n"""

_numeroIngresado = int(input(MENU))
while(_numeroIngresado != 4 ):
    if(_numeroIngresado == 1):
        print(listaNombres)
    elif(_numeroIngresado == 2):
        print(listaEdades)
    elif(_numeroIngresado == 3):
        print(listaNotas)
    else:
        print (MENU)
    _numeroIngresado = int(input(MENU))  
    
print("adios")


        

