#Nombre Ian González Pámanes
#Matricula A0373302
#Descripción Programa que convierte un numero del 1 al 10 a su equivalente romano

def convertirRomano(x):
    if x < 4:
        r = ( x * "I" )
    elif x == 4:
        r = ( "IV")
    elif x == 5:
        r = ("V")
    elif x > 5 and x < 9:
        r = ("V" + (x-5)*"I")
    elif x == 9:
        r = "IX"
    else:
        x = "X"
    return r

def main():
    num = int( input("Escribe un numero del 1 al 10"))
    
    if num >= 1 and num <= 10:
       print (convertirRomano(num))
    else:
       print ("Ese no es un numero valido")
       
       
main() 
       
    
