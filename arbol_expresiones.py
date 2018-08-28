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
    expresion = []
    contenido = open("archivo.in", "r")
    contenidoAux = contenido.readlines()
    for x in contenidoAux:
        x = x[:-1]
        print(x)
        expresion.append(x)
    return expresion

def escribirResultado(linea):
    f = open("archivo.out", "a")
    f.write(linea + '\n')
    f.close

arregloExpresiones = leerExpresionPorArchivo()

for x in arregloExpresiones:
    pila = Pila()
    expresionFinal = x.split(" ")

    convertir(x.split(" "), pila)

    evaluacion = evaluar(pila.desapilar())
    #diccionario = {}
    #diccionario['a'] = evaluacion

    #print(diccionario)

    escribirResultado(str(evaluacion))