#-----------------MENSAJE--------------
MENSAJE_BIENVENIDO = "Bienvenido"
PREGUNTA_NUMERO = """
       ingrese un numero 
       entero
       entre 1-5 
       : """
PREGUNTA_EDAD = "ingrese su edad : "
MENSAJE_EDAD = " usted puede ingresar "
MENSAJE_MAYOR_30 = "tiene un descuento del 30%"
MENSAJE_MAYOR_60 = "tiene un descuento igual a su edad "
MENSAJE_MENORES_EDAD = "no tiene derecho a entrar "
MENSAJE_DESPEDIDA = "salida,muchas gracias por usar el programa"
MENSAJE_ERROR = "entrada no valida, solo admitimos 1,2,3,4,5 "

#--------------ENTTRADA----------------
_numeroIngresado = 0 
_edadPersona = 0
_listaProductos = []
#---------------CODIGO-------------------
print (MENSAJE_BIENVENIDO)
_numeroIngresado = int (input (PREGUNTA_NUMERO))
_edadPersona  = int (input (PREGUNTA_EDAD))
while (_numeroIngresado == 1) :
    if ((_edadPersona > 0) and (_edadPersona <= 17)) : 
        print(MENSAJE_MENORES_EDAD)
    elif ((_edadPersona >=18) and (_edadPersona <=29)) :
        print(MENSAJE_EDAD)
    elif ((_edadPersona >=30) and (_edadPersona <=59)) :
        print(MENSAJE_MAYOR_30)
    else: 
        print(MENSAJE_MAYOR_60)   
    _numeroIngresado = int (input (PREGUNTA_NUMERO))

while(_numeroIngresado ==2)  :
    _listaProductos.append(input("ingrese los producto que quiere comprar : "))
    respuesta = input ("Desea ingresar mas productos? s -> si  n->no : ")
    while (respuesta =="s") :
        _listaProductos.append(input("ingrese los producto que quiere comprar : "))
        respuesta = input ("Desea ingresar mas productos? s -> si  n->no : ") 
    print (_listaProductos)
    _numeroIngresado = int (input (PREGUNTA_NUMERO))

while(_numeroIngresado ==3) :
    print (_listaProductos)
    _numeroIngresado = int (input (PREGUNTA_NUMERO))

while(_numeroIngresado ==4) :
    _productoParaEliminar= input("ingrese el producto que ya no quiere llevar : ")
    eliminar ="no exite"
    for i in range(len(_listaProductos)):
        if( _productoParaEliminar == _listaProductos[i]):
            eliminar = i       
    if (eliminar != "no existe"):
        eliminado = _listaProductos.pop(eliminar)
        print("El producto que fue eliminado es", eliminado)
        respuesta = input("si desea eliminar otro articulo ingrese si :")
        while(respuesta == "si"):
            eliminado = _listaProductos.pop(eliminar)
            print("El producto que fue eliminado es", eliminado)
            respuesta = input("si desea eliminar otro articulo ingrese si :")             
    _numeroIngresado = int (input (PREGUNTA_NUMERO))


while(_numeroIngresado ==5) :
    print (MENSAJE_DESPEDIDA)
    _numeroIngresado = int (input (PREGUNTA_NUMERO))

while (_numeroIngresado !=5) :
    print(MENSAJE_ERROR)
    _numeroIngresado = int (input (PREGUNTA_NUMERO))
