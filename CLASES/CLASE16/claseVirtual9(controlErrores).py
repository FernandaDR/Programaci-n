import sys
edad = "No ingresaste edad"
try:
    edad = int (input('Ingrese su edad :'))
except ValueError:
    print ("ingresaste mal la edad")
try :
    archivo = open ("Soy_un_archivo_que_no_existe.txt")
except FileNotFoundError :
    print("Ingresaste un archivo que no existe")

def os_validate(so):
    assert(so in sys.platform)
    print ("Estas en el sistema operativo", so)

try :
    os_validate('linux')
except AssertionError:
    print("Hola no eres linux")

try:
    os_validate('darwin')
except AssertionError:
    print("no eres mac")

def validador_parrafo(parrafo):
    assert(parrafo.endswith("."))
    return False
validador = True

while (validador):
    parrafo =  input('ingrese un parrafo debe finalizar con .')
    try:
        validador = validador_parrafo(parrafo)
    except AssertionError:
        print("Entrada no válida")
