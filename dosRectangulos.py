#encoding: utf-8
#autor: Allan Sánchez Iparrazar 
#dibuja rectángulos 

from Graphics import *

def calcularPerimetro (base,altura):
    perimetro = base*2 + altura*2
    return perimetro
    
def calcularArea (base,altura):
    area = (base*altura)/2
    return area
    
def dibujarRectangulo (t,base,altura,x,y): 
    t.moveTo(x,y)
    t.penDown()
    t.forward(base)
    t.rotate(90)
    t.forward(altura)
    t.rotate(90)
    t.forward(base)
    t.rotate(90)
    t.forward(altura)
    t.penUp()
    t.rotate(90)
    
    

def main():
    v = Window("area de dos rectangulos",450,450)
    t = Arrow((150,200),0)
    t.draw(v)
    

    base1 = float(input("Ingresa la base de tu primer rectángulo"))
    altura1 = float(input("Ingresa la altura de tu primer rectángulo"))
    base2 = float(input("Ingresa la base de tu segundo rectngulo"))
    altura2 = float(input("Ingresa la altura del segundo rectángulo"))
    
    perimetroRectangulo1 = calcularPerimetro(base1,altura1)
    areaRectangulo1 = calcularArea(base1,altura1)
    
    perimetroRectangulo2 = calcularPerimetro(base2,altura2)
    areaRectangulo2 = calcularArea(base2,altura2)
        
    dibujoRectangulo1 = dibujarRectangulo (t,base1,altura1,30,430)
    dibujoRectangulo2 = dibujarRectangulo (t,base2,altura2,30,200)
    
    print("Área del primero rectángulo: %.2f unidades cuadradas"%areaRectangulo1)
    print("Área del segundo rectángulo: %.2f unidades cuadradas"%areaRectangulo2)
    print("***********")
    print("Perimetro del primer rectángulo: %.2f unidades"%perimetroRectangulo1)
    print("Perimetro del segundo rectángulo: %.2f unidades"%perimetroRectangulo2)
    
    rectanguloMayor = comparadorRectangulos(areaRectangulo1,areaRectangulo2)
    
    print (rectanguloMayor)
    
def comparadorRectangulos (areaRectangulo1,areaRectangulo2) :
    
    if areaRectangulo1 > areaRectangulo2 : 
        print ("************")
        valor = "El rectángulo 1 tiene mayor área"        
    
    elif areaRectangulo1 < areaRectangulo2 :
        print ("************")
        valor = "El rectángulo 2 tiene mayor área"
    
    elif areaRectangulo1 == areaRectangulo2 :
        print ("************")
        valor = "Los rectángulos son iguales"
        
    return valor
        
    
main()