from pila import *
from arbol import *

diccionario = {}

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
    print("puto el que lo lea")
    if arbol.valor == "+":
        return evaluar(arbol.izq) + evaluar(arbol.der)
    if arbol.valor == "-":
        return evaluar(arbol.izq) - evaluar(arbol.der)
    if arbol.valor == "/":
        return evaluar(arbol.izq) / evaluar(arbol.der)
    if arbol.valor == "*":
        return evaluar(arbol.izq) * evaluar(arbol.der)
    if arbol.valor == "=":
        diccionario[arbol.der.valor] = evaluar(arbol.izq)
        return str(arbol.der.valor) + " = " + str(arbol.izq)
    return int(arbol.valor)

def leerExpresionPorArchivo():
    expresion = []
    contenido = open("archivo.in", "r")
    contenidoAux = contenido.readlines()
    for x in contenidoAux:
        x = x[:-1]
        expresion.append(x)
    return expresion

def escribirResultado(linea): 
    f = open("archivo.out", "a")
    f.write(linea + '\n')
    f.close

arregloExpresiones = leerExpresionPorArchivo()

f = open("archivo.out", "w")
f.write("")
f.close

for x in arregloExpresiones: 
    pila = Pila()
    expresionFinal = x.split(" ")

    convertir(x.split(" "), pila)

    while(pila.es_vacia != True):
        evaluacion = evaluar(pila.desapilar())


    escribirResultado(str(evaluacion))