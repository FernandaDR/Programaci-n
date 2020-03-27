def hablar (mensaje):
    print (mensaje)
    return "exitoso"

def validar_clave (CLAVE_REAL, _claveIngresada):
    if(CLAVE_REAL == _claveIngresada):
        print("ingreso exitoso")
        STATE = "clave valida"
    else:
        print("clave incorrecta")
        STATE = "clave invalida"
    return STATE

def mostrar_lista(lista):
    contador = 1
    for elemento in lista:
        print(elemento)
        contador += 1

def mostrar_dos_listas ( lista_1, lista_2):
    if(len(lista_1)==(len(lista_2))):
        print("elemento", "precio")
        for i in range (len(lista_1)):
            print(lista_1[i],lista_2[i])
    else:
        print("no se puede mostrar uno a uno")

def bienvenida(): print ("Bienvenido al codigo")


hablar("hola a todos este es mi mensaje")

print(hablar ("hola"))
if hablar ("hola a todos") ==  "exitoso":
    print ("el mensaje se mostró con exio")

def ingresar ():
    intentos = 0
    estado = validar_clave(1234, int(input("ingrese la clave : ")))
    intentos += 1
    while (estado != "clave valida" and intentos<3):
        estado = validar_clave(1234,int(input("ingrese la clave : ")))
        intentos += 1
    return estado

comidas =["carne", "pollo", "huevo", "queso"]
mostrar_lista(comidas)

bienvenida()

if ( ingresar() == "clave valida"):     
    comidas = ["carne","pollo","huevo","queso"]
    precios = [1234, 5678, 9101, 1213]
    mostrar_lista (comidas)
    mostrar_dos_listas(comidas,precios)
else:
    print("lo sentimos usted no ingresó correctamente, saliendo del programa")


