#encoding: UTF-8
#Adrian E. Tellez Lopez
#Transformar numeros naturales a romanos

def main():
    Numero = int(input("Pon un numero del 1 al 10"))
    romano = calcularRomano(Numero)
    print("El numero en romano es:", romano)
    

def calcularRomano (Numero):
    if Numero < 4 and Numero > 0:
        numero = (Numero * "I")
    elif Numero == 4:
        numero= ("IV")
    elif Numero > 4 and Numero < 9:
        numero = ("V" + "I"*(Numero-5))
    elif Numero == 9:
        numero = ("IX")
    elif Numero == 10:
        numero = ("X")
    else:
        numero = ("Error: el numero no esta dentro del rango")
        
    return numero

def main():
    Numero = int(input("Pon un numero del 1 al 10"))
    romano = calcularRomano(Numero)
    print("El numero en romano es:", romano)
    
main()