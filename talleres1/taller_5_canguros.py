#-----------MENSAJES------------
MENSAJE_ID = " El número de identificación de este Canguro es :"
MENSAJE_EDAD = " Este canguro tiene "
MENSAJE_NOMBRE = " El nombre del cuidador es :"
MENSAJE_CC = "El número de idenificación del cuidador es :"

class Canguro():

    def __init__(self,id,edad):
        
        self.id = id
        self.edad = edad
    
    def mostrar_atributos(self):
        print (MENSAJE_ID, self.id)
        print (MENSAJE_EDAD, self.edad, "años")
    
    def saltar(self,cantidad_saltos):
        for i in range (cantidad_saltos):
            print ( "El canguro ha dado", i+1, "saltos")

class Cuidador():

    def __init__(self,cc,nombre):
        
        self.cc = cc
        self.nombre = nombre
    
    def mostrar_atributos(self):
        print (MENSAJE_CC, self.cc)
        print (MENSAJE_NOMBRE, self.nombre)
    
    def canguros_alimentados(self,cantidad_canguros_alimentados):
        for i in range (cantidad_canguros_alimentados):
            print ( "El cuidador ha alimentado", i+1, "canguros")

class Jefe():

    def __init__(self,cc,nombre):
        self.cc = cc
        self.nombre = nombre

    def dar_mensaje (self,mensaje):
        print(mensaje)

    def contratar_cuidador(self,cantidad_cuidadores_contratados):
        for i in range (cantidad_cuidadores_contratados):
            print ( "El jefe ha contratado", i+1, "cuidadores")
       
canguro_1 = Canguro(2001,8)
canguro_2 = Canguro(2002,3)
canguro_3 = Canguro(2004,1)
canguro_4 = Canguro(2005,6)
canguro_5 = Canguro(2006,7)
canguro_6 = Canguro(2007,1)
canguro_7 = Canguro(2008,5)
canguro_8 = Canguro(2009,12)
canguro_9 = Canguro(2010,2)
canguro_10 = Canguro(2011,4)

       
canguro_1.mostrar_atributos()

canguro_1.saltar(10)

cuidador_1 = Cuidador(1005632845, "Andrés")
cuidador_2 = Cuidador(1090654875, "Samantha")
cuidador_3 = Cuidador(37255964, "Rosa")
cuidador_4 = Cuidador(63452987, "Martín")
cuidador_5 = Cuidador(1203658549,"Lucía")

cuidador_1.mostrar_atributos()

cuidador_1.canguros_alimentados(5)

jefe_1 = Jefe(88719653,"Pedro")

jefe_1.dar_mensaje(" Hola, soy el jefe y en nombre de todos los cuidadores... Tenemos el mejor trabajo del mundo ")
jefe_1.contratar_cuidador(5)


