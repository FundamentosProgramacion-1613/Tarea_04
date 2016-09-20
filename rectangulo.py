#encoding: UTF-8
# Autor: Marlon Brandon Velasco Pinello, A01379404
# Descripcion: Rectangulos Tarea 4

#importamos la libreria de graficos
from Graphics import *

#definimos una ventana
def ventana():
    v = Window("Rectangulos",800,600)
    t = Arrow((100,350),0)
    t.draw(v)
    return t

#calculamos el area del rectangulo
def calcularAreaRectangulo(base,altura):
    area=base*altura
    return area

#calculamos el perimetro
def calcularPerimetroRectangulo(base,altura):
    perimetro=(base*2)+(altura*2)
    return perimetro

#calculamos el area mayor    
def calcularAreaMayor(area1,area2):
    if area1!=area2:
        if area1 > area2:
            areaMayor="El rectangulo con mayor area es el 1"
        else:
            areaMayor="El rectangulo con mayor area es el 2"
    else:
        areaMayor="Las areas son iguales"
    return areaMayor
  
#funcion para dibujar el rectangulo  
def dibujarRectangulo(t,base,altura):
    t.penDown()
    for i in range(2):
        t.forward(base)
        t.rotate(90)
        t.forward(altura)
        t.rotate(90)
    t.penUp()
    
#funcion principal main
def main():
    base1=int(input("Ingresa la medida de la base del primer rectangulo"))
    altura1=int(input("Ingresa la medida de la altura del primer rectangulo"))
    base2=int(input("Ingresa la medida de la base del segundo rectangulo"))
    altura2=int(input("Ingresa la medida de la altura del segundo rectangulo"))
    areaRectangulo1=calcularAreaRectangulo(base1,altura1)
    perimetroRectangulo1=calcularPerimetroRectangulo(base1,altura1)
    areaRectangulo2=calcularAreaRectangulo(base2,altura2)
    perimetroRectangulo2=calcularPerimetroRectangulo(base2,altura2)
    resultado=calcularAreaMayor(areaRectangulo1,areaRectangulo2)
    print(" El area del rectangulo 1 es:",areaRectangulo1)
    print(" El perimetro del rectangulo 1 es:",perimetroRectangulo1)
    print(" El area del rectangulo 2 es:",areaRectangulo2)
    print(" El perimetro del rectangulo 2 es:",perimetroRectangulo2)
    print("",resultado)
    t = ventana()
    t.pen.color= Color("blue")
    dibujarRectangulo(t,base1,altura1)
    t.moveTo(500,350)
    t.pen.color= Color("red")
    dibujarRectangulo(t,base2,altura2)
    
main()