#encoding:UTF-8
#Autor: Carlos E. Carbajal Nogués
#Descriipción: Programa que compara el area de dos rectangulos
from Myro import*
from Graphics import *
#Inicio
def calcularArea(base,altura): #Función que calculará el área
    res1 = base*altura
    return res1

def calcularPerimetro(base,altura): #Función que calculará el perimetro
    res2=(2*base)+(2*altura)
    return res2

def compararAreas(area1,area2):#Función que compara las áreas
    if (area1==area2):
        res3=("Las áreas son iguales")
    elif (area1<area2):
        res3=("El área 1 es mayor al área 2")
    else:
        res3=("El área 2 es mayor al área 1")
    return res3
  
def dibujarRectangulos(g,base1,altura1,base2,altura2): #Función que dibuja los rectangulos
    t=Arrow((150,150),90)
    t.draw(g)
    t.penDown()
    t.pen.color = Color("red")
    t.forward(base1)
    t.rotate(90)
    t.forward(altura1)
    t.rotate(90)
    t.forward(base1)
    t.rotate(90)
    t.forward(altura1)
    
    t.penUp()
    t.moveTo(250,250)
    t.penDown()
    t.rotate(90)
    t.forward(base2)
    t.rotate(90)
    t.forward(altura2)
    t.rotate(90)
    t.forward(base2)
    t.rotate(90)
    t.forward(altura2)
    t.pen.color = Color("blue")
    
def main(): #Función principañ
    base1 = int(input("Introduce la base del primer rectángulo"))
    base2=int(input("Introduce la base del segundo rectángulo"))
    altura1 = int(input("Introduce la altura del primer rectángulo"))
    altura2 = int(input("Introduce la altura del segundo rectángulo"))
    g = Window('Rectangulos', 500,500)
    area1 = calcularArea(base1,altura1)
    perimetro1 = calcularPerimetro(base1,altura1)
    area2 = calcularArea(base2,altura2)
    perimetro2 = calcularPerimetro(base2,altura2)
    res = compararAreas(area1,area2)
    dibujarRectangulos(g,base1,altura1,base2,altura2)
    print ("""Las áreas de los rectángulos son: %d , y %d
    Los perimetros son: %d , y %d""" %(area1,area2,perimetro1,perimetro2))
    print (res)

main()
#Fin
