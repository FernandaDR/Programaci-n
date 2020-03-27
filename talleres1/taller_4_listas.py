#-----------------MENSAJES---------------
MENSAJE_BIENVENIDA = "Bienvenido a este programa "
MENSAJE_AGREGAR_EDAD = " Por favor ingrese la edad del paciente : "
MENSAJE_ACCION_FINALIZADA = " Acción finalizada "
PREGUNTA_AGREGAR ="**Cuando halla terminado por favor ingrese 0"
MENSAJE_LISTA_HOY = "Lista de edades ingresadas hoy"
MENSAJE_MOSTRAR_LISTA = " Mostrado con éxito"
MENSAJE_SUMA_LISTAS = " Esta es la lista completa de las edades de los pacientes del hospital \n"
MENSAJE_PROMEDIO = "El promedio de edades de esta lista es de"
MENSAJE_EDAD_MAX = "El paciente más adulto tiene una edad(en años) de "
MENSAJE_EDAD_MIN = "El paciente más joven tiene una edad(en años) de "
MENSAJE_LISTA_CRECIENTE = "Lista de edades en orden creciente "
MENSAJE_LISTA_DECRECIENTE = "Lista de edades en orden decreciente "
MENSAJE_MALA_ENTRADA = "Así quedaría la lista después de la entrada errada del auxiliar \n "
MENSAJE_SALIDA_PACIENTE = "La lista de edades después de que el paciente #6 se retirara, queda así \n"
MENSAJE_DESPEDIDA = "Esto fue todo por hoy"
#----------------VARIABLES--------------
NO = "No acabar"
listaEdadesDia = []


#-----------------CODIGO-----------------
def bienvenida(mensaje):
    print(mensaje)
    return
def agregar_edad ():
    print(PREGUNTA_AGREGAR)
    _edadAgregada = int(input(MENSAJE_AGREGAR_EDAD))
    listaEdadesDia.append(_edadAgregada)
    while(_edadAgregada != 0):
        _edadAgregada = int(input(MENSAJE_AGREGAR_EDAD))
        listaEdadesDia.append(_edadAgregada)
        final = NO
    for i in range (len(listaEdadesDia)):
        if (_edadAgregada == listaEdadesDia[i]):
            final = i
    if (final != NO ):
        listaEdadesDia.pop(final)
    return (print(MENSAJE_ACCION_FINALIZADA))

def mostrar_lista (lista, mensaje):
    print(mensaje)
    posicion = 1
    for edad in lista:
        print (edad)
        posicion += 1
    return(print(MENSAJE_MOSTRAR_LISTA))

def sumar_listas (lista_1, lista_2):
    lista_1.extend(lista_2)
    print(MENSAJE_SUMA_LISTAS)
    posicion =1
    for i in range (len(lista_1)):
        print (lista_1[i ])
        posicion +=1
    
def sacar_promedio (lista):
    suma = 0
    for edad in listaEdadesIniciales:
        suma = suma + edad
    promedio = suma/ (len(lista))
    print (MENSAJE_PROMEDIO,promedio)

def orden_creciente (mensaje,lista):
    print(mensaje)
    lista.sort()
    lugar = 1
    for edad in lista:
        print(edad)
        lugar += 1
    return(print("Completo"))

def orden_decreciente (mensaje,lista):
    print(mensaje)
    lista.sort(reverse = True )
    lugar = 1
    for edad in lista:
        print(edad)
        lugar += 1
    return(print("Completo"))

def ingresar_paciente (mensaje,lista,posicion, edad):
    print(mensaje)
    lista.insert(posicion,edad)
    lugar = 1
    for edad in lista:
        print (edad)
        lugar += 1
    return(print("Listo"))

def sacar_paciente (mensaje,lista,posicion):
    print(mensaje)
    lugar = 1
    lista.pop(posicion)
    for edad in lista:
        print (edad)
        lugar += 1
    return(print("Listo"))
    


bienvenida(MENSAJE_BIENVENIDA)
listaEdadesIniciales = [1,2,4,8,16,32,64]
agregar_edad()
mostrar_lista(MENSAJE_LISTA_HOY, listaEdadesDia)
sumar_listas(listaEdadesIniciales,listaEdadesDia)
listaEdadesHospitalCopia = listaEdadesIniciales.copy
sacar_promedio(listaEdadesIniciales)
print (MENSAJE_EDAD_MAX,max(listaEdadesHospitalCopia))
print(MENSAJE_EDAD_MIN,min(listaEdadesHospitalCopia))
orden_creciente(MENSAJE_LISTA_CRECIENTE, listaEdadesHospitalCopia)
orden_decreciente(MENSAJE_LISTA_DECRECIENTE, listaEdadesHospitalCopia)
ingresar_paciente(MENSAJE_MALA_ENTRADA, listaEdadesIniciales,3,87)
sacar_paciente(MENSAJE_SALIDA_PACIENTE, listaEdadesIniciales,5)



