#----------------Mensajes---------------------
PREGUNTA_NOMBRE ="ingrese su nombre \n"
MENSAJE_BIENVENIDA ="Bienvenido al programa"
MENSAJE_DESPEDIDA ="CHAO"
MENSAJE_TOCAYO ="hola hermano somos tocayos"

MENSAJE_JOVEN ="eres joven"
MENSAJE_ADULTO ="eres adulto"
MENSAJE_VIEJO ="estas viejo"

PREGUNTA_EDAD = "Ingrese su edad \n"

#----------------Variables-------------------
NOMBRE_PERSONAL = "Mafe"
#----------------Entradas--------------------
_nombreUsuario = " "
_edadUsuario = 0
#----------------Codigo--------------------
print(MENSAJE_BIENVENIDA)
_nombreUsuario = input(PREGUNTA_NOMBRE)
if(NOMBRE_PERSONAL == _nombreUsuario):
    print(MENSAJE_TOCAYO)

_edadUsuario =int(input(PREGUNTA_EDAD))
if(_edadUsuario >= 0) and (_edadUsuario <=25):
    print(MENSAJE_JOVEN)
elif(_edadUsuario >25) and (_edadUsuario <=65):
    print(MENSAJE_ADULTO)
else:
    print(MENSAJE_VIEJO)

print(MENSAJE_DESPEDIDA)





