#encoding: UTF-8
#author: Edgar Eduardo Alvarado Durn
#Problema 2

def calcularArea(a1,b1):
    a= a1*b1
    return a
    
def calcularPerimetro(a1,b1):
    p= (a1*2) + (b1*2)
    return p
    
def calcularMayor (a,a3):
    if a>a3:
        print ("El área del rectangulo 1 es mayor")
    else:
        if a3>a:
            print ("El área del rectangulo 2 es mayor")
        else:
            print ("Las áreas son iguales")
        
def main():
    a1= int(input("Dame la altura del primer rectangulo"))
    b1= int(input("Dame la base del primer rectangulo"))
    a2= int(input("Dame la altura del segundo rectangulo"))
    b2= int(input("Dame la base del segundo rectangulo"))
    print ("Rectangulo 1:")
    d1= calcularArea(a1,b1)
    print ("El area del rectangulo 1 es:",d1)
    f1= calcularPerimetro(a1,b1)
    print ("El perimetro del rectangulo 1 es:",f1)
    print ("Rectangulo 2:")
    d2= calcularArea(a2,b2)
    print ("El area del rectangulo 2 es:",d2)
    f2= calcularPerimetro(a2,b2)
    print ("El perimetro del rectangulo 2 es:",f2)
    print ("¿Que area es mayor?:")
    calcularMayor (d1,d2)
        
main()  