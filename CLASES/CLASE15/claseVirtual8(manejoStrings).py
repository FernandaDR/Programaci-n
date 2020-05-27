texto = "qui lorem ipsum quia dolor sit amet onsectetur adipisci velit"
print(texto.split('q'))

lista = ["hola", "a", "todos"]
string_of_lista = ' '.join(lista)
print(string_of_lista)
#modificar las q por las t
print('t'.join(texto.split('q')))
lista_palabras_texto = texto.split()
print(lista_palabras_texto)
print ( max (lista_palabras_texto,key=len))
#Esto retorna que a es más grande por el código ASCII
print(max("ZaWU"))
print(min("ZaWU"))
txt_primera_mayuscula= texto.capitalize()
print(txt_primera_mayuscula)
txt_mayuscula= texto.upper()
print(txt_mayuscula)
txt= "HOLA A TODOS"
print (txt.casefold())

txt= "Quiero ir en otro lugar"
print(txt.center(31))

parrafo = "hola cualquier cosa hola cualquier cosa  algo hola cualquier cosa."
print(parrafo.endswith("."))
coordenada_inicio = parrafo.find("algo")
cordenada_final = coordenada_inicio+ len("algo")+1
print(parrafo[coordenada_inicio:cordenada_final])

txt = "AAAA"
print(txt.isnumeric())
print(txt.isalpha())
print(txt.isascii())
print(txt.isprintable())
print(txt.isupper())


txt = "me gusta programar en Java"
print (txt.replace("Java", "Python"))