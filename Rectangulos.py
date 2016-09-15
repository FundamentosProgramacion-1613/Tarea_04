#Encoding UTF-8
#Oswaldo Morales Rodriguez
#Conociendo las medidas de rectangulos dibujarlos y decir cual es mas grande

from Graphics import *
def calcularPerimetro1(largo1,ancho1):
    perimetro1=(largo1*2)+(ancho1*2)
    return perimetro1

def calcularPerimetro2(largo2,ancho2):
    perimetro2=(largo2*2)+(ancho2*2)
    return perimetro2
    
def calcularArea1(largo1,ancho1):
    area1=largo1*ancho1
    return area1
    
def calcularArea2(largo2,ancho2):
    area2=largo2*ancho2
    return area2
    
def dibujarRectangulo1(largo1,ancho1,t1,v):
    t1.penDown
    t1.draw(v)
    t1.forward(largo1)
    t1.rotate(90)
    t1.forward(ancho1)
    t1.rotate(90)
    t1.forward(largo1)
    t1.rotate(90)
    t1.forward(ancho1)
    t1.rotate(90)
    
def dibujarRectangulo2(largo2,ancho2,t2,v):
    t2.penDown
    t2.draw(v)
    t2.forward(largo2)
    t2.rotate(90)
    t2.forward(ancho2)
    t2.rotate(90)
    t2.forward(largo2)
    t2.rotate(90)
    t2.forward(ancho2)
    t2.rotate(90)
    
    
def compararAreas(areaPrimero,areaSegundo):
    if(areaPrimero<areaSegundo):
        mensaje=("El segundo tiene mayor area")
    elif(areaPrimero==areaSegundo):
        mensaje=("Tienen la misma area")
    else:
        mensaje=("El primero tiene mayor area")
    return mensaje
    

def main():
    largo1=int(input("Medida del largo del primer rectangulo"))
    ancho1=int(input("Medida del ancho del primer rectangulo"))
    largo2=int(input("Medida del largo del segundo rectangulo"))
    ancho2=int(input("Medida del ancho del segundo rectangulo"))
    perimetroPrimero=calcularPerimetro1(largo1,ancho1)
    perimetroSegundo=calcularPerimetro2(largo2,ancho2)
    areaPrimero=calcularArea1(largo1,ancho1)
    areaSegundo=calcularArea2(largo2,ancho2)
    t1=Arrow((0,300),0)
    t2=Arrow((0,600),0)
    comparar=compararAreas(areaPrimero,areaSegundo)
    print("El primero tiene un perimetro de",perimetroPrimero, "y un area de",areaPrimero)
    print("El primero tiene un perimetro de",perimetroSegundo, "y un area de",areaSegundo)
    print(comparar)
    v=Window("Rectangulos",1200,900)
    dibujarRectangulo1(largo1,ancho1,t1,v)
    dibujarRectangulo2(largo2,ancho2,t2,v)

main()