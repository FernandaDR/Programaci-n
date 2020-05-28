import sys
#________Entradas________
_pesoUsuario = 0.0
_edadUsuario = 0
_estaturaUsuario = 0.0
_nombreUsuario = " "

_nombreUsuario = input("Ingrese su nombre: ")
_edadUsuario = int (input("Ingrese su edad: "))
_pesoUsuario = float(input("Ingrese su peso: "))
_estaturaUsuario = float(input("Ingrese su estatura: "))
try: 
    peso = _pesoUsuario
    estatura = _estaturaUsuario
except ValueError: 
    print ("No ingresaste valores adecuado")
IMC = (_pesoUsuario / (_estaturaUsuario**2))
print ("{} su indice de masa corporal es {}".format (_nombreUsuario , IMC))