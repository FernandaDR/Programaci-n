MENSAJE_MENU ="""Menú:
1. Mostrar los atributos de los estudiantes 
2. Mostrar los atributos de los profesores
3. Mostrar los atributos del director 
4- Salir \n"""
MENSAJE_NUMERO ="Ingrese un numero por favor : \n "
SALIR ="Usted ha salido del programa"

listaNombresEstudiantes = []
listaEdadEstudiantes = []
listaGeneroEstudiante = []
listaColgraduadoEstudiante = []

listaNombresProfes = []
listaEdadesProfes = []
listaNivelesProfes = []

_numeroIngresado = 0



class Estudiante ():
    def __init__(self,nombre,edad,genero,colGraduado):
        
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.colGraduado = colGraduado
        listaNombresEstudiantes.append(nombre)
        listaEdadEstudiantes.append(edad)
        listaGeneroEstudiante.append(genero)
        listaColgraduadoEstudiante.append(colGraduado)
    
    def asistir_clases(self,cantidadClases):
        for i in range (cantidadClases):
            print ( "El estudiante ha sistido a ", i+1, "clases en el día")

    def mostrar_atributos(self):
        print ("El nombre del estudiante es", self.nombre,
               ", tiene",self.edad,"años",", es de genero",self.genero,
               "y viene del colegio",self.colGraduado)
    
    

class Profesor ():
    def __init__(self,nombre,edad,nivelEducativo):
        
        self.nombre = nombre
        self.edad = edad
        self.nivelEducativo =nivelEducativo
        listaNombresProfes.append(nombre)
        listaEdadesProfes.append(edad)
        listaNivelesProfes.append(nivelEducativo)
    
    def dictar_clases(self,cantidadClases):
        for i in range (cantidadClases):
            print ( "El profesor ha dictado", i+1, "clases en el día")

    def mostrar_atributos(self):
        print ("El nombre del profesor es", self.nombre,
               ", tiene",self.edad,"años",
               "y tiene un nivel educativo de",self.nivelEducativo)

class Director (Profesor): 
    def contratar (self,nombre,edad,nivelEducativo):
        profesor = Profesor(nombre,edad,nivelEducativo)
        return profesor
    def mostrar_atributos(self):
        print ("El nombre del director es", self.nombre,
               ", tiene",self.edad,"años",
               "y tiene un nivel educativo de",self.nivelEducativo)

def mostrar_cuatro_listas (lista_1,lista_2,lista_3,lista_4):
    posicion = 1
    for elemento in range(len(lista_1)):
        print (lista_1[elemento],lista_2[elemento],lista_3[elemento],lista_4[elemento])
        posicion += 1
    return()

def mostrar_tres_listas (lista_1,lista_2,lista_3):
    posicion = 1
    for elemento in range(len(lista_1)):
        print (lista_1[elemento],lista_2[elemento],lista_3[elemento])
        posicion += 1
    return()

estudiante_1 = Estudiante("Mateo",16,"masculino","buenaventura del evangelio")
estudiante_2 = Estudiante("Antonia",15,"femenino","Hermanitas de la caridad")
estudiante_3 = Estudiante("Oscar",22,"Masculino","El portón del futuro")
estudiante_4 = Estudiante("Ester",18,"femenino","La diocesana")
estudiante_1 = Estudiante("Andrea",19,"femenino","santos apostoles")

profe_1 = Profesor("Julian",63,"Doctorado")
profe_2 = Profesor("Felix",45,"Epecialización")

director_1 = Director("Jorge",69,"Magister")


estudiante_1.mostrar_atributos()
estudiante_1.asistir_clases(8)

profe_1.mostrar_atributos()
profe_1.dictar_clases(5)

profe_3 = director_1.contratar("Antonio",39,"Especialista")
profe_3.mostrar_atributos
profe_4 =director_1.contratar("Marcela",27,"Especialista")
profe_4.mostrar_atributos
director_1.mostrar_atributos()

while ( _numeroIngresado != 4):
    print (MENSAJE_MENU)
    _numeroIngresado = int(input(MENSAJE_NUMERO))
    if (_numeroIngresado == 1):
        print("Nombre:", "Edad:", "Genero:", "Colegio: \n")
        mostrar_cuatro_listas(listaNombresEstudiantes,listaEdadEstudiantes,listaGeneroEstudiante,listaColgraduadoEstudiante)  
    elif (_numeroIngresado == 2 ):
        print("Nombre:", "Edad:", "Nivel académico: \n")
        mostrar_tres_listas(listaNombresProfes,listaEdadesProfes,listaNivelesProfes)
    elif (_numeroIngresado == 3):
        director_1.mostrar_atributos()
    else: 
        print(SALIR)


