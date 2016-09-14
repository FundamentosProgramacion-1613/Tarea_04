#encoding: UTF-8
#Autor: Aldo Fuentes
#Calcular area y perimetro de rectangulos

from Graphics import *

#Calcula el area de ambos rectangulos a partir de sus dimensiones de base y altura
def calcularAreas(b1, h1, b2, h2):
    a1 = b1*h1
    a2 = b2*h2
    return a1, a2

#Calcula el perimetro de los rectangulos con sus dimensiones de base y altura
def calcularPerimetros(b1, h1, b2, h2):
    p1 = 2*b1 + 2*h1
    p2 = 2*b2 + 2*h2
    return p1, p2

#Compara el area de los rectangulos para encontrar la mayor
def compararRectangulos(a1, a2):
    if a1 > a2:
        comparacion = "El rectangulo 1 tiene mayor area"
    elif a2 > a1:
        comparacion = "El rectangulo 2 tiene mayor area"
    else:
        comparacion = "Tienen las mismas areas"
    return comparacion
    
#Dibuja los rectangulos en una ventana grafica
def dibujarRectangulos(b1, h1, b2, h2, win):
    r1 = Arrow((100,600), 0)
    r1.draw(win)
    r1.penDown()
    r1.pen.color = Color("Red")
    
    for _ in range (0, 2):
        r1.forward(b1)
        r1.rotate(90)
        r1.forward(h1)
        r1.rotate(90)
        
    r2 = Arrow(((200+b1), 600), 0)
    r2.draw(win)
    r2.penDown()
    r2.pen.color = Color("Blue")
    
    for _ in range (0, 2):
        r2.forward(b2)
        r2.rotate(90)
        r2.forward(h2)
        r2.rotate(90)

def main():
    
    b1 = int(input("Teclea la base del rectangulo 1"))
    h1 = int(input("Teclea la altura del rectangulo 1"))
    b2 = int(input("Teclea la base del rectangulo 2"))
    h2 = int(input("Teclea la altura del rectangulo 2"))
    
    win = Window("Tortugas", 900, 700)
    
    dibujarRectangulos(b1, h1, b2, h2, win)
    
    a1, a2 = calcularAreas(b1,h1,b2,h2)
    p1, p2 = calcularPerimetros(b1, h1, b2, h2)
    
    comparacion = compararRectangulos(a1, a2)
    

    
    print("Area del rectangulo 1:", a1, "u^2")
    print("Perimetro de rectangulo 1:", p1, "u")
    print("Area del rectangulo 2:", a2, "u^2")
    print("Perimetro del rectangulo 2:", p2, "u")
    
    print(comparacion)
    
    


main()