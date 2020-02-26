#------------------entradas----------------
_cantidadPacientes = 0
_cantidadPacientesUCI = 0

#-----------------mensajes--------------
MENSAJE_BIENVENIDA = "Hola, bienvenido al sistema"
MENSAJE_CANTIDAD_PACIENTES = "Ingrese la cantidad de pacientes registrados \n"
MENSAJE_PACIENTES_UCI = "Ingrese la cantidad de pacientes en UCI \n"
MENSAJE_RIESGO_ALTO = "El riesgo operacional es alto"
MENSAJE_RIESGO_MEDIO = "El riesgo es medio"
MENSAJE_RIESGO_BAJO = "El riesgo es bajo"

#----------------codigo----------------

print(MENSAJE_BIENVENIDA)
_cantidadPacientes = int(input(MENSAJE_CANTIDAD_PACIENTES))
_cantidadPacientesUCI = int(input(MENSAJE_PACIENTES_UCI))
if(0<_cantidadPacientes<=1000):
     print(MENSAJE_RIESGO_BAJO)
elif(_cantidadPacientes<=5000):
    if(_cantidadPacientesUCI>1000):
        print(MENSAJE_RIESGO_ALTO)
    else:
        print(MENSAJE_RIESGO_MEDIO)
else:
    print(MENSAJE_RIESGO_ALTO)
    
    


