lista = []

def hello_world(mensaje):
    print (mensaje)
    return "Mensaje mostrado exito"

lista.append (1)   
lista.append (26)
lista.append ("mafe")
lista.append ([1,2,3,4])
lista.append (hello_world)
print (lista)
print (lista[4]("hola a todos esto es la funcion"))
 
#adicionando a una lista otra
lista = [10,5,2,7,3,4,8]
lista_adicionar = ["soy","otra","lista"]
lista_adicionar.extend(lista)
print (lista_adicionar)

#insert una variable en un punto en especifico
lista.insert(0,900)
print (lista)

#remover el primer item que tenga coincidencia 
lista.remove(8)
print(lista)

#remover un contenido de una coordenada en especifico,pero
#podemos almacenarlo en otra variable 
valor_eliminado = lista.pop(1)
print (
    lista,
    "el valor eliminado fue el numero {} de la posicion dos de la lista"
    .format(valor_eliminado))

#ubica la posicion de un elemento 
print ("el numero {} esta ubicado en la posicion {} en la lista"
.format(7,lista.index(7)+1),lista)    

lista.append(7)
#contar cuantas hay en una lista
print (
    "en la lista {} aparece el numero {},{} veces"
    .format(lista,7,lista.count(7)))

#clonar dos listas
lista_clonada = lista
lista_clonada.append ("h")   
print("lista original {} vs lista clonada {} "
.format(lista,lista_clonada))
#notemos que si hacemos un cambio en la lista clonada se afecta a la lista original 

#remover la h del ejercicio anterior 
lista.pop(-1)


#y si queremos que genere una copia mas no un clon
lista_copiada = lista.copy()
lista_copiada.append ("h")
print ("lista original {} vs lista copiada {}"
.format(lista,lista_copiada))

#tamaño de una lista
print ("la lista {} tiene un tamaño de {} elementos".format(lista,len(lista)))

#encontrar el numero mas grande de una lista 
print("el numero mas grande de la lista {} es el {}"
.format(lista, max (lista)))
#encontrar el maximo segun el tamaño del string en una lista de strings
lista_str = ["soy", "otra", "lista" ] 
print ("la palabra mas grande en la lista {} es '{}'"
.format(lista_str,max (lista_str, key=len)))

#ordenar lista
#creciente 
lista.sort()
print("lista ordenada creciente {}".format(lista))
#decreciente 
lista.sort(reverse=True)
print("lista ordenada decreciente {}".format(lista))
#lista ordenada usando el tamaño de un string 
lista_str.sort(key=len)
print("lista ordenada creciente {}".format(lista_str))
#decreciente
lista_str.sort(key=len,reverse=True)
print("lista ordenada decreciente {}".format(lista_str))