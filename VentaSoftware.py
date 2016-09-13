#encoding: UTF-8
#Autor: Diego Perez aka DiegoCodes
#VENTA DE SOFTWARE

def calculadorDescuento(num): #CALCULA DESCUENTO O ERROR
    if (num < 0):
        total = "ERROR"
    if (num > 0 and num < 10):
        total = num*1500
    if (num >= 10 and num <19):
        total = ((num*1500)-((num*1500)*.2))
    if (num >= 20 and num <149):
        total = ((num*1500)-((num*1500)*.3))
    if (num >= 50 and num <99):
        total = ((num*1500)-((num*1500)*.4))
    if (num >= 100):
        total = ((num*1500)-((num*1500)*.5))
    return total
    
def main():
    num = int(input("Ingrese no. de paquetes adquiridos"))
    total = calculadorDescuento(num)
    if (total != "ERROR"):
        print("Su total es de: $",total)
    else:
        print("ERROR")     
main()    