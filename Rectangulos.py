#Nombre Ian Gonzlez Pmanes
#Matricula A0373302
#Descripcin Programa que calcula el area y perimetro de dos rectangulos y las compara
def calcularPerimetro(a,b):
    p = 2*a + 2*b
    return p
    
def calcularArea(a,b):
    area = a*b
    return area
 
def main():
    lado1Rectangulo1 = int (input("Ingrese uno de los lados del primer rectangulo"))
    lado2Rectangulo1 = int (input("Ingrese el otro lado del primer rectangulo"))    
    lado1Rectangulo2 = int (input("Ingrese uno de los lados del segundo rectangulo"))
    lado2Rectangulo2 = int (input("Ingrese el otro lado del segundo rectangulo"))    
    
    print ("El area del primer rectangulo es:", calcularArea(lado1Rectangulo1, lado2Rectangulo1), "y su perimetro:", calcularPerimetro(lado1Rectangulo1, lado2Rectangulo1))
    print ("El area del segundo rectangulo es:", calcularArea(lado1Rectangulo2, lado2Rectangulo2), "y su perimetro:", calcularPerimetro(lado1Rectangulo2, lado2Rectangulo2))
    
    if calcularArea(lado1Rectangulo1, lado2Rectangulo1) > calcularArea(lado1Rectangulo2, lado2Rectangulo2):
        print ("El rectangulo 1 tiene un area mayor")
    elif calcularArea(lado1Rectangulo1, lado2Rectangulo1) < calcularArea(lado1Rectangulo2, lado2Rectangulo2):
        print ("El rectangulo 2 tiene un area mayor")
    else:
        print ("Las areas son iguales")

main()