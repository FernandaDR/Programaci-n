#_numeroA = 0
#_numeroB = 0
MENSAJE_ENRADA = " Por favor ingrese un digito "
MENSAJE_DIVISION = "Operacion no valida"

#_numeroA = int( input(MENSAJE_ENRADA))
#_numeroB = int(input(MENSAJE_ENRADA))


def sumar(a,b):
    suma = a+b
    return suma

def restar(a,b):
    resta = a-b
    return resta

def multiplicar( a,b):
    multiplicacion = a*b
    return multiplicacion 

def dividir(a,b):
    division = 0
    if(b==0):
        division = MENSAJE_DIVISION

    else:
        division = a/b    
    return division 

#resultado1 = sumar(_numeroA, _numeroB)
#print(resultado1)

#resultado2 = restar(_numeroA, _numeroB)
#print (resultado2)

#resultado3 = multiplicar(_numeroA, _numeroB)
#print (resultado3)

#resultado4 = dividir(_numeroA, _numeroB)
#print(resultado4)



