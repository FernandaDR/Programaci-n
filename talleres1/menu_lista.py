#----------------Mensajes----------------
MENSAJE_NUMERO = " Ingrese un numero por favor : "
MENSAJE_MENU = """ Menú:
1- Ingresar al sistema
2- Agregar productos a la lista de compra
3- Lista de productos
4- Eliminar producto
5- Salir """
MENSAJE_BIENVENIDA = " Bienveni@ a este programa \n Por favor ingrese al sistema \n "
MENSAJE_EDAD = " Por favor ingrese su edad : "
MENSAJE_INGRESO = " Usted ha ingresado correctamente al sistema, puede continuar con su compra "
MENSAJE_DESC_1 = " Usted ha ingresado correctamente al sistema y tiene 30% de descuento en su compra, puede continuar \n "
MENSAJE_DESC_2 = " Usted ha ingresado correctamente al sistema y tiene 60% de descueno en su compra, puede continuar \n  "
PREGUNTA_PRODUCTOS = " Por favor ingrese el producto que desea llevar : "
PREGUNTA_PRODUCTOS_2 = " ¿Desea llevar algo más? si->s no->n : "
MENSAJE_DENEGADO = " Su ingreso a sido denegado "
MENSAJE_ELIMINAR = " Por favor ingrese la posición del producto que desea eliminar "
MENSAJE_CONFIRMACION_ELIMINAR = """ ¿Está seguro de que desea eliminar un produCto de su lista de compra? 
 si-> s no-> n """
MENSAJE_CONTINUAR = " Si desea puede co \n "
#---------------Entradas----------------
_numeroIngresado = ""
_edadUsuario = ""
#---------------Variables---------------
EDAD_PERMITIDA = 18
RESPUESTA = ""
list_menu =[]
_posicionProducto = 1
#----------------Código-----------------
print (MENSAJE_BIENVENIDA)
while ( _numeroIngresado != 5):
    print ( MENSAJE_MENU)
    _numeroIngresado = int(input(MENSAJE_NUMERO))
    if (_numeroIngresado == 1):
        _edadUsuario = int(input(MENSAJE_EDAD))
        if ( 1 < _edadUsuario< 18 ):
            while (_edadUsuario < 18 ):
                print (MENSAJE_DENEGADO)
                _edadUsuario = int(input(MENSAJE_EDAD))
            print(MENSAJE_INGRESO)
        elif (18 <= _edadUsuario < 30): print (MENSAJE_INGRESO)
        elif (30 <= _edadUsuario < 60): print ( MENSAJE_DESC_1 )
        else: print( MENSAJE_DESC_2)
    elif (_numeroIngresado == 2 ):
        list_menu.append(input(PREGUNTA_PRODUCTOS))
        RESPUESTA = input(PREGUNTA_PRODUCTOS_2)
        while (RESPUESTA == "s"):
            list_menu.append(input(PREGUNTA_PRODUCTOS))
            RESPUESTA = input(PREGUNTA_PRODUCTOS_2)
        print(MENSAJE_CONTINUAR)
    elif (_numeroIngresado == 3):
        for producto in list_menu:
            print(list_menu)
    elif ( _numeroIngresado == 4):
        list_menu.pop (MENSAJE_ELIMINAR,_posicionProducto)
        while (RESPUESTA == "s"):
            RESPUESTA = input(MENSAJE_CONFIRMACION_ELIMINAR)
        print(MENSAJE_CONTINUAR)
print("GRACIAS POR SU COMPRA")