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
MENSAJE_DENEGADO = " Su ingreso ha sido denegado "
MENSAJE_ELIMINAR = " Por favor ingrese el producto que desea eliminar "
MENSAJE_CONFIRMACION_ELIMINAR = """ ¿Está seguro de que desea eliminar un produCto de su lista de compra? 
 si-> s no-> n """
MENSAJE_ERROR = " Su acción ha sido errada "
MENSAJE_CONTINUAR = " Si desea puede continuar \n "
MENSAJE_PRODUCTO_ELIMINADO = " Se ha eliminado el producto"
MENSAJE_ELIMINADO_ERROR = " El producto a eliminar no fue encontrado"
SALIR = "Usted ha salido de la compra"
GRACIAS = "GRACIAS POR SU COMPRA"

#---------------Entradas----------------
_numeroIngresado = ""
_edadUsuario = ""
#---------------Variables---------------
respuesta = ""
list_menu =[]
posicionProducto = 1
NE = "No existe"
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
        respuesta = input(PREGUNTA_PRODUCTOS_2)
        while (respuesta == "s"):
            list_menu.append(input(PREGUNTA_PRODUCTOS))
            respuesta = input(PREGUNTA_PRODUCTOS_2)
        if (respuesta =="n"): print(MENSAJE_CONTINUAR)
        else: print(MENSAJE_ERROR)
    elif (_numeroIngresado == 3):
        def mostrar_lista(Lista):
            posicionProducto = 1
            print ("Su lista de productos \n")
            for producto in Lista:
                print(posicionProducto,producto)
                posicionProducto +=1
        mostrar_lista (list_menu)
    elif (_numeroIngresado == 4):
        _producto = input(MENSAJE_ELIMINAR)
        posicionProductoEliminar = NE
        for i in range(len(list_menu)):
            if(_producto == list_menu[i]):
                input(MENSAJE_CONFIRMACION_ELIMINAR)
                posicionProductoEliminar = i       
        if (posicionProductoEliminar != NE) :
            eliminado = list_menu.pop(posicionProductoEliminar)
            print(MENSAJE_PRODUCTO_ELIMINADO, eliminado)
        else:
            print(MENSAJE_ELIMINADO_ERROR)
        print(list_menu)                  
        print(MENSAJE_CONTINUAR)
    else: print(SALIR)
print(GRACIAS)