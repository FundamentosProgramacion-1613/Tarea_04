#encoding: UTF-8
#Autor: Manuel Alejandro Bracho Mendoza
#Matricula del autor: A01378897
#Ejercicio n°2 de la tarea 4 ¬

from Graphics import *

def calcularAreaRectangulo (base, altura):
    areaRectangulo = base * altura
    return areaRectangulo

def calcularPerimetroRectangulo (base, altura):
    perimetroRectangulo = base + base + altura + altura
    return perimetroRectangulo
    
    
def main():
    basePrimerRectangulo = float(input("escriba la base de el primer rectangulo"))
    alturaPrimerRectangulo = float(input("escriba la altura del segundo rectangulo"))
    baseSegundoRectangulo = float(input("escriba la base del segundo rectangulo"))
    alturaSegundoRectangulo = float(input("escriba la altura del segundo rectangulo"))
    
    areaPrimerRectangulo = calcularAreaRectangulo(basePrimerRectangulo, alturaPrimerRectangulo)
    perimetroPrimerRectangulo = calcularPerimetroRectangulo (basePrimerRectangulo, alturaPrimerRectangulo)
    areaSegundoRectangulo = calcularAreaRectangulo (baseSegundoRectangulo, alturaSegundoRectangulo)
    perimetroSegundoRectangulo = calcularPerimetroRectangulo (baseSegundoRectangulo, alturaSegundoRectangulo)
    
    if areaPrimerRectangulo > areaSegundoRectangulo and areaPrimerRectangulo != areaSegundoRectangulo:
        print("el Primer rectangulo es más grande que el segundo rectangulo")
    elif areaPrimerRectangulo == areaSegundoRectangulo:
        print("los dos rectangulos son iguales")
    else:
     print("el segundo rectangulo es más grande que el primer rectangulo")
     
     #Profe, intente mucho hacer la grafica, pero no me salio, me gustaria ir el lunes a acesoria, aunque tenga que sacrificar una clase para que me ayude a resolverlo, gracias de antemano. 
     

main()
        
    