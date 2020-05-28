import sys
def validador_parrafo(parrafo):
    assert(parrafo.endswith("."))
    return False
validador = True

while (validador):
    parrafo =  input("¿Cómo se ha sentido en esta cuarentena?(termine su párrafo con un punto(.)) \n")
    try:
        validador = validador_parrafo(parrafo)
    except AssertionError:
        print("Entrada no válida")