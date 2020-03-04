
#numero = 0
#NUMERO_DESEADO = 12
#while(numero < NUMERO_DESEADO):
#    numero = numero +1
#    print(numero)
#print(numero)
import random
PREGUNTA_NUMERO = """
    Ingrese un numero 
    entero 
    entre 1-10 
    : """
MENSAJE_FALLO = " Fallaste, vuelve a intentarlo "
MENSAJE_ACIERTO = " Es correcto, ese es mi numero favorito "
NUMERO_FAVORITO = random.randint(1,10)
MENSAJE_MAYOR = "Casi, tu numero es mayor"
MENSAJE_MENOR = "Casi, tu numero es menor"
_numeroIngresado = int(input(PREGUNTA_NUMERO))
while(_numeroIngresado != NUMERO_FAVORITO):
    print(MENSAJE_FALLO)
    if( _numeroIngresado > NUMERO_FAVORITO ): print(MENSAJE_MAYOR)
    else: print(MENSAJE_MENOR)
    _numeroIngresado = int(input(PREGUNTA_NUMERO))
print(MENSAJE_ACIERTO)


