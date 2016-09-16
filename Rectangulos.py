#encoding = UTF-8
#Adrian Tellez
#Sacar area y perimetro de 2 rectangulos, compararlos y dibujarlos
from Graphics import *
        
def main():
    ancho1 = float(input("Pon el ancho del primer rectangulo en cm"))
    ancho2 = float(input("Pon el ancho del segundo rectangulo en cm"))
    largo1 = float(input("Pon el largo del primer rectangulo en cm"))
    largo2 = float(input("Pon el largo del segundo rectangulo en cm"))
    areas = calcularArea(ancho1, ancho2, largo1, largo2)
    perimetros = calcularPerimetro(ancho1, ancho2, largo1, largo2)
    grande = calcularGrande (area1, area2)
    ventana = Window ("Tortuga", 600, 600)
    tortuga = Arrow ((300, 300), 0)
    tortuga.draw(ventana)
    dibujarRectangulo (tortuga,ancho1, ancho2, largo1, largo2) 
    print ("El area del primer rectangulo es:", area1, "cm y del segundo:", area2, "cm")
    print ("El perimetro del primer rectangulo es:", perimetro1, "y del segundo:", perimetro2)
    print (grande)
    
    

def calcularArea(ancho1, ancho2, largo1, largo2):
    global area1, area2
    area1 = ancho1 * largo1
    area2 = ancho2 * largo2
    return area1, area2
    
def calcularPerimetro (ancho1, ancho2, largo1, largo2):
    global perimetro1, perimetro2
    perimetro1 = (ancho1 * 2) + (largo1 * 2)
    perimetro2 = (ancho2 * 2) + (largo2 * 2)
    return perimetro1, perimetro2
    
    
def calcularGrande(area1, area2):
    if area1 < area2:
        return ("El area del segundo rectangulo es mayor al del primero")
    elif area1 > area2:
        return ("El area del primer rectangulo es mayor al del segundo")
    else:
        return ("Ambas areas son iguales")
    
def dibujarRectangulo (tortuga,ancho1, ancho2, largo1, largo2):
    tortuga.moveTo(500,500)
    tortuga.penDown()
    tortuga.pen.color = Color("Blue")
    tortuga.forward(ancho1)
    tortuga.rotate(90)
    tortuga.forward(largo1)
    tortuga.rotate(90)
    tortuga.forward(ancho1)
    tortuga.rotate(90)
    tortuga.forward(largo1)
    tortuga.rotate(90)
    tortuga.penUp()
    tortuga.forward(ancho1 + 50)
    tortuga.pen.color = Color("Green")
    tortuga.penDown()
    tortuga.forward(ancho2)
    tortuga.rotate(90)
    tortuga.forward(largo2)
    tortuga.rotate(90)
    tortuga.forward(ancho2)
    tortuga.rotate(90)
    tortuga.forward(largo2)
    tortuga.rotate(90)
    
    
main()
    
