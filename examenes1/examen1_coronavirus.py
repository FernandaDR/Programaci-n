#----------------mensajes-------------

MENSAJE_BIENVENIDA = "Bienvenido,"
MENSAJE_BIENVENIDO_II = " a continuación será evaluado para determinar su estado de salud."
MENSAJE_NOMBRE = "Por favor introduzc su nombre \n "
MENSAJE_TEMP = "Por favor intraduzca la temperatura actual de su cuerpo \n"
MENSAJE_LUGAR = "Por favor ingrese su lugar de procedencia \n"
MENSAJE_OBSERVACION = "Usted se encuentra en estado de observacion"
MENSAJE_SALUDABLE = "Usted se encuentra en estado saludable"
MENSAJE_HIPOTERMIA = "Usted se encuentra en estado de hipotermia"
MENSAJE_ALERTA = "Usted se encuentra en estado de alerta"
MENSAJE_PELIGRO = "Usted se encuentra en estado de peligro"

#--------------entradas-------------
_nombrePersona = ""
T = 0.0
_lugar_procedencia = ""

#--------------variables-----------
T = 0.0
A = "China"
B = "Iran" 
C = "Italia"

#-------------codigo---------------
_nombrePersona = input(MENSAJE_NOMBRE)
T = float(input(MENSAJE_TEMP))
_lugar_procedencia = input(MENSAJE_LUGAR)
print(MENSAJE_BIENVENIDA, _nombrePersona, MENSAJE_BIENVENIDO_II)

if(_lugar_procedencia == A) or (_lugar_procedencia == B) or (_lugar_procedencia == C):
    print(MENSAJE_OBSERVACION)
else:
    if(T>=36) and (T<=38.4):
        print(MENSAJE_SALUDABLE)
    elif(T<36):
        
        print(MENSAJE_HIPOTERMIA)
    elif(T>=38.5) and (T<=40):
        print(MENSAJE_ALERTA)
    else:
        print(MENSAJE_PELIGRO)






