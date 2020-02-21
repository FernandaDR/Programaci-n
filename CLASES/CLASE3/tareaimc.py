#------mensajes---------------------

MENSAJE_BIENVENIDA = "BIENVENIDO"
MENSAJE_DESPEDIDA = "DE NADA, ADIOS"
PREGUNTA_NOMBRE = "Ingresa tu nombre \n "
PREGUNTA_PESO = "Ingresa tu peso \n "
PREGUNA_ESTATURA = "ingresa tu estatura \n "

MENSAJE_OBESO = "estas obeso"
MENSAJE_PESO_IDEAL = "Tu peso es el ideal, felicitaciones"
MENSAJE_SOBRE_PESO = "Estas en sobrepeso"
MENSAJE_BAJO_PESO= "Estas en riego de desnutricion"
MENSAJE_TOCAYO = "somos tocayos"
#------variables--------------------
imc = 0
#------entradas--------------------
_nombreUsuario = ""
_peso = 0.0
_estatura = 0.0

#------codigo----------------------
print(MENSAJE_BIENVENIDA)
_nombreUsuario = input(PREGUNTA_NOMBRE)
_peso = float(input(PREGUNTA_PESO))
_estatura = float(input(PREGUNA_ESTATURA))

imc = (_peso / (_estatura**2))
print("Tu imc es \n", imc)

if(imc >= 19) and (imc <= 24):
    print(MENSAJE_PESO_IDEAL)
elif(imc >= 12) and (imc <19):
    print(MENSAJE_BAJO_PESO),
elif(imc >24) and (imc <=29):
    print(MENSAJE_SOBRE_PESO)
else:
    print(MENSAJE_OBESO)
    print(MENSAJE_TOCAYO)
print(MENSAJE_DESPEDIDA)






