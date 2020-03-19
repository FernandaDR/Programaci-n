class Persona():
    def __init__(self,nombre,estatura,peso,genero,edad):
        
        self.raza = "ser humano"
        self.nombre = nombre
        self.estatura = estatura
        self.peso =  peso
        self.genero = genero
        self.edad = edad
        print("hola a todos soy un",self.raza, "mi nombre es", self.nombre)

    def mostrar_atributos(self):
        print ("mi nombre es", self.nombre)
        print ("mi estatura es", self.estatura)
        print ( "mi peso es", self.peso)
        print ("mi genero es", self.genero)
        print ("mi edad es", self.edad)

    def caminar(self,cantidad_pasos):
        for i in range (cantidad_pasos):
            print ( "he caminado", i+1, "pasos")

ser_humano_1 = Persona("Daniel",1.67,77,"Masculino",26)
ser_humano_2 = Persona("Mafer",1.64,50,"Femenino",26)

ser_humano_1.mostrar_atributos()
ser_humano_2.mostrar_atributos()

ser_humano_1.caminar(100)
