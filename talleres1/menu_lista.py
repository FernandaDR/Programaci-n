#----------------Mensajes----------------
MENSAJE_BIENVENIDA = " Bienveni@ a este programa "
MENSAJE_EDAD = " Por favor ingrese su edad : "
MENSAJE_DESC_1 = " Usted tiene 30% de descuento en su compra "
MENSAJE_DESC_2 = " Usted tiene 60% de descueno en su compra "
PREGUNTA_PRODUCTOS = " Por favor ingrese el producto que desea llevar : "
PREGUNTA_PRODUCTOS_2 = "¿Desea llevar algo más? si->s no->n : "
#---------------Entradas----------------
_edadUsuario = ""
_productosQuiere =""

#---------------Variables---------------
EDAD_PERMITIDA = 18
RESPUESTA = ""
#----------------Código-----------------
print (MENSAJE_BIENVENIDA)
_edadUsuario = int(input(MENSAJE_EDAD))
RESPUESTA = input(PREGUNTA_PRODUCTOS_2)
while (EDAD_PERMITIDA <= _edadUsuario):
    if (18<=_edadUsuario < 30):
        _productosQuiere = input(PREGUNTA_PRODUCTOS)
        RESPUESTA = input(PREGUNTA_PRODUCTOS_2)
        while (RESPUESTA == "s"):
            _productosQuiere = input(PREGUNTA_PRODUCTOS)
        
    elif (30 <= _edadUsuario < 60):
        print(MENSAJE_DESC_1)
        _productosQuiere = input (PREGUNTA_PRODUCTOS)
    else:
        print(MENSAJE_DESC_2)
        _productosQuiere = input(PREGUNTA_PRODUCTOS)
print("GRACIAS POR SU COMPRA")
    

