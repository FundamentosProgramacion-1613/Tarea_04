#encoding: UTF-8
#Karla Valeria Alcánatara Duarte
#Perímetro y área de rectángulos

from Graphics import *

def calcularPerimetro(lado1,lado2):
    perimetro = (lado1*2)+(lado2*2)
    return perimetro
    
def calcularArea(base,altura):
    area = base*altura
    return area
    
def calcularAreaMayor(areaRec1, areaRec2):
    if areaRec1>areaRec2:
        mayor = "El primer rectangulo tiene un área mayor"
    elif areaRec1<areaRec2:
        mayor = "El segundo rectangulo tiene un área mayor"
    else:
        mayor = "Ambas áreas son iguales"
    return mayor
    
def dibujarRectangulo(t,lado1,lado2):
    t.forward(lado1)
    t.rotate(90)
    t.forward(lado2)
    t.rotate(90)
    t.forward(lado1)
    t.rotate(90)
    t.forward(lado2)
    t.rotate(90)
    
    
def main():
    lado1Rec1 = int(input("Base del primer rectangulo"))
    lado2Rec1 = int(input("Altura del primer rectangulo"))
    lado1Rec2 = int(input("Base del segundo rectangulo"))
    lado2Rec2 = int(input("Altura del segundo rectangulo"))
    perimetroRec1 = calcularPerimetro(lado1Rec1,lado2Rec2)
    areaRec1 = calcularArea(lado1Rec1,lado2Rec2)
    perimetroRec2 = calcularPerimetro(lado1Rec2,lado2Rec2)
    areaRec2 = calcularArea(lado1Rec2,lado2Rec2)
    areaMayor = calcularAreaMayor(areaRec1,areaRec2)
    print("El perimetro del primer rectangulo es:",perimetroRec1,"y el área:",areaRec1)
    print("El perimetro del segundo rectangulo es:",perimetroRec2,"y el área:",areaRec2)
    print(areaMayor)
    v = Window("Rectangulos",600,600)
    t = Arrow((150,300),0)
    t.penDown()
    t.draw(v)
    t.pen.color = Color("Red")
    dibujarRectangulo(t,lado1Rec1,lado2Rec1)
    t.penUp()
    t.moveTo(450,300)
    t.penDown()
    t.pen.color = Color("Blue")
    dibujarRectangulo(t,lado1Rec2,lado2Rec2)
    
    
main()
    