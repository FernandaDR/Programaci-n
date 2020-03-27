#-----------------MENSAJES---------------
MENSAJE_AGREGAR_EDAD = " Por favor ingrese la edad del paciente : "
MENSAJE_ACCION_FINALIZADA = " Acción finalizada "
PREGUNTA_AGREGAR ="**Cuando halla terminado por favor ingrese fin"

#----------------VARIABLES--------------
NO = "No acabar"


#-----------------CODIGO-----------------
def agregar_edad ():
    listaEdadesDia = []
    _edadAgregada = input(MENSAJE_AGREGAR_EDAD)
    listaEdadesDia.append(_edadAgregada)
    print(PREGUNTA_AGREGAR)
    while(_edadAgregada != "fin"):
        _edadAgregada = input(MENSAJE_AGREGAR_EDAD)
        listaEdadesDia.append(_edadAgregada)
        final = NO
    for i in range (len(listaEdadesDia)):
        if (_edadAgregada == listaEdadesDia[i]):
            final = i
    if (final != NO ):
        listaEdadesDia.pop(final)
    return (print(MENSAJE_ACCION_FINALIZADA))

def mostrar_lista (lista):
    posicion = 1
    for edad in lista:
        print (edad)
        posicion += 1


    



listaEdadesIniciales = [1,2,4,8,16,32,64]
agregar_edad()
mostrar_lista( "")

