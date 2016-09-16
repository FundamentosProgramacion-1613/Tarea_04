# encoding: UTF-8
# Autor: Rodrigo García López, A01373670
# Descripcion: Cálculo del área y perimetro de dos rectángulo a partir de sus lados

from Graphics import *

# Función que calcula el perimetro de un rectángulo
def calcularPerimetro(a,b):
    perimetro = 2*a+2*b
    return(perimetro)

# Función que calcula el área de un rectángulo
def calcularArea(a,b):
    area = a*b
    return(area)

# Función que dibuja un rectángulo
def dibujarRectangulo(tortuga,a,b):
    tortuga.penDown()
    tortuga.forward(a)
    tortuga.rotate(90)
    tortuga.forward(b)
    tortuga.rotate(90)
    tortuga.forward(a)
    tortuga.rotate(90)
    tortuga.forward(b)
    tortuga.rotate(90)

def main():
    lado1A = int(input("Introduce el largo del primer rectángulo"))
    lado1B = int(input("Introduce el ancho lado del primer rectángulo"))
    lado2A = int(input("Introduce el largo del segundo rectángulo"))
    lado2B = int(input("Introduce el ancho lado del segundo rectángulo"))
    area1 = calcularArea(lado1A, lado1B)
    area2 = calcularArea(lado2A, lado2B)
    perimetro1 = calcularPerimetro(lado1A, lado1B)
    perimetro2 = calcularPerimetro(lado2A, lado2B)
    print("El perímetro del primer rectángulo es ", perimetro1)
    print("El área del primer rectángulo es ", area1)
    print("El perímetro del segundo rectángulo es ", perimetro2)
    print("El área del segundo rectángulo es ", area2)
    if area1>area2:
        print("El área del primer rectángulo es mayor")
    elif area1==area2:
        print("Las áreas de ambos rectángulos son iguales")
    else:
        print("El área del segundo rectángulo es mayor")
    ventana = Window("Rectángulos", 800, 800)
    tortuga = Arrow ((400,400),0)
    tortuga.draw(ventana)
    tortuga.pen.color = Color("Orange")
    dibujarRectangulo(tortuga, lado1A, lado1B)
    tortuga.penUp()
    tortuga.pen.color = Color("Blue")
    tortuga.forward(lado1A+10)
    dibujarRectangulo(tortuga, lado2A, lado2B)
       
main()