
#encoding:UTF-8

#Autor:José Javier Rodríguez Mota
#Descripción: Analiza rectangulos (perimetro, area, mayor e imagen)

#Importamos gráficos
from Graphics import *
#Inicio
#Definimos nuestra función para obtener el área 
def obtenerArea(base,altura):
    area=base*altura
    return area   
#Definimos nuestra función para obtener el perimetro
def obtenerPerimetro(base,altura): 
    perimetro=base*2+altura*2
    return perimetro
#Definimos nuestra función para obtener el mayor    
def obtenerMayor(area1,area2):
    if (area1>area2):
        resultado="El rectángulo 1 es el mayor"
    elif (area2>area1):
        resultado="El rectángulo 2 es el mayor"
    else:
        resultado="Los rectángulos tienen la misma área"
    return resultado           
def dibujarRectangulo(base,altura,color,flecha):
    flecha.penDown()
    flecha.pen.color= Color(color)
    for x in range(0,2):
        flecha.forward(base)
        flecha.rotate(90)
        flecha.forward(altura)
        flecha.rotate(90)
    flecha.penUp()
    flecha.forward(2*base)    
#Definimos nuestra función principal
def main():
    base1=int(input("¿Cuál es la base del primer rectángulo?"))
    altura1=int(input("Cuál es la altura del primer rectángulo?"))
    base2=int(input(""))
    altura2=int(input(""))
    area1=obtenerArea(base1,altura1)
    area2=obtenerArea(base2,altura2)
    perimetro1=obtenerPerimetro(base1,altura1)
    perimetro2=obtenerPerimetro(base2,altura2)
    mayor=obtenerMayor(area1,area2)
    ventana=Window("Los dos rectángulos",700,700)
    flecha=Arrow((300,300),0)
    flecha.draw(ventana)
    dibujarRectangulo(base1,altura1,"red",flecha)
    dibujarRectangulo(base2,altura2,"blue",flecha)
    print("""%s

Los datos de los rectángulos son los siguientes

Rectángulo 1(rojo):
base: %d
altura: %d
área: %d
perímetro: %d

Rectángulo 2 (azul):
base: %d
altura: %d
área: %d
perímetro: %d"""%(mayor,base1,altura1,area1,perimetro1,base2,altura2,area2,perimetro2))
main()    