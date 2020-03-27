#----------------Mensajes----------------
MENSAJE_NUMERO = " Ingrese un numero por favor : "
MENSAJE_MENU = """ Menú:
1- Ver peso y presión de los pacientes
2- Añadir peso a la lista
3- Ver registro
4- Salir
"""
MENSAJE_BIENVENIDA = " Bienveni@ a este programa "
PREGUNTA_PESO = " Por favor ingrese el peso del paciente nuevo : "
PREGUNTA_AGREGAR ="**Cuando halla terminado por favor ingrese 0.0"
MENSAJE_ACCION_FINALIZADA = " Acción finalizada "
MENSAJE_OPCION_UNO = "Estos son los pesos de los pacientes con su respectiva presión "
MENSAJE_LISTA_DECRECIENTE = "Lista de presiones en orden decreciente "
MENSAJE_PRESION_MAX = "La presión más alta registrada en mm/hg es de  "
MENSAJE_PRESION_MIN = " La presión más baja registrada en mm/hg es de "
MENSAJE_DENEGADO = " Su ingreso ha sido denegado "
MENSAJE_ERROR = " Su acción ha sido errada "
MENSAJE_CONTINUAR = " Si desea puede continuar \n "
SALIR = "Usted ha salido del programa"

#---------------Entradas----------------
_pesoNuevo = ""
_numeroIngresado = ""
#---------------Variables---------------
respuesta = ""
list_menu =[]
posicionProducto = 1
NE = "No existe"
NO = "No agragar mas"
#----------------Código-----------------
print (MENSAJE_BIENVENIDA)
pesosPacientesIniciales = [32,64,74,85,98,115,122,127,137,148]
presionPaciente = []

for _numeroIngresado in range (1,4):
    while ( _numeroIngresado != 4):
        print (MENSAJE_MENU)
        _numeroIngresado = int(input(MENSAJE_NUMERO))
        if (_numeroIngresado == 1):
            def mostrar_dos_listas (lista_1,lista_2, mensaje):
                print(mensaje)
                posicion = 1
                for peso in range(len(lista_1)):
                    presion = peso*6
                    lista_2.append(presion)
                    print (lista_1,lista_2)
                    posicion += 1
                return()
            mostrar_dos_listas(pesosPacientesIniciales,presionPaciente, MENSAJE_OPCION_UNO)

        elif (_numeroIngresado == 2 ):
            def agregarPeso ():
                print(PREGUNTA_AGREGAR)
                _pesoAgregado = float(input(PREGUNTA_PESO))
                pesosPacientesIniciales.append(_pesoAgregado)
                while(_pesoAgregado != 0.0):
                    _pesoAgregado = float(input(PREGUNTA_PESO))
                    pesosPacientesIniciales.append(_pesoAgregado)
                    final = NO
                for i in range (len(pesosPacientesIniciales)):
                    if (_pesoAgregado == pesosPacientesIniciales[i]):
                        final = i
                if (final != NO ):
                    pesosPacientesIniciales.pop(final)
                print (pesosPacientesIniciales)
                return (print(MENSAJE_ACCION_FINALIZADA))
            agregarPeso()

        elif (_numeroIngresado == 3):
            print (MENSAJE_PRESION_MAX,max(presionPaciente))
            print(MENSAJE_PRESION_MIN,min(presionPaciente))
            def orden_decreciente (mensaje,lista):
                print(mensaje)
                lista.sort(reverse = True )
                lugar = 1
                for peso in lista:
                    print(peso)
                    lugar += 1
                return(print("Completo"))
            orden_decreciente(MENSAJE_LISTA_DECRECIENTE,presionPaciente)
            print("Pacientes: ",len(presionPaciente))
            print(list_menu)                  
            print(MENSAJE_CONTINUAR)
        else: 
            print(SALIR)
    print(SALIR)
    




