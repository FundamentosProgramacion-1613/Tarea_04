#Nombre Ian Gonzlez Pmanes
#Matricula A0373302
#Descripcin Programa que calcula el % de descuento dependiendo de la cantidad comprada

def calcularDescuento(a):
    if a > 0 and a < 10:
        precio = a*1500
    elif a >= 10 and a <= 19:
        precio = a*1500*.8
    elif a >= 20 and a <= 49:
        precio = a*1500*.7
    elif a >= 50 and  a <= 99:
        precio = a*1500*.6
    elif a >= 100:
        precio = a*1500*.5
    else:
        precio = "Cantidad invalida"
        
    return precio
    
def main():
    paquetes = int( input("Cuantos paquetes desea comprar?"))
    
    print ("El total de su compra seria:", calcularDescuento(paquetes))
    
main()
