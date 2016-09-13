#encoding: UTF-8
#Autor: Diego Perez aka DiegoCodes
#AREAS DE RECTANGULOS
from Graphics import *
def calculadorArea(alt0,base0,alt1,base1): #CALCULA AREA DE AMBOS RECTANGULOS
    area_0 = alt0*base0
    area_1 = alt1*base1
    return area_0,area_1

def calculadorPerimetro(alt0,base0,alt1,base1):#SUMA LOS LADOS DE LOS RECTANGULOS
    peri_0 = alt0*base0
    peri_1 = alt1*base1
    return peri_0,peri_1
    
def dibujarRectangulos(x,alt,base,col,win): # DIBUJA UN RECTANGULO,UTLIZA COLOR
    line0 = Line((x,x),(x+base,x))
    line0.color = Color(col)
    line0.draw(win)
    line1 = Line((x+base,x),(x+base,x+alt))
    line1.color = Color(col)
    line1.draw(win)
    line2 = Line((x,x),(x,x+alt))
    line2.color = Color(col)
    line2.draw(win)
    line3 = Line((x,x+alt),(x+base,x+alt))
    line3.color = Color(col)
    line3.draw(win)
 
def calculadorEscalas(area_0,area_1): #Calcula el area mayor
    if area_0 > area_1:
        conclusion = "El area del primer rectangulo es mayor"
    if area_0 < area_1:
        conclusion = "El area del segundo rectangulo es mayor"
    if area_0 == area_1:
        conclusion = "Las areas son iguales"
    return conclusion   
       
def main():    
    alt0 = int(input("Ingrese altura del 1er rectangulo"))
    base0 = int(input("ingrese base del 1er rectangulo"))
    alt1 = int(input("Ingrese altura del 2do rectangulo"))
    base1 = int(input("ingrese base del 2do rectangulo"))
        
    win = Window("Rectangulos",960,540)
    dibujarRectangulos(75,alt0,base0,"Green",win)
    dibujarRectangulos(80+base1,alt1,base1,"Red",win)
    
    (area_0,area_1) = calculadorArea(alt0,base0,alt1,base1)
    (peri_0,peri_1) = calculadorPerimetro(alt0,base0,alt1,base1)
    
    print("El area del primero es de",area_0,"u^3")
    print("El area del segundo es de",area_1,"u^3")
    
    print("El perimetro del primero es de",peri_0,"u")
    print("El perimetro del segundo es de",peri_1,"u")
    
    conclusion = calculadorEscalas(area_0,area_1)
    print(conclusion)
    
main()       