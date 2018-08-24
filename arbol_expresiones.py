from pila import *
from arbol import *

def convertir(lista, pila):
    if lista != []:
        if lista[0] in "+-*/":
            nodo_der = pila.desapilar()
            nodo_izq = pila.desapilar()
            pila.apilar(Nodo(lista[0],nodo_izq,nodo_der))
        else:
            pila.apilar(Nodo(lista[0]))
        return convertir(lista[1:],pila)
            

def evaluar(arbol):
    if arbol.valor == "+":
        return evaluar(arbol.izq) + evaluar(arbol.der)
    if arbol.valor == "-":
        return evaluar(arbol.izq) - evaluar(arbol.der)
    if arbol.valor == "/":
        return evaluar(arbol.izq) / evaluar(arbol.der)
    if arbol.valor == "*":
        return evaluar(arbol.izq) * evaluar(arbol.der)
    return int(arbol.valor)

def leerExpresionPorArchivo():
    expresion = ""
    contenido = open("archivo.in", "r")
    if contenido.mode == 'r':
        expresion = contenido.read()
    return expresion

def escribirResultado(linea):
    f = open("archivo.out", "w")
    f.write(linea)
    f.close

pila = Pila()

convertir(leerExpresionPorArchivo().split(" "), pila)

evaluacion = evaluar(pila.desapilar())
print(evaluacion)

escribirResultado(str(evaluacion))